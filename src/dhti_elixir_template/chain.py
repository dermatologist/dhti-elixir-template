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
    pass
    # @property
    # @override
    # def chain(self): # type: ignore
    #     _chain = RunnablePassthrough() | get_context | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() | get_card # type: ignore
    #     chain = _chain.with_types(input_type=self.input_type)
    #     return chain

