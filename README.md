# LLM-based Knowledge Graph Constructor

This project is a FastAPI-based application that uses Large Language Models (LLMs) to automatically construct a knowledge graph from high-level topics, such as a course name.

## Features

- **Dynamic Planning:** Uses an LLM to generate a curriculum/plan for any given topic.
- **Knowledge Generation:** Uses an LLM to generate detailed text for each topic in the plan.
- **Knowledge Structuring:** Extracts structured knowledge triplets (head, relation, tail) from the generated text.
- **Graph Storage:** Stores the extracted triplets in a Neo4j graph database.
- **API Driven:** Exposes the entire workflow through a clean and simple REST API.

## Architecture Overview

The application follows a simple, multi-agent pipeline:

1.  **Planner Agent:** Receives a high-level topic (e.g., a course name) and generates a structured plan or outline.
2.  **Generation Agent:** Takes each item from the plan and generates detailed, unstructured text about it.
3.  **Structuring Agent:** Processes the unstructured text to extract a list of structured knowledge triplets.
4.  **Database Driver:** Stores these triplets in a Neo4j database, forming the knowledge graph.

This entire process is exposed via a FastAPI server.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd LLM_based_Knowledge_Graph
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the project root and add the following variables. This file is ignored by Git.

    ```env
    # DeepSeek LLM API Credentials
    DEEPSEEK_API_KEY="your_deepseek_api_key"
    DEEPSEEK_API_URL="https://api.deepseek.com/v1/chat/completions"

    # Neo4j Database Credentials
    NEO4J_URI="bolt://localhost:7687"
    NEO4J_USER="neo4j"
    NEO4J_PASSWORD="your_neo4j_password"
    ```

## Usage

1.  **Run the FastAPI server:**
    ```bash
    uvicorn src.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

2.  **API Endpoints:**
    All knowledge graph endpoints are prefixed with `/kg`.

    - **`GET /kg/plan_kg/{course_name}`**: Generates a learning plan for a course.
      - Example: `http://127.0.0.1:8000/kg/plan_kg/DSAA2011%20Machine%20Learning`

    - **`GET /kg/generate_knowledge/{topic}`**: Generates knowledge text for a topic.
      - Example: `http://127.0.0.1:8000/kg/generate_knowledge/Supervised%20Learning`

    - **`POST /kg/extract_triplets`**: Extracts triplets from a block of text.
      - Body: `{"text": "Your text here..."}`

    - **`POST /kg/store_triplets`**: Stores a list of triplets in the database.
      - Body: `{"triplets": [{"head": "A", "relation": "is", "tail": "B"}]}`

## Running Tests

To run the unit tests, execute the following command from the project root:

```bash
pytest
```
