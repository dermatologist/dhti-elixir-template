import logging
from typing import Any
from typing_extensions import override
from fhiry import FlattenFhir
from dhti_elixir_base import BaseChain, get_di, BaseAgent
from dhti_elixir_base.cds_hook.generate_cards import get_card
from dhti_elixir_base.cds_hook.request_parser import get_context
from dhti_elixir_base.fhir.fhir_search import DhtiFhirSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch, RunnableLambda, RunnableParallel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DhtiChain(BaseChain):

    def __init__(self):
        agent = BaseAgent(
            llm=get_di("function_llm"),  # type: ignore
        )
        self.my_agent = agent.get_agent_response
        super().__init__()

    def print_log(self, message):
        logger.info(message)
        return message

    def fhir_path_process(self, context: str):
        try:
            return str(DhtiFhirSearch().get_conditions_for_patient(
                    context,
                    fhirpath="Bundle.entry.resource.ofType(Condition).code.coding.code.first()", # Get first condition code
                ))
        except Exception as e:
            self.print_log(f"Error in fhir_path_process: {e}")
            return "Demo working, but FHIR search failed."

    def fhir_everything(self, context):
        try:
            _everything = DhtiFhirSearch().get_everything_for_patient(context)
            return str(FlattenFhir(_everything).flattened)
        except Exception as e:
            self.print_log(f"Error in fhir_everything: {e}")
            return "Demo working, but FHIR search failed."

    def get_question(self, context):
        return context.get("input", "")

    def get_string_message_to_agent(self, context):
        self.print_log(f"Message to agent: {context}")
        return str(f"Given the following FHIR resources: {context['fhir_context']}, Answer the following question in a complete sentence: {context['query']}.")

    def get_no_agent_response(self, context: Any):
        self.print_log("Agent has no tools, returning empty response.")
        return ""

    def get_output(self, context: Any) -> Any:
        return str(context)

    @property
    @override
    def chain(self):  # type: ignore
        _fhir_context = RunnablePassthrough() | get_context | self.fhir_everything
        _query = RunnablePassthrough() | get_context | self.get_question
        _chain = (
            RunnableParallel(fhir_context=_fhir_context, query=_query)
            | self.get_string_message_to_agent
            | self.my_agent
            | self.print_log
            | self.get_output
            | StrOutputParser()
            | get_card
        )
        return _chain.with_types(input_type=self.input_type)
