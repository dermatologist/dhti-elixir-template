import pytest
import requests


@pytest.fixture
def chain():
    from src.dhti_elixir_template import TestChain
    return TestChain().chain

def test_chain(chain):
    try:
        input = {
            "input": "Answer in one word: What is the capital of France?"
        }
        result = chain.invoke(input = input)
        assert result == 'Paris'
    except (requests.exceptions.ConnectionError) as e:
        print("ConnectionError: Skipping test")
        assert True