import logging
from typing_extensions import override
from fhiry import FlattenFhir
from dhti_elixir_base import BaseChain, get_di
from dhti_elixir_base.cds_hook.generate_cards import get_card
from dhti_elixir_base.cds_hook.request_parser import get_context
from dhti_elixir_base.fhir.fhir_search import DhtiFhirSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DhtiChain(BaseChain):

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
            if context.get("input"):
                return f"Given the following FHIR resources: {FlattenFhir(_everything).flattened}, Answer the following question in a complete sentence: {context['input']}."
            return str(FlattenFhir(_everything).flattened)
        except Exception as e:
            self.print_log(f"Error in fhir_everything: {e}")
            return "Demo working, but FHIR search failed."

    @property
    @override
    def chain(self):  # type: ignore
        _chain = (
            RunnablePassthrough()
            | get_context
            | self.fhir_everything
            | get_di("template_main_llm")  # type: ignore
            | StrOutputParser()
            | get_card
        )
        return _chain.with_types(input_type=self.input_type)
