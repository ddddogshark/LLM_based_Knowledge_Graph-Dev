import pytest
import requests
from src.agents.knowledge_generation_agent import generate_knowledge

def test_generate_knowledge_success(mocker):
    """
    Tests successful knowledge generation by mocking the LLM API call.
    """
    # 1. Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    expected_knowledge = "This is a detailed explanation about the topic."
    mock_response.json.return_value = {
        "choices": [{"message": {"content": expected_knowledge}}]
    }
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    topic = "Test Topic"
    actual_knowledge = generate_knowledge(topic)

    # 3. Assert the result
    assert actual_knowledge == expected_knowledge

def test_generate_knowledge_api_error(mocker):
    """
    Tests handling of an API error.
    """
    # 1. Mock the error
    mocker.patch('requests.post', side_effect=requests.exceptions.RequestException("API down"))

    # 2. Call the function
    topic = "Test Topic"
    result = generate_knowledge(topic)

    # 3. Assert the error message
    assert "Error calling DeepSeek API" in result

def test_generate_knowledge_no_content(mocker):
    """
    Tests handling of an empty or malformed response from the LLM.
    """
    # 1. Mock the malformed response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"choices": [{"message": {"content": None}}]} # No content
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    topic = "Test Topic"
    result = generate_knowledge(topic)

    # 3. Assert the default message
    assert result == "No content generated."
