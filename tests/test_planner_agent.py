import pytest
import json
import requests
from src.agents.planner_agent import plan_course_kg_construction

def test_plan_course_kg_construction_success(mocker):
    """
    Tests the successful generation of a course plan by mocking the LLM API call.
    """
    # 1. Mock the response from the requests.post call
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    
    # The expected content from the LLM, which is a JSON string inside a larger structure
    expected_plan = [
        "Introduction to Machine Learning",
        "Supervised Learning: Regression and Classification",
        "Unsupervised Learning: Clustering and Dimensionality Reduction",
        "Neural Networks and Deep Learning"
    ]
    mock_llm_content = f"Here is the plan you requested: {json.dumps(expected_plan)}"
    
    mock_response.json.return_value = {
        "choices": [{
            "message": {
                "content": mock_llm_content
            }
        }]
    }
    
    # Patch requests.post to return our mock response
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function under test
    course_name = "DSAA2011 Machine Learning"
    actual_plan = plan_course_kg_construction(course_name)

    # 3. Assert the results
    assert actual_plan == expected_plan

def test_plan_course_kg_construction_api_error(mocker):
    """
    Tests how the function handles an API error from requests.post.
    """
    # 1. Mock the requests.post to raise an exception
    mocker.patch('requests.post', side_effect=requests.exceptions.RequestException("API is down"))

    # 2. Call the function
    course_name = "Some Course"
    result = plan_course_kg_construction(course_name)

    # 3. Assert that the function returns a specific error message
    assert result == ["Error: API call failed."]

def test_plan_course_kg_construction_bad_json(mocker):
    """
    Tests how the function handles a response with invalid JSON from the LLM.
    """
    # 1. Mock the response with malformed JSON
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{
            "message": {
                "content": "This is not a valid JSON list."
            }
        }]
    }
    mocker.patch('requests.post', return_value=mock_response)

    # 2. Call the function
    course_name = "Some Course"
    result = plan_course_kg_construction(course_name)

    # 3. Assert the error message
    assert result == ["Error: No JSON list found in response."]
