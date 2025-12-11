# src/topic_analyzer.py

import collections
import re
from typing import List

def analyze_topics(content: List[str], top_n: int = 20):
    """
    Analyzes the topics in a list of strings by counting the frequency of keywords.
    """
    text = " ".join(content)
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    
    # Simple stop words list, can be expanded
    stop_words = set(['the', 'a', 'in', 'of', 'to', 'and', 'is', 'for', 'with', 'on', 'as', 'an', 'by', 'that', 'it', 'from', 'at', 'this', 'or', 'of', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'who', 'when', 'where', 'why', 'how', 'which', 'with', 'if', 'then', 'was', 'are', 'be', 'has', 'had', 'do', 'does', 'did', 'but', 'not', 'so', 'very', 'can', 'will', 'just'])
    
    words = [word for word in words if word not in stop_words and not word.isdigit()]
    
    word_counts = collections.Counter(words)
    
    return word_counts.most_common(top_n)

if __name__ == "__main__":
    import json
    
    try:
        with open('final_context.json', 'r') as f:
            final_context = json.load(f)
        
        multimodal_parsed_content = final_context.get('multimodal_parsed_content', [])
        
        if multimodal_parsed_content:
            topics = analyze_topics(multimodal_parsed_content)
            print("Top 20 topics in the source data:")
            for topic, count in topics:
                print(f"- {topic}: {count}")
        else:
            print("Could not find 'multimodal_parsed_content' in final_context.json or it is empty.")

    except FileNotFoundError:
        print("final_context.json not found. Please run the orchestrator first.")
    except json.JSONDecodeError:
        print("Error decoding final_context.json. The file might be corrupted.")
