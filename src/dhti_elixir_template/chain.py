from dhti_elixir_base import BaseChain, get_di
from langchain_core.pydantic_v1 import BaseModel, Field
from overrides import override
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap, RunnablePassthrough
from langchain.tools import tool

class RagChain(BaseChain):

    class ChainInput(BaseModel): # type: ignore
        input: str = Field(default="")

    @override
    def init_prompt(self):
        # Override the input type
        self.input_type = self.ChainInput

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() # type: ignore
        chain = _chain.with_types(input_type=self.input_type)
        return chain

# Named chain according to the langchain template convention
# The description is used by the agents
@tool(RagChain().name, args_schema=RagChain().input_type) # type: ignore
def chain(**kwargs):
    """
    This is a template chain that takes a text input and returns a summary of the text.

    The input is a dict with the following mandatory keys:
        input (str): The text to summarize.
    """
    return RagChain().chain.invoke(kwargs)