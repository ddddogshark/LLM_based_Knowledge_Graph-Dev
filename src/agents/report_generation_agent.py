from .base_agent import BaseAgent
from typing import Dict, Any
import json
import os

class ReportGenerationAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates various reports (e.g., Markdown, mind maps, queryable databases) from the final knowledge graph.
        """
        final_knowledge_graph = initial_context.get("final_knowledge_graph", [])
        course_name = initial_context.get("course_name", "a generic subject")

        self._log(f"Generating final report for '{course_name}' from {len(final_knowledge_graph)} triplets.")

        if not final_knowledge_graph:
            self._log("No final knowledge graph to generate a report from.")
            initial_context["final_report"] = "No knowledge graph data available for reporting."
            initial_context["final_report_path"] = None
            return initial_context

        # Convert triplets to a readable string for the LLM
        triplets_str = "\n".join([f"- ({t['head']}) -[{t['relation']}]-> ({t['tail']})" for t in final_knowledge_graph])

        prompt = f"""
        As a Report Generation Specialist, your task is to create a comprehensive Markdown report summarizing the constructed knowledge graph for the course "{course_name}".

        The knowledge graph consists of the following triplets:
        ---
        {triplets_str}
        ---

        Your report should include:
        1.  **Introduction:** Briefly describe the purpose of the knowledge graph.
        2.  **Key Concepts and Relationships:** Highlight the most important entities and their connections.
        3.  **Structure Overview:** Explain how the knowledge graph is organized.
        4.  **Potential Applications:** Suggest how this knowledge graph can be used.
        5.  **Summary of Triplet Count:** Mention the total number of triplets.

        Format the output as a well-structured Markdown document.
        """
        
        final_report = await self.llm_service.generate_text(prompt)
        self._log("Final report generated.")
        
        # Save the report to a Markdown file
        report_filename = f"{course_name.replace(' ', '_')}_KG_Report.md"
        report_path = os.path.join(os.getcwd(), report_filename) # Save in current working directory
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(final_report)
        self._log(f"Final report saved to: {report_path}")

        initial_context["final_report"] = final_report
        initial_context["final_report_path"] = report_path
        return initial_context