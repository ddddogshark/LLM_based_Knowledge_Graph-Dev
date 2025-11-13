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

    class DemandAnalysisAgent(BaseAgent):
        def __init__(self):
            super().__init__("DemandAnalysisAgent", "Analyzes user requirements.")

        async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
            self._log("Starting demand analysis...")
            # Simulate LLM call
            response = self.llm_service.generate_text("Generate a demand analysis for building a KG for Machine Learning course.")
            context["demand_analysis_report"] = response
            self._log("Demand analysis completed.")
            return context

    class SubjectOverviewAgent(BaseAgent):
        def __init__(self):
            super().__init__("SubjectOverviewAgent", "Creates overall subject plan.")

        async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
            self._log("Starting subject overview planning...")
            demand_report = context.get("demand_analysis_report", "No demand report found.")
            # Simulate LLM call
            response = self.llm_service.generate_text(f"Based on this demand: {demand_report[:200]}, create a subject overview plan.")
            context["subject_overview_plan"] = response
            self._log("Subject overview planning completed.")
            return context

    class ValidationCoordinatorAgent(BaseAgent):
        def __init__(self):
            super().__init__("ValidationCoordinatorAgent", "Coordinates validation and quality gates.")

        async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
            self._log("Validation coordinator is active.")
            # This agent might not have a direct 'execute' in every stage,
            # but its methods might be used by gate functions.
            return context

    async def demand_review_gate(context: Dict[str, Any]) -> bool:
        print("\n--- Simulating Demand Review Meeting ---")
        print("Reviewing demand analysis report and subject overview plan...")
        # In a real scenario, this would involve human input or more complex LLM evaluation
        demand_report = context.get("demand_analysis_report", "")
        subject_plan = context.get("subject_overview_plan", "")

        if "Machine Learning" in demand_report and "syllabus" in subject_plan:
            print("Gate: Demand and plan look good. APPROVED.")
            return True
        else:
            print("Gate: Demand or plan missing key elements. REJECTED.")
            return False

    async def main():
        agent_manager = AgentManager()
        agent_manager.register_agent(DemandAnalysisAgent, "DemandAnalysisAgent", "Analyzes user requirements.")
        agent_manager.register_agent(SubjectOverviewAgent, "SubjectOverviewAgent", "Creates overall subject plan.")
        agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.")

        orchestrator = Orchestrator(agent_manager)
        orchestrator.add_stage(
            "Stage1_DemandAnalysisAndPlanning",
            agents=["DemandAnalysisAgent", "SubjectOverviewAgent"],
            gate_function=demand_review_gate,
            description="Analyze user requirements and create an overall subject plan."
        )
        # Add more stages here...

        initial_context = {"course_name": "Machine Learning"}
        final_context = await orchestrator.run_pipeline(initial_context)
        print("\nFinal Context:", final_context)
        print("Pipeline Status:", orchestrator.get_pipeline_status())

    asyncio.run(main())