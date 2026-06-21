"""Agent implementations for the knowledge graph builder.

Each agent is responsible for a specific stage of the KG construction pipeline:
  - DemandAnalysisAgent — captures user requirements
  - CourseAgent — provides course-specific resources
  - MultimodalParserAgent — parses various document formats (PPT, PDF, etc.)
  - ContentUnderstandingAgent — extracts knowledge points via LLM
  - TheoreticalAnalysisAgent — validates theoretical rigor
  - PracticalAnalysisAgent — enriches with practical examples
  - KgBuilderAgent — builds sub-knowledge graphs (triplet extraction)
  - ValidationCoordinatorAgent — runs quality gates
  - ReportGenerationAgent — produces final reports
"""

from .base_agent import BaseAgent
