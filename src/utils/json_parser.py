import json
import re

def extract_json_from_string(text: str) -> any:
    """
    Extracts a JSON object or array from a string, even if it's embedded in other text
    or markdown code blocks.
    """
    if not text:
        return None

    # Regex to find JSON wrapped in markdown code blocks (```json ... ```)
    match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1)

    # Find the first '{' or '[' to start parsing from there
    start_brace = text.find('{')
    start_bracket = text.find('[')

    if start_brace == -1 and start_bracket == -1:
        return None

    if start_brace == -1:
        start_index = start_bracket
    elif start_bracket == -1:
        start_index = start_brace
    else:
        start_index = min(start_brace, start_bracket)

    # Find the last '}' or ']'
    end_brace = text.rfind('}')
    end_bracket = text.rfind(']')

    if end_brace == -1 and end_bracket == -1:
        return None
        
    end_index = max(end_brace, end_bracket)

    json_str = text[start_index : end_index + 1]

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None
