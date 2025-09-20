import pytest
import requests


@pytest.fixture
def chain():
    from src.dhti_elixir_template import TestChain
    return TestChain().chain


def test_chain_invoke(chain, capsys):
    input_data = {"input": "Answer in one word: What is the capital of France?"}
    result = chain.invoke(input=input_data)  # type: ignore
    print(result)
    captured = capsys.readouterr()
    assert "Paris" in captured.out or "know" in captured.out


def test_chain_invoke_with_hook(chain, capsys):
    input_data = {
        "hookInstance": "test_hook",
        "fhirServer": "http://example.com/fhir",
        "fhirAuthorization": "Bearer test_token",
        "hook": "patient-view",
        "context": {"input": "Hello"},
        "prefetch": {},
    }
    result = chain.invoke(input=input_data)  # type: ignore
    print(result)
    captured = capsys.readouterr()
    assert "Paris" in captured.out or "know" in captured.out
