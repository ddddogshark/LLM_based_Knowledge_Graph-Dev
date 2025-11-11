# 基于LLM的知识图谱构建器

本项目是一个基于 FastAPI 的应用程序，使用大型语言模型（LLM）从高级主题（如课程名称）自动构建知识图谱。

## 功能特性

- **动态规划:** 使用 LLM 为任何给定主题生成课程大纲或计划。
- **知识生成:** 使用 LLM 为计划中的每个主题生成详细的文本。
- **知识结构化:** 从生成的文本中提取结构化的知识三元组（头实体、关系、尾实体）。
- **图谱存储:** 将提取的三元组存储在 Neo4j 图数据库中。
- **API驱动:** 通过简洁的 REST API 暴露整个工作流程。

## 架构概览

该应用程序遵循一个简单的、多代理的流水线：

1.  **计划器代理 (Planner Agent):** 接收一个高级主题（例如课程名称）并生成结构化的计划或大纲。
2.  **生成器代理 (Generation Agent):** 获取计划中的每个项目，并生成关于它的详细非结构化文本。
3.  **结构化代理 (Structuring Agent):** 处理非结构化文本，以提取结构化的知识三元组列表。
4.  **数据库驱动 (Database Driver):** 将这些三元组存储在 Neo4j 数据库中，形成知识图谱。

整个过程通过 FastAPI 服务器进行暴露。

## 安装与设置

1.  **克隆仓库:**
    ```bash
    git clone <your-repository-url>
    cd LLM_based_Knowledge_Graph
    ```

2.  **创建并激活虚拟环境:**
    ```bash
    python -m venv venv
    # Windows 系统
    venv\Scripts\activate
    # macOS/Linux 系统
    source venv/bin/activate
    ```

3.  **安装依赖:**
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

4.  **设置环境变量:**
    在项目根目录中创建一个名为 `.env` 的文件，并添加以下变量。此文件已被 Git 忽略。

    ```env
    # DeepSeek LLM API 凭证
    DEEPSEEK_API_KEY="your_deepseek_api_key"
    DEEPSEEK_API_URL="https://api.deepseek.com/v1/chat/completions"

    # Neo4j 数据库凭证
    NEO4J_URI="bolt://localhost:7687"
    NEO4J_USER="neo4j"
    NEO4J_PASSWORD="your_neo4j_password"
    ```

## 如何使用

1.  **运行 FastAPI 服务器:**
    ```bash
    uvicorn src.main:app --reload
    ```
    API 将在 `http://127.0.0.1:8000` 上可用。您可以通过 `http://127.0.0.1:8000/docs` 访问交互式API文档（Swagger UI）。

2.  **API 端点:**
    所有知识图谱相关的端点都以 `/kg` 为前缀。

    - **`GET /kg/plan_kg/{course_name}`**: 为课程生成学习计划。
      - 示例: `http://127.0.0.1:8000/kg/plan_kg/DSAA2011%20Machine%20Learning`

    - **`GET /kg/generate_knowledge/{topic}`**: 为主题生成知识文本。
      - 示例: `http://127.0.0.1:8000/kg/generate_knowledge/Supervised%20Learning`

    - **`POST /kg/extract_triplets`**: 从文本块中提取三元组。
      - 请求体: `{"text": "Your text here..."}`

    - **`POST /kg/store_triplets`**: 在数据库中存储三元组列表。
      - 请求体: `{"triplets": [{"head": "A", "relation": "is", "tail": "B"}]}`

## 运行测试

要运行单元测试，请在项目根目录中执行以下命令：

```bash
pytest
```
