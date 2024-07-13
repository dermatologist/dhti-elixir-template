import pytest
import requests


@pytest.fixture
def chain():
    from dhti_elixir_template.chain import chain
    return chain

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