# temp_run_multimodal_parser.py
import asyncio
import json
from src.core.agent_manager import AgentManager
from src.core.orchestrator import Orchestrator
from src.config import LLM_API_KEY, LLM_API_URL
# Stage 2 Agents
from src.agents.multimodal_parser_agent import MultimodalParserAgent
from src.agents.content_understanding_agent import ContentUnderstandingAgent
from src.agents.validation_coordinator_agent import ValidationCoordinatorAgent # For the gate function
from typing import Dict, Any

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

async def main():
    agent_manager = AgentManager()
    
    # Register Agents for Stage 2
    agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
    agent_manager.register_agent(ContentUnderstandingAgent, "ContentUnderstandingAgent", "Processes raw data into drafts.", api_key=LLM_API_KEY, api_url=LLM_API_URL)
    agent_manager.register_agent(ValidationCoordinatorAgent, "ValidationCoordinatorAgent", "Coordinates validation and quality gates.", api_key=LLM_API_KEY, api_url=LLM_API_URL)

    orchestrator = Orchestrator(agent_manager)
    
    # Add Stage 2
    orchestrator.add_stage("Stage2_DataCollectionAndPreprocessing", ["MultimodalParserAgent", "ContentUnderstandingAgent"], data_acceptance_gate, "Collect and preprocess data into standardized knowledge point drafts.")

    initial_context = {
        "course_name": "All Courses",
        "data_path": "C:\\1DevProject\\LLM_based_Knowledge_Graph\\data"
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
