
from fastapi import FastAPI
from dotenv import load_dotenv

# Import the router from the new API module
from src.api.knowledge_graph import router as kg_router

load_dotenv()

from src.config import LLM_API_KEY # Import LLM_API_KEY for verification

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the Knowledge Graph Builder API"}

# Include the new router with the /kg prefix
app.include_router(kg_router, prefix="/kg")

# The old endpoints below are now obsolete and have been removed.
# The new architecture is handled by the router in src/api/knowledge_graph.py.
