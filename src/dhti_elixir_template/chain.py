import logging
from typing_extensions import override

from dhti_elixir_base import BaseChain, get_di
from dhti_elixir_base.cds_hook.generate_cards import add_card, get_card
from dhti_elixir_base.cds_hook.request_parser import get_context
from dhti_elixir_base.fhir.fhir_search import DhtiFhirSearch
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from langchain.tools import tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DhtiChain(BaseChain):

    def print_log(self, message):
        logger.info(message)
        print(message)
        return message

    @property
    @override
    def chain(self): # type: ignore
        _chain = RunnablePassthrough() | get_context | get_di("template_main_prompt") | get_di("template_main_llm") | StrOutputParser() | get_card # type: ignore
        _fhir = (
            RunnablePassthrough()
            | get_context
            | self.print_log
            | DhtiFhirSearch().get_conditions_for_patient
            | self.print_log
        )
        # Run both in parallel using RunnableParallel
        runnable = RunnableParallel(first=_chain, second=_fhir)
        return runnable.with_types(input_type=self.input_type)
