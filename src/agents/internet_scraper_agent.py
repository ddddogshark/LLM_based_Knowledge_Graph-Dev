from .base_agent import BaseAgent
from typing import Dict, Any, List

class InternetScraperAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Scrapes external latest information based on keywords.
        """
        course_resources = initial_context.get("course_resources", {})
        keywords = course_resources.get("keywords", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Scraping internet for '{course_name}' using keywords: {keywords}")

        scraped_content_list = []
        if keywords:
            sentences = [
                "Data science is the study of data to extract meaningful insights for business.",
                "Machine learning is a subset of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience.",
                "Data analysis is a process of inspecting, cleansing, transforming and modeling data with the goal of discovering useful information.",
                "Data visualization is the graphical representation of information and data.",
                "Python is an interpreted, high-level and general-purpose programming language.",
                "R is a programming language and free software environment for statistical computing and graphics.",
            ]
            for i, keyword in enumerate(keywords):
                scraped_content_list.append(sentences[i % len(sentences)])
        else:
            scraped_content_list.append(f"No specific keywords provided for internet scraping for {course_name}.")

        scraped_content = "\n".join(scraped_content_list)
        
        self._log("Internet scraping completed (simulated).")
        initial_context["internet_scraped_content"] = scraped_content
        return initial_context