# src/agents/report_generation_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any
import json

class ReportGenerationAgent(BaseAgent):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting final report generation...")
        
        integrated_triplets = context.get("integrated_triplets", [])
        course_name = context.get("course_name", "the course")
        
        if not integrated_triplets:
            self._log("No integrated triplets found to generate a report from.")
            context["final_report"] = "No knowledge graph was generated."
            return context
            
        self._log(f"Generating report for {len(integrated_triplets)} triplets.")
        
        prompt = f"""
        You are a Report Generation Agent. Your task is to create a comprehensive summary report
        in Markdown format based on the final, integrated knowledge graph for {course_name}.

        The report should include:
        1.  **Title:** A clear title for the report.
        2.  **Executive Summary:** A brief overview of the knowledge graph.
        3.  **Key Concepts:** A list of the most important concepts (entities) found in the graph.
        4.  **Key Relationships:** A summary of the main relationships discovered.
        5.  **Sample Triplets:** A small sample of representative triplets from the graph.
        6.  **Conclusion:** A concluding paragraph about the generated knowledge graph.

        Here is a sample of the knowledge graph triplets (Head, Relation, Tail):
        (Showing first 30 triplets)
        ---
        {json.dumps(integrated_triplets[:30], indent=2)}
        ---
        
        Generate the final report in Markdown format.
        """
        
        final_report = self.llm_service.generate_text(prompt, temperature=0.6)
        
        context["final_report"] = final_report
        self._log("Final report generated.")
        
        # Optionally, save the report to a file
        report_file_path = f"./{course_name.replace(' ', '_')}_KG_Report.md"
        with open(report_file_path, "w", encoding="utf-8") as f:
            f.write(final_report)
        self._log(f"Report saved to {report_file_path}")
            
        return context
