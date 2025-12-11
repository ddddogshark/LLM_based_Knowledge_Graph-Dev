# LLM-based Knowledge Graph Constructor

This project is a FastAPI-based application that uses Large Language Models (LLMs) to automatically construct a knowledge graph from high-level topics, such as a course name.

## Features

- **Dynamic Planning:** Uses an LLM to generate a curriculum/plan for any given topic.
- **Knowledge Generation:** Uses an LLM to generate detailed text for each topic in the plan.
- **Knowledge Structuring:** Extracts structured knowledge triplets (head, relation, tail) from the generated text.
- **Graph Storage:** Stores the extracted triplets in a Neo4j graph database.
- **API Driven:** Exposes the entire workflow through a clean and simple REST API.

## Architecture Overview

The application follows a modular, multi-agent pipeline orchestrated by a central `Orchestrator`. This design allows for flexible and extensible knowledge graph construction, primarily focusing on processing knowledge from local files.

### Core Components

1.  **FastAPI Server (`src/main.py`)**: The entry point for the application, providing RESTful API endpoints to trigger and interact with the knowledge graph construction process.
2.  **Orchestrator (`src/core/orchestrator.py`)**: Manages and executes the entire pipeline, maintaining the stages, agents, and shared data (`Context`).
3.  **AgentManager (`src/core/agent_manager.py`)**: Responsible for registering, initializing, and retrieving various agents.
4.  **BaseAgent (`src/agents/base_agent.py`)**: An abstract base class defining the common interface and functionalities for all agents.
5.  **Specialized Agents (`src/agents/`)**: Each agent handles a specific task within the pipeline. Key agents include:
    *   `MultimodalParserAgent`: The core data ingestion agent. It reads Markdown and image files from specified local directories by traversing them hierarchically. For each course found, it aggregates all its content into a single, course-specific Markdown file (e.g., `CourseName.md`) for review. The parsed content and image paths are then stored in the shared context for downstream agents.
    *   `ContentUnderstandingAgent`: Processes text content from various sources, segments it, and extracts knowledge point drafts using an LLM.
    *   `KgBuilderAgent`: Extracts knowledge triplets from refined knowledge points and integrates them into the Neo4j database.
    *   Other agents like `DemandAnalysisAgent`, `TheoreticalAnalysisAgent`, `PracticalAnalysisAgent`, and `ReportGenerationAgent` handle specific steps in the knowledge refinement and reporting process.
6.  **Services (`src/services/`)**: Provide common services, such as interaction with Large Language Models (LLMs).
7.  **Database Drivers (`src/database/`)**: Offer connectivity and operations for databases (e.g., Neo4j).

### Pipeline Stages

The entire process is divided into five distinct stages:

1.  **Demand Analysis and Planning**: `DemandAnalysisAgent` creates a structured requirement document.
2.  **Data Collection and Preprocessing**: `MultimodalParserAgent` reads local Markdown and image files, while `ContentUnderstandingAgent` processes the text to extract knowledge point drafts.
3.  **Knowledge Refinement and Course Construction**: `TheoreticalAnalysisAgent` and `PracticalAnalysisAgent` refine knowledge points, and `KgBuilderAgent` extracts knowledge triplets.
4.  **Knowledge Graph Integration and Validation**: `KgBuilderAgent` integrates extracted triplets into the Neo4j database.
5.  **Report Generation and Delivery**: `ReportGenerationAgent` generates a summary report based on the final knowledge graph.

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

## Usage

1.  **Run the FastAPI server:**
    ```bash
    uvicorn src.main:app --reload
    ```
    The API will be available at `http://127.00.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

2.  **API Endpoints:**
    All knowledge graph endpoints are prefixed with `/kg`.

    -   **`POST /kg/build`**: Triggers the asynchronous pipeline to construct a knowledge graph for a given course. This endpoint now supports an optional `data_path` parameter in the request body to specify local directories containing Markdown and image files.
        -   **Method**: `POST`
        -   **URL**: `http://127.0.0.1:8000/kg/build`
        -   **Request Body (JSON)**:
            ```json
            {
                "course_name": "Data Science",
                "data_path": "E:/data" // Optional: path to local files
            }
            ```
        -   **Example (using curl)**:
            ```bash
            curl -X POST "http://127.0.0.1:8000/kg/build" -H "Content-Type: application/json" -d "{
                \"course_name\": \"Data Science\",
                \"data_path\": \"E:/data\"
            }"
            ```
            Or, if you only want to generate content online via LLM (without local files):
            ```bash
            curl -X POST "http://127.0.0.1:8000/kg/build" -H "Content-Type: application/json" -d "{
                \"course_name\": \"Data Science\"
            }"
            ```

    -   **`GET /kg/build/status/{task_id}`**: Retrieves the status of a knowledge graph construction task.
        -   **Example**: `http://127.0.0.1:8000/kg/build/status/your-task-id`

    -   **Older Endpoints (not part of the main pipeline flow):**
        -   `GET /kg/plan_kg/{course_name}`: Generates a learning plan for a course.
        -   `GET /kg/generate_knowledge/{topic}`: Generates knowledge text for a topic.
        -   `POST /kg/extract_triplets`: Extracts triplets from a block of text.
        -   `POST /kg/store_triplets`: Stores a list of triplets in the database.

## Running Tests

To run the unit tests, execute the following command from the project root:

```bash
pytest
```
