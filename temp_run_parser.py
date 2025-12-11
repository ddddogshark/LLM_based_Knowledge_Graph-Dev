# temp_run_parser.py
import asyncio
from src.core.agent_manager import AgentManager
from src.core.orchestrator import Orchestrator
from src.config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL
# Agent to run
from src.agents.multimodal_parser_agent import MultimodalParserAgent
from typing import Dict, Any

async def main():
    agent_manager = AgentManager()
    
    # Register Agent for the task
    agent_manager.register_agent(MultimodalParserAgent, "MultimodalParserAgent", "Parses various file formats.", api_key=DEEPSEEK_API_KEY, api_url=DEEPSEEK_API_URL)

    orchestrator = Orchestrator(agent_manager)
    
    # Add a temporary stage that only runs the MultimodalParserAgent
    orchestrator.add_stage("Stage_RunParser", ["MultimodalParserAgent"], None, "Parse local multimodal data.")

    # The data path needs to use double backslashes for escaping in a Python string
    data_path = "C:\\1DevProject\\LLM_based_Knowledge_Graph\\data"
    
    initial_context = {
        "course_name": "Local Data Processing", # This name is for context, agent will process all folders in data_path
        "data_path": data_path
    }
    
    print(f"--- Starting parser for data_path: {data_path} ---")
    
    final_context = await orchestrator.run_pipeline(initial_context)
    
    print("\n--- Final Context ---")
    for key, value in final_context.items():
        if key == "multimodal_parsed_content":
             print(f"{key}: (list of {len(value)} items)")
        elif key == "image_paths":
             print(f"{key}: (list of {len(value)} items)")
        else:
            print(f"{key}: {str(value)[:300]}...")

    print("\n--- Pipeline Status ---")
    print(orchestrator.get_pipeline_status())
    
    print("\n--- Parser execution finished. Check the root directory for generated .md files. ---")

asyncio.run(main())