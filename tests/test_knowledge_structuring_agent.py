import pytest
import json
import requests
from src.agents.knowledge_structuring_agent import extract_triplets

def test_extract_triplets_success(mocker):
    """
    Tests successful triplet extraction by mocking the LLM API call.
    """
    # 1. Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    expected_triplets = [
        {"head": "Entity1", "relation": "is", "tail": "Entity2"}
    ]
    mock_llm_content = json.dumps(expected_triplets)
    mock_response.json.return_value = {
        "choices": [{"message": {"content": mock_llm_content}}]
    }
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    text = "Some text to extract from."
    actual_triplets = extract_triplets(text)

    # 3. Assert the result
    assert actual_triplets == expected_triplets

def test_extract_triplets_api_error(mocker):
    """
    Tests handling of an API error.
    """
    # 1. Mock the error
    mocker.patch('requests.post', side_effect=requests.exceptions.RequestException("API down"))

    # 2. Call the function
    text = "Some text."
    result = extract_triplets(text)

    # 3. Assert the function returns an empty list
    assert result == []

def test_extract_triplets_bad_json(mocker):
    """
    Tests handling of a response with invalid JSON from the LLM.
    """
    # 1. Mock the malformed response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "This is not JSON."}}]
    }
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    text = "Some text."
    result = extract_triplets(text)

    # 3. Assert the function returns an empty list
    assert result == []

def test_extract_triplets_non_list_json(mocker):
    """
    Tests handling of a response with valid JSON that is not a list.
    """
    # 1. Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_llm_content = json.dumps({"key": "value"}) # A dictionary, not a list
    mock_response.json.return_value = {
        "choices": [{"message": {"content": mock_llm_content}}]
    }
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    text = "Some text."
    result = extract_triplets(text)

    # 3. Assert the function returns an empty list
    assert result == []
