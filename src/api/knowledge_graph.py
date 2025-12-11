# src/api/knowledge_graph.py

from fastapi import APIRouter, BackgroundTasks, status, Depends
from typing import Dict, Any, Optional
import uuid
from pydantic import BaseModel

# Import the main components of the new architecture
from src.core.agent_manager import AgentManager
from src.core.orchestrator import Orchestrator
from src.agents.demand_analysis_agent import DemandAnalysisAgent
from src.agents.validation_coordinator_agent import ValidationCoordinatorAgent
from src.agents.course_agent import CourseAgent
from src.agents.multimodal_parser_agent import MultimodalParserAgent
from src.agents.internet_scraper_agent import InternetScraperAgent
from src.agents.academic_scraper_agent import AcademicScraperAgent
from src.agents.content_understanding_agent import ContentUnderstandingAgent
from src.agents.theoretical_analysis_agent import TheoreticalAnalysisAgent
from src.agents.practical_analysis_agent import PracticalAnalysisAgent
from src.agents.kg_builder_agent import KgBuilderAgent
from src.agents.report_generation_agent import ReportGenerationAgent

from src.config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL # Import API credentials

router = APIRouter()

# In a real application, you might have a global dictionary or a database
# to track the status and results of running tasks.
pipeline_tasks = {}

class KGBuildRequest(BaseModel):
    course_name: str
    data_path: Optional[str] = None

async def run_pipeline_background(course_name: str, data_path: Optional[str], task_id: str):
    """The function that will run in the background."""
    try:
        # This is the same setup as in the __main__ block of orchestrator.py
        agent_manager = AgentManager()
        
        # Register Agents
        agent_manager.register_agent(DemandAnalysisAgent, "DemandAnalysisAgent", "Analyzes user requirements.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(CourseAgent, f"{course_name}_CourseAgent", f"Provides resources for the {course_name} course.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(InternetScraperAgent, "InternetScraperAgent", "Scrapes web pages.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(AcademicScraperAgent, "AcademicScraperAgent", "Scrapes academic papers.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(ContentUnderstandingAgent, "ContentUnderstandingAgent", "Processes raw data into drafts.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(TheoreticalAnalysisAgent, "TheoreticalAnalysisAgent", "Ensures theoretical rigor of knowledge points.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(PracticalAnalysisAgent, "PracticalAnalysisAgent", "Finds practical examples for knowledge points.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(KgBuilderAgent, "KgBuilderAgent", "Builds and integrates knowledge graphs.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)
        agent_manager.register_agent(ReportGenerationAgent, "ReportGenerationAgent", "Generates final reports from the knowledge graph.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)

        orchestrator = Orchestrator(agent_manager)
        
        # Define Gates
        async def demand_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            # Simplified logic for brevity in API
            return await validation_agent.organize_review("Demand Specification Document Review", context.get("demand_spec_doc", ""))

        async def data_acceptance_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            # Simplified logic for brevity in API
            return await validation_agent.organize_review("Data Acceptance Review", context.get("knowledge_point_drafts", []))

        async def subject_level_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            # Simplified logic for brevity in API
            return await validation_agent.organize_review("Subject Level Review", context.get("subgraphs", {}).get(course_name, []))

        async def final_result_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            return await validation_agent.organize_integration_test(context)

        # Add Stages
        orchestrator.add_stage("Stage1_DemandAnalysisAndPlanning", ["DemandAnalysisAgent"], demand_review_gate, "Analyze user requirements and create an overall subject plan.")
        orchestrator.add_stage("Stage2_DataCollectionAndPreprocessing", [f"{course_name}_CourseAgent", "MultimodalParserAgent", "InternetScraperAgent", "AcademicScraperAgent", "ContentUnderstandingAgent"], data_acceptance_gate, "Collect and preprocess data into standardized knowledge point drafts.")
        orchestrator.add_stage("Stage3_KnowledgeRefinementAndCourseConstruction", ["TheoreticalAnalysisAgent", "PracticalAnalysisAgent", "KgBuilderAgent"], subject_level_review_gate, "Refine knowledge points, add practical examples, and build a course sub-graph.")
        orchestrator.add_stage("Stage4_KnowledgeGraphIntegrationAndValidation", [("KgBuilderAgent", "integrate_kps"), ("ValidationCoordinatorAgent", "organize_integration_test")], final_result_review_gate, "Integrate sub-graphs into a unified knowledge graph and perform validation.")
        orchestrator.add_stage("Stage5_ReportGenerationAndDelivery", ["ReportGenerationAgent"], None, "Generate and deliver the final report.")

        initial_context = {"course_name": course_name}
        if data_path:
            initial_context["data_path"] = data_path
        
        pipeline_tasks[task_id] = {"status": "running", "result": None}
        final_context = await orchestrator.run_pipeline(initial_context)
        
        pipeline_tasks[task_id]["status"] = "completed"
        pipeline_tasks[task_id]["result"] = {
            "final_report_path": f"./{course_name.replace(' ', '_')}_KG_Report.md",
            "pipeline_status": orchestrator.get_pipeline_status()
        }

    except Exception as e:
        pipeline_tasks[task_id]["status"] = "failed"
        pipeline_tasks[task_id]["result"] = str(e)


@router.post("/build", status_code=status.HTTP_200_OK)
async def build_knowledge_graph(request: KGBuildRequest, background_tasks: BackgroundTasks):
    """
    Triggers the asynchronous pipeline to build a knowledge graph for the specified course.
    Optionally accepts a data_path for local file processing.
    """
    task_id = str(uuid.uuid4())
    background_tasks.add_task(run_pipeline_background, request.course_name, request.data_path, task_id)
    pipeline_tasks[task_id] = {"status": "starting", "result": None}
    return {"message": "Pipeline started.", "task_id": task_id, "status_endpoint": f"/build/status/{task_id}"}

@router.get("/build/status/{task_id}")
async def get_build_status(task_id: str):
    """
    Retrieves the status of a running pipeline task.
    """
    task = pipeline_tasks.get(task_id)
    if not task:
        return {"message": "Task not found.", "status": "error"}
    return task
