# src/core/orchestrator.py

from src.core.agent_manager import AgentManager
from src.agents.base_agent import BaseAgent
from src.config import get_logger
from typing import Dict, Any, Callable, List

logger = get_logger(__name__)


class Orchestrator:
    """Orchestrates a multi-stage knowledge graph construction pipeline.

    Stages are executed sequentially. Each stage runs its assigned agents,
    followed by an optional quality gate. If the gate fails, the stage is re-run.
    """

    def __init__(self, agent_manager: AgentManager):
        self.agent_manager = agent_manager
        self.pipeline_stages: Dict[str, Dict[str, Any]] = {}
        self.current_stage = None
        self.context: Dict[str, Any] = {}

    def add_stage(
        self,
        stage_name: str,
        agents: List,
        gate_function: Callable = None,
        description: str = "",
    ):
        """Register a stage in the pipeline.

        Args:
            stage_name: Unique stage identifier.
            agents: List of agent names or (agent_name, method_name) tuples.
            gate_function: Optional async callable(context, agent_manager) -> bool.
            description: Human-readable stage description.
        """
        self.pipeline_stages[stage_name] = {
            "agents": agents,
            "gate_function": gate_function,
            "description": description,
            "status": "PENDING",
        }
        logger.info("Stage '%s' added to pipeline.", stage_name)

    async def run_pipeline(self, initial_context: Dict[str, Any]):
        """Execute all stages sequentially.

        Args:
            initial_context: Shared context dict passed through every stage.

        Returns:
            Final context dict after all stages complete.
        """
        self.context = initial_context
        logger.info("Starting pipeline execution.")

        stage_names = list(self.pipeline_stages.keys())
        i = 0
        while i < len(stage_names):
            stage_name = stage_names[i]
            stage_info = self.pipeline_stages[stage_name]
            self.current_stage = stage_name
            logger.info("--- Entering Stage: %s ---", stage_name)
            stage_info["status"] = "IN_PROGRESS"

            try:
                await self._execute_stage_agents(stage_name)

                if stage_info["gate_function"]:
                    logger.info("Applying quality gate for stage: %s", stage_name)
                    gate_passed = await stage_info["gate_function"](
                        self.context, self.agent_manager
                    )
                    if gate_passed:
                        logger.info("Quality gate '%s' PASSED.", stage_name)
                        stage_info["status"] = "COMPLETED"
                        i += 1
                    else:
                        logger.warning("Quality gate '%s' REJECTED. Re-running.", stage_name)
                        stage_info["status"] = "REJECTED"
                else:
                    logger.debug("No quality gate for stage: %s", stage_name)
                    stage_info["status"] = "COMPLETED"
                    i += 1

            except Exception as e:
                logger.error("Error during stage '%s': %s", stage_name, e, exc_info=True)
                stage_info["status"] = "FAILED"
                break

        logger.info("Pipeline execution finished.")
        return self.context

    async def _execute_stage_agents(self, stage_name: str):
        """Execute all agents assigned to a stage."""
        stage_agents = self.pipeline_stages[stage_name]["agents"]
        for agent_spec in stage_agents:
            if isinstance(agent_spec, tuple):
                agent_name, method_name = agent_spec
            else:
                agent_name, method_name = agent_spec, "execute"

            agent = self.agent_manager.get_agent(agent_name)
            method_to_call = getattr(agent, method_name)

            logger.debug("Executing Agent: %s.%s (%s)", agent.name, method_name, agent.description)
            result = await method_to_call(self.context)

            if isinstance(result, dict):
                self.context = result

            logger.debug("Agent '%s' finished.", agent.name)

    def get_pipeline_status(self):
        """Return a mapping of stage names to their current status."""
        return {name: stage["status"] for name, stage in self.pipeline_stages.items()}

# Example usage (for testing purposes)
if __name__ == "__main__":
    import asyncio
    import json
    from src.config import LLM_API_KEY, LLM_API_URL # Import API credentials
    # Stage 1 Agents
    from src.agents.demand_analysis_agent import DemandAnalysisAgent
    from src.agents.subject_overview_agent import SubjectOverviewAgent
    from src.agents.validation_coordinator_agent import ValidationCoordinatorAgent
    # Stage 2 Agents
    from src.agents.course_agent import CourseAgent
    from src.agents.multimodal_parser_agent import MultimodalParserAgent
    from src.agents.internet_scraper_agent import InternetScraperAgent
    from src.agents.academic_scraper_agent import AcademicScraperAgent
    from src.agents.content_understanding_agent import ContentUnderstandingAgent
    # Stage 3 Agents
    from src.agents.theoretical_analysis_agent import TheoreticalAnalysisAgent
    from src.agents.practical_analysis_agent import PracticalAnalysisAgent
    from src.agents.kg_builder_agent import KgBuilderAgent
    # Stage 5 Agents
    from src.agents.report_generation_agent import ReportGenerationAgent
    # Added back missing imports
    from src.agents.knowledge_generation_agent import KnowledgeGenerationAgent
    from src.agents.knowledge_structuring_agent import KnowledgeStructuringAgent

    async def demand_review_gate(context: Dict[str, Any], agent_manager: AgentManager) -> bool:
        print("\n--- Simulating Demand Review Meeting (Gate 1) ---")
        validation_agent = agent_manager.get_agent("ValidationCoordinatorAgent")
        demand_report = context.get("demand_spec_doc", "")
        subject_plan = context.get("subject_overview_plan", "")
        demand_review_passed = await validation_agent.organize_review("Demand Specification Document Review", demand_report)
        subject_plan_review_passed = await validation_agent.organize_review("Subject Knowledge System Overall Plan Review", subject_plan)
        if demand_review_passed and subject_plan_review_passed:
            print("Gate 1: Demand and plan look good. APPROVED.")
            return True
        print("Gate 1: Demand or plan missing key elements. REJECTED.")
        return False

    async def data_acceptance_gate(context: Dict[str, Any], agent_manager: AgentManager) -> bool:
        print("\n--- Simulating Data Acceptance Meeting (Gate 2) ---")
        validation_agent = agent_manager.get_agent("ValidationCoordinatorAgent")
        drafts = context.get("knowledge_point_drafts", [])
        if not drafts:
            print("Gate 2: No knowledge point drafts were generated. REJECTED.")
            return False
        sample_draft = drafts[0]['explanation']
        review_passed = await validation_agent.organize_review("Knowledge Point Draft Sample Review", sample_draft)
        if review_passed:
            print("Gate 2: Knowledge point drafts seem to be of good quality. APPROVED.")
            return True
        print("Gate 2: Knowledge point drafts failed quality check. REJECTED.")
        return False

    async def subject_level_review_gate(context: Dict[str, Any], agent_manager: AgentManager) -> bool:
        print("\n--- Simulating Subject-Level Review Meeting (Gate 3) ---")
        validation_agent = agent_manager.get_agent("ValidationCoordinatorAgent")
        subgraphs = context.get("subgraphs", {})
        if not subgraphs or not any(subgraphs.values()):
            print("Gate 3: No knowledge triplets were generated for the sub-graph. REJECTED.")
            return False
        
        triplet_count = sum(len(triplets) for triplets in subgraphs.values())
        review_passed = await validation_agent.organize_review("Subject Level Sub-graph Review", subgraphs)
        if triplet_count > 5 and review_passed:
            print(f"Gate 3: Sub-graph with {triplet_count} triplets looks reasonable. APPROVED.")
            return True
        else:
            print(f"Gate 3: Only {triplet_count} triplets were generated or review failed. REJECTED.")
            return False

    async def final_result_review_gate(context: Dict[str, Any], agent_manager: AgentManager) -> bool:
        print("\n--- Simulating Final Result Review Meeting (Gate 4) ---")
        print("Gate 4: Final knowledge graph has passed integration testing. APPROVED for delivery (simulated).")
        return True

    async def main():
        agent_manager = AgentManager()
        
        # Register Agents
        agent_manager.register_agent(DemandAnalysisAgent, "DemandAnalysisAgent", "Analyzes user requirements.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(SubjectOverviewAgent, "SubjectOverviewAgent", "Creates an overall subject plan.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(CourseAgent, "ML_CourseAgent", "Provides resources for the Machine Learning course.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(InternetScraperAgent, "InternetScraperAgent", "Scrapes web pages.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(AcademicScraperAgent, "AcademicScraperAgent", "Scrapes academic papers.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(ContentUnderstandingAgent, "ContentUnderstandingAgent", "Processes raw data into drafts.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(TheoreticalAnalysisAgent, "TheoreticalAnalysisAgent", "Ensures theoretical rigor of knowledge points.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(PracticalAnalysisAgent, "PracticalAnalysisAgent", "Finds practical examples for knowledge points.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(KgBuilderAgent, "KgBuilderAgent", "Builds and integrates knowledge graphs.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(ReportGenerationAgent, "ReportGenerationAgent", "Generates final reports from the knowledge graph.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(KnowledgeGenerationAgent, "KnowledgeGenerationAgent", "Generates detailed knowledge for topics.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
        agent_manager.register_agent(KnowledgeStructuringAgent, "KnowledgeStructuringAgent", "Extracts structured knowledge triplets.", api_key=LLM_API_KEY, api_url=LLM_API_URL)

        orchestrator = Orchestrator(agent_manager)
        
        # Add Stages
        orchestrator.add_stage("Stage1_DemandAnalysisAndPlanning", ["DemandAnalysisAgent", "SubjectOverviewAgent"], demand_review_gate, "Analyze user requirements and create an overall subject plan.")
        orchestrator.add_stage("Stage2_DataCollectionAndPreprocessing", ["MultimodalParserAgent", "ContentUnderstandingAgent"], data_acceptance_gate, "Collect and preprocess data into standardized knowledge point drafts.")
        orchestrator.add_stage("Stage3_KnowledgeRefinementAndCourseConstruction", ["TheoreticalAnalysisAgent", "PracticalAnalysisAgent", "KgBuilderAgent"], subject_level_review_gate, "Refine knowledge points, add practical examples, and build a course sub-graph.")
        orchestrator.add_stage("Stage4_KnowledgeGraphIntegrationAndValidation", [("KgBuilderAgent", "integrate_kps")], final_result_review_gate, "Integrate sub-graphs into a unified knowledge graph and perform validation.")
        orchestrator.add_stage("Stage5_ReportGenerationAndDelivery", ["ReportGenerationAgent"], None, "Generate and deliver the final report.")

        initial_context = {
            "course_name": "DATA SCIENCE",
            "data_path": r"E:\data"
        }
        final_context = await orchestrator.run_pipeline(initial_context)
        
        print("\n--- Final Context ---")
        for key, value in final_context.items():
            if key == "final_report":
                print(f"final_report:\n{value}")
            elif isinstance(value, list) and value:
                print(f"{key}: (list of {len(value)} items)")
            elif isinstance(value, dict) and value:
                 print(f"{key}: (dict with keys: {list(value.keys())})")
            else:
                print(f"{key}: {str(value)[:300]}...")

        print("\n--- Pipeline Status ---")
        print(orchestrator.get_pipeline_status())

    asyncio.run(main())