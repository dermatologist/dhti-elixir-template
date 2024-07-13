from dhti_elixir_base import BaseChain, get_di
from langchain_core.pydantic_v1 import BaseModel, Field
from overrides import override
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from langchain.tools import tool

class RagChain(BaseChain):

    class ChainInput(BaseModel):
        input: str = Field(default="")

    @override
    def init_prompt(self):
        # Override the input type
        self.input_type = self.ChainInput

    @property
    @override
    def chain(self):
        _chain = RunnablePassthrough() | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser()
        chain = _chain.with_types(input_type=self.input_type)
        return chain

# Named chain according to the langchain template convention
@tool(RagChain().name, args_schema=RagChain().input_type)
def chain(**kwargs):
    """
    Description of what this chain does for agents.

    The input is a dict with the following mandatory keys:
        input (str): The question to ask based on the available context from the patient's health record.
    """
    return RagChain().chain.invoke(kwargs)