import json
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables.config import RunnableConfig

# ! DO NOT REMOVE THE COMMENT BELOW
# DHTI_CLI_IMPORT
from bootstrap import bootstrap as dhti_elixir_template_bootstrap

dhti_elixir_template_bootstrap()
# add src to sys path
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from dhti_elixir_template.chain import chain as dhti_elixir_template_chain

import uvicorn

# Comes after elixir bootstraps, so can override elixir configurations
from bootstrap import bootstrap

bootstrap()

app = FastAPI(title="LangServe Launch Example")

try:
    from langfuse import Langfuse
    from langfuse.callback import CallbackHandler

    langfuse_handler.auth_check()
    langfuse_handler = CallbackHandler()
    config = RunnableConfig(callbacks=[langfuse_handler])
    # ! DO NOT REMOVE THE COMMENT BELOW
    # DHTI_LANGFUSE_ROUTE
    add_routes(
        app,
        dhti_elixir_template_chain.with_config(config),
        path="/langserve/dhti_elixir_template",
    )

except:
    # ! DO NOT REMOVE THE COMMENT BELOW
    # DHTI_NORMAL_ROUTE
    add_routes(app, dhti_elixir_template_chain, path="/langserve/dhti_elixir_template")
    x = True


@app.post("/langserve/dhti_elixir_template/dhti")
async def invoke_chain(payload: dict):

    _input = {}
    _input["input"] = {}
    _input["input"]["input"] = payload
    return dhti_elixir_template_chain(_input) # type: ignore


# https://cds-hooks.org/specification/current/#discovery
@app.get("/cds-services")
async def read_root():
    return {
        "services": [
            {
                "hook": "patient-view",
                "title": "Static CDS Service Example",
                "description": "An example of a CDS Service that returns a static set of cards",
                "id": "static-patient-greeter",
                "prefetch": {"patientToGreet": "Patient/{{context.patientId}}"},
            },
            {
                "hook": "order-select",
                "title": "Order Echo CDS Service",
                "description": "An example of a CDS Service that simply echoes the order(s) being placed",
                "id": "order-echo",
                "prefetch": {
                    "patient": "Patient/{{context.patientId}}",
                    "medications": "MedicationRequest?patient={{context.patientId}}",
                },
            },
            {
                "hook": "order-sign",
                "title": "Pharmacogenomics CDS Service",
                "description": "An example of a more advanced, precision medicine CDS Service",
                "id": "pgx-on-order-sign",
                "usageRequirements": "Note: functionality of this CDS Service is degraded without access to a FHIR Restful API as part of CDS recommendation generation.",
            },
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
