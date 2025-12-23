import asyncio
import os
from dotenv import load_dotenv
from src.agents.content_understanding_agent import ContentUnderstandingAgent
from src.agents.kg_builder_agent import KgBuilderAgent
from src.database.neo4j_driver import Neo4jDriver
from src.services.llm_service import generate_text_async
from typing import Dict, Any, List
import json

# Load environment variables
load_dotenv()

# --- Configuration (for demonstration purposes, replace with actual values in .env) ---
# It's assumed LLM_API_KEY, LLM_API_URL, LLM_MODEL are set in .env or src/config.py

# --- Helper function to simulate MultimodalParserAgent's output ---
def get_multimodal_parsed_content(slides_content: str) -> List[str]:
    # For this demonstration, we'll treat the entire slides content as one chunk.
    # In a real scenario, MultimodalParserAgent would intelligently split this.
    return [slides_content]

async def run_pipeline():
    print("Starting knowledge graph generation pipeline for the full content...")

    # --- 1. Load data (simulating MultimodalParserAgent) ---
    slides_file_path = "Slides.md"
    try:
        with open(slides_file_path, "r", encoding="utf-8") as f:
            slides_content = f.read() # Read the full content
    except FileNotFoundError:
        print(f"Error: {slides_file_path} not found. Please ensure the file exists.")
        return

    initial_context: Dict[str, Any] = {
        "course_name": "Introduction to High-Performance and Parallel Computing",
        "multimodal_parsed_content": get_multimodal_parsed_content(slides_content),
        "internet_scraped_content": "", # Not used in this specific run
        "academic_scraped_content": ""  # Not used in this specific run
    }
    print(f"Loaded content for course: {initial_context['course_name']}")

    # --- 2. Run ContentUnderstandingAgent (Stage 2 part) ---
    content_agent = ContentUnderstandingAgent(
        name="ContentUnderstandingAgent",
        description="Extracts knowledge points using EDC."
    )
    print("Running ContentUnderstandingAgent...")
    context_after_content_understanding = await content_agent.execute(initial_context.copy())
    
    knowledge_point_drafts = context_after_content_understanding.get("knowledge_point_drafts", [])
    if not knowledge_point_drafts:
        print("ContentUnderstandingAgent did not generate any knowledge point drafts. Exiting.")
        return

    print(f"ContentUnderstandingAgent generated {len(knowledge_point_drafts)} knowledge point drafts.")

    # --- 3. Run KgBuilderAgent (Stage 3 & 4) ---
    kg_builder_agent = KgBuilderAgent(
        name="KgBuilderAgent",
        description="Extracts and integrates triplets into Neo4j."
    )
    print("Running KgBuilderAgent for triplet extraction and Neo4j integration...")

    # Simulate the context expected by KgBuilderAgent's execute method for triplet extraction
    # The KgBuilderAgent typically takes knowledge_point_drafts from the context
    triplet_extraction_context = {
        "practically_enhanced_knowledge_points": knowledge_point_drafts, # Correct key for KgBuilderAgent
        "course_name": initial_context["course_name"]
    }

    # Execute KgBuilderAgent for triplet extraction
    context_after_triplet_extraction = await kg_builder_agent.execute(triplet_extraction_context.copy())
    
    subgraphs = context_after_triplet_extraction.get("subgraphs", {})
    extracted_triplets = subgraphs.get(initial_context["course_name"], [])

    if not extracted_triplets:
        print("KgBuilderAgent did not extract any triplets. Exiting.")
        return

    print(f"KgBuilderAgent extracted {len(extracted_triplets)} triplets.")

    # Integrate into Neo4j (KgBuilderAgent's integrate_kps method)
    # The integrate_kps method is typically called after triplets are extracted.
    # It directly uses self.neo4j_driver to store.
    # We need a way to pass the extracted_triplets to it, or mock the Orchestrator behavior.
    # For this direct run, we'll manually call store_triplets.
    
    # Initialize Neo4j Driver (already done in KgBuilderAgent constructor, but we ensure connectivity)
    neo4j_driver = Neo4jDriver()
    try:
        neo4j_driver.store_triplets(extracted_triplets)
        print("Triplets successfully stored in Neo4j.")
    except Exception as e:
        print(f"Error storing triplets in Neo4j: {e}")
    finally:
        neo4j_driver.close()

    print("\nPipeline execution complete.")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
