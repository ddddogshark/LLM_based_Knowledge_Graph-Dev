# src/utils/text_splitter.py

from typing import List

def recursive_text_splitter(text: str, chunk_size: int = 1000, chunk_overlap: int = 150, separators: List[str] = None) -> List[str]:
    """
    A simple recursive text splitter.
    """
    if separators is None:
        separators = ["\n\n", "\n", " ", ""]

    if len(text) <= chunk_size:
        return [text]

    # Find the best separator
    separator = ""
    for s in separators:
        if s in text:
            separator = s
            break
    
    # Split the text
    if separator:
        parts = text.split(separator)
    else:
        parts = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Merge small parts
    chunks = []
    current_chunk = ""
    for part in parts:
        if len(current_chunk) + len(part) + len(separator) > chunk_size:
            chunks.append(current_chunk)
            current_chunk = part
        else:
            if current_chunk:
                current_chunk += separator + part
            else:
                current_chunk = part
    if current_chunk:
        chunks.append(current_chunk)

    # Add overlap
    if chunk_overlap > 0 and len(chunks) > 1:
        for i in range(len(chunks) - 1):
            overlap = chunks[i+1][:chunk_overlap]
            chunks[i] += overlap

    return chunks
