from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string
from src.services.llm_service import generate_text_sync
import asyncio
from requests.exceptions import ReadTimeout
from src.utils.text_splitter import recursive_text_splitter

class ContentUnderstandingAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)
        self.concurrency_limit = 80

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes raw text data using a simple recursive splitter and generates knowledge point drafts.
        """
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Understanding content for '{course_name}'. Combining and splitting data from multiple sources.")

        internet_content = initial_context.get("internet_scraped_content", "")
        academic_content = initial_context.get("academic_scraped_content", "")
        multimodal_content = initial_context.get("multimodal_parsed_content", [])

        # Combine all text sources into a single string
        full_text = "\n\n---\n\n".join(multimodal_content)
        if internet_content:
            full_text += "\n\n---\n\n" + internet_content
        if academic_content:
            full_text += "\n\n---\n\n" + academic_content

        if not full_text.strip():
            self._log("No content to understand.")
            initial_context["knowledge_point_drafts"] = []
            return initial_context

        # Use the simple recursive text splitter
        text_chunks = recursive_text_splitter(full_text)
        self._log(f"Split content into {len(text_chunks)} chunks.")

        semaphore = asyncio.Semaphore(self.concurrency_limit)

        async def process_chunk(chunk_num, chunk):
            async with semaphore:
                prompt = f"""
                Based on the following content for a course on "{course_name}", identify and generate a list of key knowledge points.
                Each knowledge point should be a dictionary with 'title', 'explanation', and 'keywords' (a list of strings).
                Return a JSON array of these dictionaries.

                Content:
                {chunk}
                """
                
                self._log(f"Processing chunk {chunk_num + 1}/{len(text_chunks)}")
                try:
                    kp_drafts_json_str = await asyncio.to_thread(generate_text_sync, prompt, 0.5)
                    kp_drafts = extract_json_from_string(kp_drafts_json_str)

                    if isinstance(kp_drafts, list) and all(isinstance(item, dict) for item in kp_drafts):
                        return kp_drafts
                    else:
                        self._log(f"Failed to generate valid knowledge point drafts for chunk {chunk_num + 1}. Raw LLM output: {kp_drafts_json_str}")
                        return []
                except ReadTimeout:
                    self._log(f"ReadTimeout error on chunk {chunk_num + 1}. Skipping this chunk.")
                    return []

        tasks = [process_chunk(i, chunk) for i, chunk in enumerate(text_chunks)]
        results = await asyncio.gather(*tasks)
        
        all_knowledge_points = [item for sublist in results for item in sublist]

        self._log(f"Knowledge point drafts generated: {len(all_knowledge_points)} total.")
        
        # Save knowledge point drafts to a Markdown file
        if all_knowledge_points:
            # Sanitize course_name for use in filename
            sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip()
            sanitized_course_name = sanitized_course_name.replace(' ', '_')
            filename = f"knowledge_point_drafts_{sanitized_course_name}.md"
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for i, kp in enumerate(all_knowledge_points):
                        f.write(f"## {i+1}. {kp.get('title', 'No Title')}\n\n")
                        f.write(f"**Explanation:**\n{kp.get('explanation', 'No explanation provided.')}\n\n")
                        f.write(f"**Keywords:**\n- {'\n- '.join(kp.get('keywords', []))}\n\n")
                        f.write("---\n\n")
                self._log(f"Knowledge point drafts saved to '{filename}'.")
            except Exception as e:
                self._log(f"Error writing knowledge point drafts file: {e}")

        initial_context["knowledge_point_drafts"] = all_knowledge_points

        return initial_context