from fastapi import FastAPI
from dotenv import load_dotenv

# Import the router from the api module
from src.api.knowledge_graph import router as kg_router

load_dotenv()

app = FastAPI(
    title="LLM-based Knowledge Graph Constructor",
    description="An API to build a knowledge graph from courses using LLMs.",
    version="0.1.0",
)

# Include the router from the api module
app.include_router(kg_router, prefix="/kg", tags=["Knowledge Graph"])

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"Hello": "World"}

# The neo4j_driver initialization is now in src/database/connection.py
# and is imported by the api module.
# The agent functions are also called within the api module.
# The Pydantic models and other imports were moved to the api module.
