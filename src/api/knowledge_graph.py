# src/api/knowledge_graph.py

from fastapi import APIRouter, BackgroundTasks
from typing import Dict, Any

# Import the main components of the new architecture
from src.core.agent_manager import AgentManager
from src.core.orchestrator import Orchestrator
from src.agents.demand_analysis_agent import DemandAnalysisAgent
from src.agents.subject_overview_agent import SubjectOverviewAgent
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

router = APIRouter()

# In a real application, you might have a global dictionary or a database
# to track the status and results of running tasks.
pipeline_tasks = {}

async def run_pipeline_background(course_name: str, task_id: str):
    """The function that will run in the background."""
    try:
        # This is the same setup as in the __main__ block of orchestrator.py
        agent_manager = AgentManager()
        
        # Register Agents
        agent_manager.register_agent(DemandAnalysisAgent, "DemandAnalysisAgent", "Analyzes user requirements.")
        agent_manager.register_agent(SubjectOverviewAgent, "SubjectOverviewAgent", "Creates an overall subject plan.")
        agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.")
        agent_manager.register_agent(lambda name, description: CourseAgent(name, description, course_name), f"{course_name}_CourseAgent", f"Provides resources for the {course_name} course.")
        agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.")
        agent_manager.register_agent(InternetScraperAgent, "InternetScraperAgent", "Scrapes web pages.")
        agent_manager.register_agent(AcademicScraperAgent, "AcademicScraperAgent", "Scrapes academic papers.")
        agent_manager.register_agent(ContentUnderstandingAgent, "ContentUnderstandingAgent", "Processes raw data into drafts.")
        agent_manager.register_agent(TheoreticalAnalysisAgent, "TheoreticalAnalysisAgent", "Ensures theoretical rigor of knowledge points.")
        agent_manager.register_agent(PracticalAnalysisAgent, "PracticalAnalysisAgent", "Finds practical examples for knowledge points.")
        agent_manager.register_agent(KgBuilderAgent, "KgBuilderAgent", "Builds and integrates knowledge graphs.")
        agent_manager.register_agent(ReportGenerationAgent, "ReportGenerationAgent", "Generates final reports from the knowledge graph.")

        orchestrator = Orchestrator(agent_manager)
        
        # Define Gates
        async def demand_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            # Simplified logic for brevity in API
            return await validation_agent.review_document("Demand Specification Document", context.get("demand_spec_doc", ""), "Ensure goals and scope are defined.")

        async def data_acceptance_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            return len(context.get("knowledge_point_drafts", [])) > 0

        async def subject_level_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            return len(context.get("subgraphs", {}).get(course_name, [])) > 0

        async def final_result_review_gate(context: Dict[str, Any], am: AgentManager) -> bool:
            validation_agent = am.get_agent("ValidationCoordinatorAgent")
            return await validation_agent.perform_integration_test(context)

        # Add Stages
        orchestrator.add_stage("Stage1", ["DemandAnalysisAgent", "SubjectOverviewAgent"], demand_review_gate)
        orchestrator.add_stage("Stage2", [f"{course_name}_CourseAgent", "MultimodalParserAgent", "InternetScraperAgent", "AcademicScraperAgent", "ContentUnderstandingAgent"], data_acceptance_gate)
        orchestrator.add_stage("Stage3", ["TheoreticalAnalysisAgent", "PracticalAnalysisAgent", "KgBuilderAgent"], subject_level_review_gate)
        orchestrator.add_stage("Stage4", [("KgBuilderAgent", "integrate_and_store"), ("ValidationCoordinatorAgent", "perform_integration_test")], final_result_review_gate)
        orchestrator.add_stage("Stage5", ["ReportGenerationAgent"], None)

        initial_context = {"course_name": course_name, "resource_files": []} # No files for now
        
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


@router.post("/build/{course_name}")
async def build_knowledge_graph(course_name: str, background_tasks: BackgroundTasks):
    """
    Triggers the asynchronous pipeline to build a knowledge graph for the specified course.
    """
    import uuid
    task_id = str(uuid.uuid4())
    background_tasks.add_task(run_pipeline_background, course_name, task_id)
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
