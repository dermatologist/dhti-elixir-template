from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from kink import di

_prompt = di["main_prompt"]
_llm = di["main_llm"]


# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _llm
