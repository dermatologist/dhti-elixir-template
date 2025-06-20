import requests
from tests.bootstrap import bootstrap
bootstrap()
from dhti_elixir_template.chain import TestChain


input = {
    "input": "Answer in one word: What is the capital of France?"
}
result = TestChain().chain.invoke(input = input) # type: ignore
print(result)
assert result == 'Paris'
