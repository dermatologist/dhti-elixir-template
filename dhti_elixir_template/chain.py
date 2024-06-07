from dhti_elixir_base import get_di
_prompt = get_di("template_main_prompt")
_llm = get_di("template_main_llm")


# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _llm
