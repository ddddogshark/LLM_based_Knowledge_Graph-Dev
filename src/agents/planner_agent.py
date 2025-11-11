import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

def plan_course_kg_construction(course_name: str) -> list[str]:
    """
    Generates a plan for constructing the knowledge graph for a given course by calling an LLM.
    """
    if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
        print("DeepSeek API key or URL not configured.")
        return [f"Error: API credentials not configured."]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    }

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

    data = {
        "model": "DeepSeek-R1-671B",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()
        content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "[]")
        
        # Clean the content to extract only the JSON list
        try:
            # Find the start and end of the JSON list
            start_index = content.find('[')
            end_index = content.rfind(']') + 1
            if start_index != -1 and end_index != 0:
                json_str = content[start_index:end_index]
                plan = json.loads(json_str)
                if isinstance(plan, list):
                    return plan
                else:
                    print(f"Warning: LLM returned a non-list JSON object: {plan}")
                    return [f"Error: LLM returned a non-list object."]
            else:
                print(f"Warning: Could not find a JSON list in the LLM response: {content}")
                return [f"Error: No JSON list found in response."]
        except json.JSONDecodeError:
            print(f"Error decoding JSON from LLM response. Raw content: {content}")
            return [f"Error: Failed to decode JSON from LLM."]

    except requests.exceptions.RequestException as e:
        print(f"Error calling DeepSeek API for planning: {e}")
        return [f"Error: API call failed."]
