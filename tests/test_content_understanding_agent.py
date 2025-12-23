import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock, mock_open
from src.agents.content_understanding_agent import ContentUnderstandingAgent

import json
import numpy as np

# Mock the SentenceTransformer for faster testing without loading the actual model
@pytest.fixture(autouse=True)
def mock_sentence_transformer():
    with patch('src.agents.content_understanding_agent.SentenceTransformer') as MockTransformer:
        mock_model_instance = MockTransformer.return_value
        # Mock encode to return dummy embeddings
        mock_model_instance.encode.return_value = MagicMock()
        mock_model_instance.encode.return_value.cpu.return_value.numpy.return_value = \
            np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
        yield

# Mock the generate_text_async function globally for LLM calls
@pytest.fixture(autouse=True)
def mock_llm_service():
    with patch('src.agents.content_understanding_agent.generate_text_async', new_callable=AsyncMock) as mock_generate_text_async:
        # Default mock responses for various stages
        # Stage 1: OIE - return raw triplets
        mock_generate_text_async.side_effect = [
            # 1. First call for OIE
            json.dumps([
                ["concept1", "has property", "value1"],
                ["concept2", "is related to", "concept1"],
                ["concept3", "has property", "value3"]
            ]),
            # 2. Second call for relation definition "has property"
            "This relation indicates that the subject possesses the characteristic described by the object.",
            # 3. Third call for relation definition "is related to"
            "This relation signifies a general connection between two concepts.",
            # 4. Fourth call for converting canonical triplets for 'concept1'
            json.dumps({
                "title": "Concept1 Details",
                "explanation": "Concept1 possesses value1 and is related to concept2.",
                "keywords": ["concept1", "value1", "concept2"]
            }),
            # 5. Fifth call for converting canonical triplets for 'concept2'
            json.dumps({
                "title": "Concept2 Relations",
                "explanation": "Concept2 is generally related to concept1.",
                "keywords": ["concept2", "concept1"]
            }),
            # 6. Sixth call for converting canonical triplets for 'concept3'
            json.dumps({
                "title": "Concept3 Properties",
                "explanation": "Concept3 is associated with value3.",
                "keywords": ["concept3", "value3"]
            })
        ]
        yield mock_generate_text_async

@pytest.mark.asyncio
async def test_content_understanding_agent_edc_flow(mock_llm_service):
    agent = ContentUnderstandingAgent(
        name="TestContentUnderstandingAgent",
        description="A test agent for content understanding with EDC."
    )

    initial_context = {
        "course_name": "Test Course",
        "multimodal_parsed_content": ["This is some test content about concept1 and concept2. Concept3 is also here."],
        "internet_scraped_content": "More content about value1 and value3.",
        "academic_scraped_content": "Academic discussions linking concept1 to value1."
    }

    # Verify that the JSON file was attempted to be saved
    with patch('builtins.open', new_callable=mock_open) as mocked_open:
        result_context = await agent.execute(initial_context)

        # Assertions for the final knowledge point drafts
        assert "knowledge_point_drafts" in result_context
        assert isinstance(result_context["knowledge_point_drafts"], list)
        assert len(result_context["knowledge_point_drafts"]) > 0

        # The first knowledge point might be any of the three subjects, depending on dict iteration order.
        # So we check for general content in the list of knowledge points.
        found_concept1_kp = False
        found_concept2_kp = False
        found_concept3_kp = False
        for kp in result_context["knowledge_point_drafts"]:
            if "title" in kp and kp["title"] == "Concept1 Details":
                found_concept1_kp = True
                assert "explanation" in kp
                assert "keywords" in kp
                assert isinstance(kp["keywords"], list)
                assert "concept1" in kp["keywords"]
            elif "title" in kp and kp["title"] == "Concept2 Relations":
                found_concept2_kp = True
                assert "explanation" in kp
                assert "keywords" in kp
                assert isinstance(kp["keywords"], list)
                assert "concept2" in kp["keywords"]
            elif "title" in kp and kp["title"] == "Concept3 Properties":
                found_concept3_kp = True
                assert "explanation" in kp
                assert "keywords" in kp
                assert isinstance(kp["keywords"], list)
                assert "concept3" in kp["keywords"]
        
        assert found_concept1_kp
        assert found_concept2_kp
        assert found_concept3_kp

        # Verify that LLM calls were made as expected for OIE, definition, and final KP conversion
        assert mock_llm_service.call_count == 6

        # Assertions for the mocked_open call
        mocked_open.assert_called_once()
        call_args = mocked_open.call_args[0]
        assert call_args[0].endswith(".json")
        
        # Collect all content written by multiple calls to .write()
        written_content_list = [call.args[0] for call in mocked_open.return_value.write.call_args_list]
        full_written_content = "".join(written_content_list)
        
        # Check for presence of all three expected knowledge points in the JSON output
        assert '"title": "Concept1 Details"' in full_written_content
        assert '"title": "Concept2 Relations"' in full_written_content
        assert '"title": "Concept3 Properties"' in full_written_content

    # Test with no content
    no_content_context = {
        "course_name": "Empty Course",
        "multimodal_parsed_content": [],
        "internet_scraped_content": "",
        "academic_scraped_content": ""
    }
    empty_result_context = await agent.execute(no_content_context)
    assert "knowledge_point_drafts" in empty_result_context
    assert len(empty_result_context["knowledge_point_drafts"]) == 0
