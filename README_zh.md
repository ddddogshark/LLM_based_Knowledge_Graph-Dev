# 基于LLM的知识图谱构建器

本项目是一个基于FastAPI的应用，使用大型语言模型（LLM）从高级主题（如课程名称）自动构建知识图谱。

## 设计逻辑

### 架构概览

本应用采用一个多智能体（Multi-Agent）的流水线（Pipeline）架构。整个流程由一个总指挥（Orchestrator）来协调，该总指挥按顺序执行定义好的各个阶段。每个阶段包含一个或多个智能体，这些智能体负责执行特定的任务。数据在智能体之间通过一个共享的“上下文”（Context）对象进行传递。

这种设计的优势在于其模块化和可扩展性。每个智能体都是一个独立的单元，可以被替换、修改或重新排序，而不会影响到其他智能体。这种设计也使得添加新的功能阶段变得简单。

### 核心组件

1.  **FastAPI服务器 (`src/main.py`)**: 作为应用的入口，提供RESTful API接口，用于触发知识图谱的构建流程并与之交互。
2.  **总指挥 Orchestrator (`src/core/orchestrator.py`)**: 负责管理和执行整个流水线。它维护着流水线的各个阶段、智能体以及它们之间的共享数据。
3.  **智能体管理器 AgentManager (`src/core/agent_manager.py`)**: 负责注册、初始化和检索各个智能体。
4.  **基础智能体 BaseAgent (`src/agents/base_agent.py`)**: 一个抽象基类，定义了所有智能体的通用接口和功能，例如日志记录和数据库连接。
5.  **具体智能体 Agents (`src/agents/`)**: 各个具体的智能体，每个都负责一个特定的任务，例如：
    *   `DemandAnalysisAgent`: 需求分析
    *   `MultimodalParserAgent`: 本地文件解析器，是数据处理流程的核心入口。它负责从本地文件系统（例如 `E:\data`）的特定目录结构中，分层次地读取课程、讲座相关的Markdown（`.md`）文件和图片文件。该智能体提取内容、记录图片路径，并将每个讲座的信息组织成结构化对象，最终为每个课程生成一个聚合的Markdown文件（例如 `课程名.md`），并将解析出的内容存入共享上下文供下游智能体使用。
    *   `ContentUnderstandingAgent`: 理解从本地文件读取的内容，提取知识点草稿。
    *   `KgBuilderAgent`: 从知识点中提取三元组，并将其集成到Neo4j知识图谱中。
    *   `TheoreticalAnalysisAgent` & `PracticalAnalysisAgent`: 对知识点进行理论和实践上的精炼。
    *   `ReportGenerationAgent`: 生成最终的总结报告。
6.  **服务 Services (`src/services/`)**: 提供通用的服务，例如与LLM的交互。
7.  **数据库驱动 Drivers (`src/database/`)**: 提供与数据库（Neo4j, MySQL, Redis）的连接和操作。

### 流水线阶段概览

整个流程被划分为五个阶段：

1.  **需求分析与规划**: `DemandAnalysisAgent` 创建结构化的需求文档。
2.  **数据收集与预处理**: `MultimodalParserAgent` 解析本地文件，`ContentUnderstandingAgent` 处理文本并提取知识点草稿。
3.  **知识精炼与课程构建**: `TheoreticalAnalysisAgent` 和 `PracticalAnalysisAgent` 精炼知识点，`KgBuilderAgent` 提取知识三元组。
4.  **知识图谱集成与验证**: `KgBuilderAgent` 将提取的三元组集成到 Neo4j 数据库。
5.  **报告生成与交付**: `ReportGenerationAgent` 生成基于知识图谱的总结报告。

## 各阶段算法逻辑



整个流水线被划分为五个阶段，核心逻辑是 **基于本地文件内容** 进行知识图谱的构建。



### 阶段一：需求分析与规划 (Stage 1: Demand Analysis and Planning)







1.  **`DemandAnalysisAgent`**:



    *   **逻辑**: 此智能体接收一个高层次的主题（例如课程名称），并利用LLM生成一份结构化的需求规格文档，为整个知识图谱的构建确立目标和范围。



    *   **算法**:



        1.  构建一个Prompt，要求LLM为给定的主题生成一份详细的需求文档。



        2.  调用LLM服务，获取生成的Markdown格式的需求文档。



        3.  将生成的需求文档存入共享的上下文中。







### 阶段二：数据收集与预处理 (Stage 2: Data Collection and Preprocessing)



1.  **`MultimodalParserAgent`**:



    *   **逻辑**: 这是数据处理流程的 **核心入口**。此智能体负责从本地文件系统（例如 `C:\1DevProject\LLM_based_Knowledge_Graph\data`）的特定目录结构中，分层次地读取课程、讲座相关的Markdown（`.md`）文件和图片文件。



    *   **算法**:



        1.  从上下文中获取 `data_path`。



        2.  **分层遍历**: 遍历 `data_path` 下的每个文件夹，假定一级文件夹为 **课程名称**（如 `DSAA2011XXXX`），二级文件夹为 **讲座/页面名称**（如 `DSAA2011-L01_intro-L02_page_001`）。



        3.  **内容提取**: 在每个讲座/页面文件夹中：



            -   查找并读取 `.md` 文件的内容。



            -   查找所有图片文件（`.png`, `.jpg` 等）并记录它们的完整路径。



        4.  **结构化数据**: 将每个讲座的信息（包括课程名、讲座名、Markdown内容、图片路径列表）组织成一个结构化的对象。



        5.  **生成课程Markdown文件**: 对于每个成功解析的课程，将该课程下所有讲座的Markdown内容和图片路径聚合成一个单独的Markdown文件。该文件以课程名称命名（例如 `课程名.md`），并保存在项目的根目录下（例如 `Slides.md`）。这为每个课程提供了一个完整的、可供查阅的文本和图片资源概览。
            -   **独立运行示例**: 您可以通过执行 `python temp_run_multimodal_parser.py` 来独立运行此代理及其后续的内容理解步骤。




        6.  将原始的Markdown内容列表和结构化的图片路径信息分别存入共享上下文的 `multimodal_parsed_content` 和 `image_paths` 键中，供下游智能体使用。



2.  **`ContentUnderstandingAgent`**:



    *   **逻辑**: 对从本地文件中读取到的所有文本内容进行整合和智能切分，然后利用EDC的方法从这些文本块中提取结构化的“知识点草稿”，确保在处理长文本时信息的完整性。具体的EDC算法专注于**“后处理”的质量优化和可扩展性**。它通过开放信息提取（OIE）来绕过上下文窗口对模式大小的限制，然后用定义和规范化来解决开放提取固有的冗余和不一致问题。该方法通过LLM生成的定义和语义相似性验证，将模糊、冗余的关系统一为规范关系，在消除语义歧义的同时，生成一个更简洁、更具可读性的知识图谱模式。这种方法灵活性高，适用于有或无目标模式的场景。



    *   **算法**: 采用EDC（Extract-Define-Canonicalize）三阶段方法，将非结构化文本转化为结构化的知识点草稿。

        1.  **步骤1：开放信息提取 (Open Information Extraction, OIE)**
            -   **文本整合与切分**: 从上下文中获取所有文本内容，合并后使用递归文本切分函数 (`src/utils/text_splitter.py`) 将其切分成合适的文本块。
            -   **自由三元组提取**: 并行地将文本块发送给LLM，利用少样本提示（few-shot prompting）自由地提取所有可能的知识三元组 `[主语, 关系, 宾语]`。此阶段不限制关系的格式，因此提取结果可能存在冗余和不一致（例如，'profession', 'job', 'occupation' 可能被视为不同的关系）。

        2.  **步骤2：模式定义 (Schema Definition)**
            -   **收集独特关系**: 从所有提取的三元组中收集所有唯一的关系名称。
            -   **生成关系定义**: 要求LLM为每个唯一的关系生成一个精确的自然语言定义。例如，为关系 'participatedIn' 生成定义：“主体实体参与了对象实体指定的事件或任务”。

        3.  **步骤3：模式规范化 (Schema Canonicalization)**
            -   **语义向量化**: 将每个关系的自然语言定义转换为向量嵌入。
            -   **聚类与规范化**: 通过向量相似性搜索找到语义上相近的关系，并将其分组。
            -   **LLM验证与合并**: 要求LLM对每个分组内的关系进行验证，并确定一个统一的“规范关系”来代表整个分组（例如，将 'job', 'occupation' 等合并为 'profession'）。
            -   **生成最终知识点**: 将原始三元组中的关系替换为规范化后的关系，形成最终的“知识点草稿”列表。

        4.  **存储与输出**: 将规范化后的知识点草稿列表存入共享上下文，并同时将其格式化为一个JSON文件 (`knowledge_point_drafts.json`) 保存到本地，以便查阅。



*(注：`InternetScraperAgent` 和 `AcademicScraperAgent` 在此工作流中变为次要角色，主要的数据源是本地文件。)*



### 阶段三：知识精炼与课程构建 (Stage 3: Knowledge Refinement and Course Construction)



1.  **`TheoreticalAnalysisAgent` & `PracticalAnalysisAgent`**:

    *   **逻辑**: 对从本地文件中提取的知识点草稿进行理论上的精炼和实践上的扩充，增加其深度和实用性。

    *   **算法**:

        1.  **理论分析**: 遍历每个知识点草稿，要求LLM进行理论上的补充和修正。

        2.  **实践分析**: 遍历经过理论分析的知识点，要求LLM为其添加实际的应用案例或代码示例。

        3.  将处理后的知识点列表更新到共享的上下文中。



2.  **`KgBuilderAgent` (execute方法)**:

    *   **逻辑**: 从经过实践增强的知识点中，利用LLM提取出知识三元组（头实体、关系、尾实体）。

    *   **算法**:

        1.  将多个知识点打包成批次以提高效率。

        2.  构建Prompt，要求LLM从知识点的文本中提取所有的知识三元组。

        3.  调用LLM服务，获取JSON格式的三元组列表，并存入共享上下文。



### 阶段四：知识图谱集成与验证 (Stage 4: Knowledge Graph Integration and Validation)



1.  **`KgBuilderAgent` (integrate_kps方法)**:

    *   **逻辑**: 将所有提取出的三元组整合成一个统一的知识图谱，并将其 **自动存储到Neo4j数据库** 中。

    *   **算法**:

        1.  从上下文中收集所有三元组。

        2.  调用`Neo4jDriver`，将每个三元组写入Neo4j。头实体和尾实体成为节点，关系成为边。



### 阶段五：报告生成与交付 (Stage 5: Report Generation and Delivery)



1.  **`ReportGenerationAgent`**:

    *   **逻辑**: 基于最终的知识图谱，自动生成一份全面的总结报告。

    *   **算法**:

        1.  从上下文中获取最终的知识图谱。

        2.  要求LLM撰写一份Markdown格式的报告。

        3.  将报告保存为 `.md` 文件。



## 使用 (Usage)

### 运行完整的Web服务

1.  **运行FastAPI服务器**:

    ```bash

    uvicorn src.main:app --reload

    ```

    API将在 `http://127.0.0.1:8000` 上可用。您可以通过 `http://127.0.0.1:8000/docs` 访问交互式API文档 (Swagger UI)。


2.  **通过API触发完整流水线**:

    所有知识图谱相关的API都以 `/kg` 为前缀。

    -   **`POST /kg/build`**: 触发异步流水线以构建指定课程的知识图谱。现在支持通过请求体传递 `data_path` 参数，用于指定本地Markdown和图片文件的路径。

        -   **方法**: `POST`

        -   **URL**: `http://127.0.0.1:8000/kg/build`

        -   **请求体 (JSON)**:

            ```json

            {

                "course_name": "Data Science",

                "data_path": "E:/data"  // 可选，本地文件路径

            }

            ```

### 运行多模态内容解析与预处理

- **目的**: 此脚本用于独立测试流水线的“阶段二：数据收集与预处理”。它会从一个指定的本地目录（例如 `E:/data` 或 `data/`）读取分层组织的课程材料（Markdown文件和图片）。
- **效果**:
  1. **执行 `MultimodalParserAgent`**: 脚本会遍历指定的 `data_path`，将每个课程下所有零散的 `.md` 文件和图片路径聚合成一个统一的、大的Markdown文件（例如 `Slides.md` 或 `课程名.md`），并保存在项目根目录。
  2. **执行 `ContentUnderstandingAgent`**: 接着，这个聚合后的Markdown文件内容会被传递给内容理解代理，进行知识点的初步提取。
- **命令**:
  ```bash
  python temp_run_multimodal_parser.py
  ```
  *(注意: 您可能需要修改 `temp_run_multimodal_parser.py` 脚本内部的 `data_path` 变量来指向您的实际数据目录。)*

### 运行核心流水线测试脚本 (推荐)

如果您想快速测试核心的知识提取和图谱构建流程，而无需启动完整的Web服务，可以直接运行测试脚本。

- **命令**:
  ```bash
  python temp_run_10_chunks.py
  ```

- **功能**:
  该脚本将执行一个简化的端到端流程：
  1.  **读取源文件**: 自动读取项目根目录下的 `Slides.md` 文件作为输入数据。
  2.  **执行内容理解**: 运行 `ContentUnderstandingAgent`，它会使用EDC（提取-定义-规范化）方法从文本中提取知识点。
  3.  **执行图谱构建**: 运行 `KgBuilderAgent`，它会从知识点中进一步提取知识三元组。
  4.  **存储结果**:
      - 将提取的三元组 **存储到Neo4j数据库** 中。
      - 同时，将三元组以JSON格式 **保存到本地文件**，命名为 `KgBuilder_Introduction_to_High-Performance_and_Parallel_Computing.json`。

这个脚本是验证核心Agent逻辑和LLM集成的最直接方式。

### 其他API端点

-   **`GET /kg/build/status/{task_id}`**: 获取知识图谱构建任务的状态。

    -   **示例**: `http://127.0.0.1:8000/kg/build/status/your-task-id`


-   **`GET /kg/plan_kg/{course_name}`**: 为课程生成学习计划（此为旧有接口，可能与新流水线不完全兼容）。

-   **`GET /kg/generate_knowledge/{topic}`**: 为主题生成知识文本（此为旧有接口，可能与新流水线不完全兼容）。

-   **`POST /kg/extract_triplets`**: 从文本块中提取三元组（此为旧有接口，可能与新流水线不完全兼容）。

-   **`POST /kg/store_triplets`**: 在数据库中存储三元组列表（此为旧有接口，可能与新流水线不完全兼容）。






## 运行测试



要运行单元测试，请从项目根目录执行以下命令：



```bash



pytest



```



## 代码文件说明

以下是项目核心代码文件的功能摘要：

-   `src/main.py`: **应用主入口**。使用FastAPI创建Web服务器，并定义了用于触发知识图谱构建流程的API端点。

-   `src/config.py`: **配置文件**。从环境变量（`.env`文件）中加载所有配置，如API密钥、数据库连接信息等。

-   `src/core/orchestrator.py`: **总指挥**。定义了`Orchestrator`类，负责按顺序执行流水线的各个阶段和其中的智能体。

-   `src/core/agent_manager.py`: **智能体管理器**。定义了`AgentManager`类，用于注册、管理和检索项目中的所有智能体。

-   `src/agents/base_agent.py`: **基础智能体**。定义了所有智能体都必须继承的抽象基类`BaseAgent`，包含了通用属性和方法。

-   `src/agents/multimodal_parser_agent.py`: **本地文件解析器**。负责从本地文件系统（如 `E:\data`）读取`.md`文件和图片文件，是当前工作流的主要数据来源。它会为每个课程生成一个聚合的Markdown文件（例如 `课程名.md`），并记录图片路径。

-   `src/agents/*_agent.py`: **具体智能体**。每个文件都实现了一个特定的智能体，负责流水线中的一个具体任务。例如：
    -   `content_understanding_agent.py`: 理解从本地文件读取的内容，提取知识点草稿，并生成一个 `knowledge_point_drafts.md` 文件。
    -   `kg_builder_agent.py`: 从知识点中提取三元组，并将其集成到Neo4j知识图谱中。
    -   `internet_scraper_agent.py` & `academic_scraper_agent.py`: 在当前工作流中作为次要数据源，提供模拟的在线数据。

-   `src/services/llm_service.py`: **LLM服务**。封装了与大型语言模型API交互的逻辑，提供文本生成功能。

-   `src/database/neo4j_driver.py`: **Neo4j数据库驱动**。提供了连接和操作Neo4j图数据库的方法，特别是存储三元组。

-   `src/utils/json_parser.py`: **JSON解析工具**。提供从LLM返回的原始文本中提取有效JSON对象的工具函数。

-   `create_csv.py`: **CSV生成脚本**。在流水线执行完毕后，用于从`final_context.json`中提取知识图谱三元组，并生成`knowledge_graph.csv`文件。

-   `tests/`: **测试目录**。包含了对项目中各个模块的单元测试。