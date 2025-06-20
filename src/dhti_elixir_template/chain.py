from dhti_elixir_base import BaseChain, get_di
from langchain_core.pydantic_v1 import BaseModel, Field
from overrides import override
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from langchain.tools import tool

class TestChain(BaseChain):

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() # type: ignore
        chain = _chain.with_types(input_type=self.input_type)
        return chain