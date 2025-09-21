import logging
from typing import Any

from dhti_elixir_base import BaseChain, get_di
from dhti_elixir_base.cds_hook import CDSHookCard
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.tools import tool
from overrides import override

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestChain(BaseChain):

    def inputParser2(self, input: Any):
            # Try to extract CommunicationRequest content if possible
            try:
                entries = input["input"].context["draftOrders"]["entry"]
                communication_request = next(
                    (entry for entry in entries if entry.get("resource", {}).get("resourceType") == "CommunicationRequest"),
                    None,
                )
                if communication_request:
                    content = communication_request["resource"]["payload"][0]["contentString"]
                    logger.info(f"Extracted content: {content}")
                    return {"input": content}
            except Exception as e:
                logger.info(f"inputParser2 fallback: {e}, input: {input}")

            # Fallback: try to return input["input"] if possible
            if isinstance(input, dict) and "context" in input:
                logger.info(f"inputParser2 fallback: returning input['context']")
                return input["context"]

            # Final fallback: return input as is
            logger.info(f"inputParser2 final fallback: returning input as is")
            return input

    def outputCard2(self, text: str) -> dict:
        cards = {"cards": [CDSHookCard(summary=text)]}
        return cards

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | self.inputParser2 | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() | self.outputCard2 # type: ignore
        chain = _chain.with_types(input_type=self.input_type)
        return chain


# Named chain according to the langchain template convention
# The description is used by the agents
# This is only in the inherited class, not in the base class
@tool(TestChain().name or "test_chain", args_schema=TestChain().input_type)
def chain(**kwargs):
    """
    This is a template chain that takes a text input and returns a summary of the text.

    The input is a dict with the following mandatory keys:
        input (str): The text to summarize.
    """
    return TestChain().chain.invoke(kwargs)
