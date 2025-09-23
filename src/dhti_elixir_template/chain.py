import logging
from typing_extensions import override

from dhti_elixir_base import BaseChain, get_di
from dhti_elixir_base.cds_hook.generate_cards import add_card, get_card
from dhti_elixir_base.cds_hook.request_parser import get_context
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.tools import tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestChain(BaseChain):

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | get_context | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() | get_card # type: ignore
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
