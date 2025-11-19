from .base_agent import BaseAgent
from typing import Dict, Any, List
import os

class MultimodalParserAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses multimodal materials from the specified data path and returns a list of file contents.
        """
        data_path = initial_context.get("data_path")
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Parsing multimodal materials for '{course_name}' from path: {data_path}")

        if not data_path or not os.path.exists(data_path):
            self._log(f"Data path not found: {data_path}")
            initial_context["multimodal_parsed_content"] = []
            return initial_context

        all_md_content = []
        for root, _, files in os.walk(data_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            all_md_content.append(f.read())
                    except Exception as e:
                        self._log(f"Error reading file {file_path}: {e}")

        self._log(f"Successfully parsed {len(all_md_content)} markdown files.")
        initial_context["multimodal_parsed_content"] = all_md_content
        return initial_context