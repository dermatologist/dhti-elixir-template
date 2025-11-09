import logging
from typing_extensions import override

from dhti_elixir_base import BaseChain, get_di
from dhti_elixir_base.cds_hook.generate_cards import add_card, get_card
from dhti_elixir_base.cds_hook.request_parser import get_context
from dhti_elixir_base.fhir.fhir_search import DhtiFhirSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.tools import tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DhtiChain(BaseChain):

    def print_log(self, message):
        logger.info(message)
        print(message)
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

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | get_context | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() | get_card # type: ignore
        _fhir = (
            RunnablePassthrough()
            | get_context
            | self.fhir_path_process
            | get_card
        )
        # Run both in parallel using RunnableParallel
        runnable = RunnableParallel(first=_chain, second=_fhir)
        return _chain.with_types(input_type=self.input_type)
