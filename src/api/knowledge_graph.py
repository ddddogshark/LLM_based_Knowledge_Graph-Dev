import os
import requests
from fastapi import APIRouter
from pydantic import BaseModel

from src.agents.planner_agent import plan_course_kg_construction
from src.agents.knowledge_generation_agent import generate_knowledge
from src.agents.knowledge_structuring_agent import extract_triplets
from src.database.connection import neo4j_driver # Import from the new connection file

router = APIRouter()

# Pydantic Models
class TextToTripletsRequest(BaseModel):
    text: str

class Triplet(BaseModel):
    head: str
    relation: str
    tail: str

class StoreTripletsRequest(BaseModel):
    triplets: list[Triplet]

# API Endpoints
@router.get("/test_deepseek")
def test_deepseek():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    api_url = os.getenv("DEEPSEEK_API_URL")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{api_key}",
    }

    data = {
        "model": "Qwen",
        "messages": [{"role": "user", "content": "This is a test."}],
        "temperature": 0.7,
    }

    response = requests.post(api_url, headers=headers, json=data)

    return response.json()

@router.get("/plan_kg/{course_name}")
def get_kg_plan(course_name: str):
    plan = plan_course_kg_construction(course_name)
    return {"course_name": course_name, "plan": plan}

@router.get("/generate_knowledge/{topic}")
def get_generated_knowledge(topic: str):
    knowledge = generate_knowledge(topic)
    return {"topic": topic, "knowledge": knowledge}

@router.post("/extract_triplets")
def get_extracted_triplets(request: TextToTripletsRequest):
    triplets = extract_triplets(request.text)
    return {"text": request.text, "triplets": triplets}

@router.post("/store_triplets")
def store_extracted_triplets(request: StoreTripletsRequest):
    if not neo4j_driver:
        return {"message": "Neo4j driver not initialized.", "status": "error"}
    try:
        triplets_dicts = [t.dict() for t in request.triplets]
        neo4j_driver.store_triplets(triplets_dicts)
        return {"message": f"Successfully stored {len(request.triplets)} triplets.", "status": "success"}
    except Exception as e:
        return {"message": f"Failed to store triplets: {e}", "status": "error"}
