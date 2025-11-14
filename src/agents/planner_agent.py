import json
from .base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, course_name: str) -> list[str]:
        """
        Generates a plan for constructing the knowledge graph for a given course by calling an LLM.
        """
        self._log(f"Generating plan for course: {course_name}")
        prompt = f"""
    As an expert curriculum designer, create a detailed syllabus or topic outline for the course "{course_name}".
    The outline should consist of a list of key concepts, topics, and sub-topics that are essential for understanding the subject.
    Return the output as a JSON formatted list of strings.

    Example for "Introduction to Python":
    [
        "Python Basics: Variables, Data Types, and Operators",
        "Control Flow: If statements, For and While loops",
        "Data Structures: Lists, Tuples, Dictionaries, and Sets",
        "Functions and Modules",
        "File I/O",
        "Object-Oriented Programming: Classes and Objects",
        "Error and Exception Handling"
    ]

    Course: "{course_name}"
    """
        content = await self.llm_service.generate_text(prompt, temperature=0.5)
        
        if "Error" in content:
            self._log(f"Error generating plan: {content}")
            return [f"Error: {content}"]

        try:
            # Clean the content to extract only the JSON list
            start_index = content.find('[')
            end_index = content.rfind(']') + 1
            if start_index != -1 and end_index != 0:
                json_str = content[start_index:end_index]
                plan = json.loads(json_str)
                if isinstance(plan, list):
                    self._log(f"Successfully generated plan with {len(plan)} topics.")
                    return plan
                else:
                    self._log(f"Warning: LLM returned a non-list JSON object: {plan}")
                    return [f"Error: LLM returned a non-list object."]
            else:
                self._log(f"Warning: Could not find a JSON list in the LLM response: {content}")
                return [f"Error: No JSON list found in response."]
        except json.JSONDecodeError:
            self._log(f"Error decoding JSON from LLM response. Raw content: {content}")
            return [f"Error: Failed to decode JSON from LLM."]
