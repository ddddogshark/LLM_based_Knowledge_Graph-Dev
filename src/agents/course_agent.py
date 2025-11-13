# src/agents/course_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List

class CourseAgent(BaseAgent):
    def __init__(self, name: str, description: str, course_name: str):
        super().__init__(name, description)
        self.course_name = course_name

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log(f"Starting task for course: {self.course_name}")
        
        # In Stage 2, this agent's role is to provide a list of core resources.
        # This would be based on the task breakdown from the Subject Overview Plan.
        subject_plan = context.get("subject_overview_plan", "")
        
        prompt = f"""
        You are a Course-Specific Agent for "{self.course_name}".
        Based on the overall Subject Knowledge System Plan, your task is to provide a list of core resources
        for your course. This includes:
        1.  **Core Keywords:** A list of essential keywords for searching academic papers and web resources.
        2.  **Recommended Textbooks:** A list of recommended textbooks (if any).
        3.  **Key Online Resources:** A list of important websites, lecture series, or open-source projects.

        Here is the Subject Knowledge System Overall Plan:
        ---
        {subject_plan}
        ---
        
        Generate the resource list for "{self.course_name}".
        """
        
        resource_list_str = self.llm_service.generate_text(prompt, temperature=0.5)
        
        # Initialize course-specific context if it doesn't exist
        if "courses" not in context:
            context["courses"] = {}
        if self.course_name not in context["courses"]:
            context["courses"][self.course_name] = {}
            
        context["courses"][self.course_name]["resource_list"] = resource_list_str
        self._log(f"Generated resource list for {self.course_name}.")
        
        return context
