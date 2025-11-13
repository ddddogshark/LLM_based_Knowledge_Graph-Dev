# src/core/orchestrator.py

from src.core.agent_manager import AgentManager
from src.agents.base_agent import BaseAgent
from typing import Dict, Any, Callable, List

class Orchestrator:
    def __init__(self, agent_manager: AgentManager):
        self.agent_manager = agent_manager
        self.pipeline_stages: Dict[str, Dict[str, Any]] = {}
        self.current_stage = None
        self.context: Dict[str, Any] = {} # Shared context for the pipeline

    def add_stage(self, stage_name: str, agents: List[str], gate_function: Callable = None, description: str = ""):
        """
        Adds a stage to the pipeline.
        :param stage_name: Unique name for the stage.
        :param agents: List of agent names involved in this stage.
        :param gate_function: A callable that acts as a quality gate. It should return True for approval, False for rejection.
        :param description: Description of the stage.
        """
        self.pipeline_stages[stage_name] = {
            "agents": agents,
            "gate_function": gate_function,
            "description": description,
            "status": "PENDING" # PENDING, IN_PROGRESS, COMPLETED, FAILED, REJECTED
        }
        print(f"Stage '{stage_name}' added to the pipeline.")

    async def run_pipeline(self, initial_context: Dict[str, Any]):
        """
        Executes the defined pipeline stages sequentially.
        """
        self.context = initial_context
        print("Starting pipeline execution...")

        stage_names = list(self.pipeline_stages.keys())
        i = 0
        while i < len(stage_names):
            stage_name = stage_names[i]
            stage_info = self.pipeline_stages[stage_name]
            self.current_stage = stage_name
            print(f"\n--- Entering Stage: {stage_name} ---")
            print(f"Description: {stage_info['description']}")
            stage_info['status'] = "IN_PROGRESS"

            try:
                # Execute agents for the current stage
                await self._execute_stage_agents(stage_name)

                # Apply quality gate if defined
                if stage_info["gate_function"]:
                    print(f"--- Applying Quality Gate for Stage: {stage_name} ---")
                    gate_passed = await stage_info["gate_function"](self.context)
                    if gate_passed:
                        print(f"Quality Gate for '{stage_name}' PASSED.")
                        stage_info['status'] = "COMPLETED"
                        i += 1 # Move to next stage
                    else:
                        print(f"Quality Gate for '{stage_name}' REJECTED. Re-running stage.")
                        stage_info['status'] = "REJECTED"
                        # If rejected, re-run the current stage. No change to 'i'.
                else:
                    print(f"No Quality Gate for Stage: {stage_name}. Proceeding to next stage.")
                    stage_info['status'] = "COMPLETED"
                    i += 1 # Move to next stage

            except Exception as e:
                print(f"Error during stage '{stage_name}': {e}")
                stage_info['status'] = "FAILED"
                break # Stop pipeline on error

        print("\n--- Pipeline Execution Finished ---")
        return self.context

    async def _execute_stage_agents(self, stage_name: str):
        """
        Executes all agents assigned to a specific stage.
        Agents are expected to update the shared context.
        """
        stage_agents = self.pipeline_stages[stage_name]["agents"]
        for agent_name in stage_agents:
            agent = self.agent_manager.get_agent(agent_name)
            print(f"  Executing Agent: {agent.name} ({agent.description})")
            # Agents should update self.context directly or return updates
            # For simplicity, agents will receive and return context for now.
            # A more sophisticated approach might involve message queues or shared memory.
            self.context = await agent.execute(self.context)
            print(f"  Agent '{agent.name}' finished.")

    def get_pipeline_status(self):
        return {name: stage['status'] for name, stage in self.pipeline_stages.items()}

# Example usage (for testing purposes)
if __name__ == "__main__":
    import asyncio
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

    async def demand_review_gate(context: Dict[str, Any]) -> bool:
        print("\n--- Simulating Demand Review Meeting (Gate 1) ---")
        validation_agent = ValidationCoordinatorAgent()
        demand_report = context.get("demand_spec_doc", "")
        subject_plan = context.get("subject_overview_plan", "")
        demand_review_passed = await validation_agent.review_document("Demand Specification Document", demand_report, "Ensure the document clearly defines project goals, scope, and success metrics.")
        subject_plan_review_passed = await validation_agent.review_document("Subject Knowledge System Overall Plan", subject_plan, "Ensure the plan includes core course list, logical relationships, and task breakdown.")
        if demand_review_passed and subject_plan_review_passed:
            print("Gate 1: Demand and plan look good. APPROVED.")
            return True
        print("Gate 1: Demand or plan missing key elements. REJECTED.")
        return False

    async def data_acceptance_gate(context: Dict[str, Any]) -> bool:
        print("\n--- Simulating Data Acceptance Meeting (Gate 2) ---")
        validation_agent = ValidationCoordinatorAgent()
        drafts = context.get("knowledge_point_drafts", [])
        if not drafts:
            print("Gate 2: No knowledge point drafts were generated. REJECTED.")
            return False
        sample_draft = drafts[0]['draft']
        review_passed = await validation_agent.review_document("Knowledge Point Draft Sample", sample_draft, "Ensure the draft is a concise summary of key information.")
        if review_passed:
            print("Gate 2: Knowledge point drafts seem to be of good quality. APPROVED.")
            return True
        print("Gate 2: Knowledge point drafts failed quality check. REJECTED.")
        return False

    async def subject_level_review_gate(context: Dict[str, Any]) -> bool:
        print("\n--- Simulating Subject-Level Review Meeting (Gate 3) ---")
        validation_agent = ValidationCoordinatorAgent()
        triplets = context.get("knowledge_subgraph_triplets", [])
        if not triplets:
            print("Gate 3: No knowledge triplets were generated for the sub-graph. REJECTED.")
            return False
        
        # For simplicity, we'll just check if a reasonable number of triplets were generated.
        # A real gate would involve much more complex validation, e.g., checking for graph connectivity,
        # looking for cross-course conflicts, or identifying knowledge gaps.
        if len(triplets) > 5:
            print(f"Gate 3: Sub-graph with {len(triplets)} triplets looks reasonable. APPROVED.")
            return True
        else:
            print(f"Gate 3: Only {len(triplets)} triplets were generated. This seems too low. REJECTED.")
            return False

    async def main():
        agent_manager = AgentManager()
        
        # Register Stage 1 Agents
        agent_manager.register_agent(DemandAnalysisAgent, "DemandAnalysisAgent", "Analyzes user requirements.")
        agent_manager.register_agent(SubjectOverviewAgent, "SubjectOverviewAgent", "Creates an overall subject plan.")
        agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.")

        # Register Stage 2 Agents
        agent_manager.register_agent(lambda name, desc: CourseAgent(name, desc, "Machine Learning"), "ML_CourseAgent", "Provides resources for the Machine Learning course.")
        agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.")
        agent_manager.register_agent(InternetScraperAgent, "InternetScraperAgent", "Scrapes web pages.")
        agent_manager.register_agent(AcademicScraperAgent, "AcademicScraperAgent", "Scrapes academic papers.")
        agent_manager.register_agent(ContentUnderstandingAgent, "ContentUnderstandingAgent", "Processes raw data into drafts.")

        # Register Stage 3 Agents
        agent_manager.register_agent(TheoreticalAnalysisAgent, "TheoreticalAnalysisAgent", "Ensures theoretical rigor of knowledge points.")
        agent_manager.register_agent(PracticalAnalysisAgent, "PracticalAnalysisAgent", "Finds practical examples for knowledge points.")
        agent_manager.register_agent(KgBuilderAgent, "KgBuilderAgent", "Builds knowledge sub-graphs by extracting triplets.")

        orchestrator = Orchestrator(agent_manager)
        
        # Add Stage 1
        orchestrator.add_stage("Stage1_DemandAnalysisAndPlanning", ["DemandAnalysisAgent", "SubjectOverviewAgent"], demand_review_gate, "Analyze user requirements and create an overall subject plan.")
        
        # Add Stage 2
        orchestrator.add_stage("Stage2_DataCollectionAndPreprocessing", ["ML_CourseAgent", "MultimodalParserAgent", "InternetScraperAgent", "AcademicScraperAgent", "ContentUnderstandingAgent"], data_acceptance_gate, "Collect and preprocess data into standardized knowledge point drafts.")

        # Add Stage 3
        orchestrator.add_stage("Stage3_KnowledgeRefinementAndCourseConstruction", ["TheoreticalAnalysisAgent", "PracticalAnalysisAgent", "KgBuilderAgent"], subject_level_review_gate, "Refine knowledge points, add practical examples, and build a course sub-graph.")

        initial_context = {"course_name": "Machine Learning", "resource_files": ["lecture1.pptx", "book_chapter.pdf"]}
        final_context = await orchestrator.run_pipeline(initial_context)
        
        print("\n--- Final Context ---")
        for key, value in final_context.items():
            if isinstance(value, list) and value:
                print(f"{key}: (list of {len(value)} items)")
            elif isinstance(value, dict) and value:
                 print(f"{key}: (dict with keys: {list(value.keys())})")
            else:
                print(f"{key}: {str(value)[:300]}...")

        print("\n--- Pipeline Status ---")
        print(orchestrator.get_pipeline_status())

    asyncio.run(main())