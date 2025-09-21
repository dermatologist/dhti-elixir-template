from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables.config import RunnableConfig
from fastapi.testclient import TestClient
from dhti_elixir_base import get_di
from fastapi.middleware.cors import CORSMiddleware

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

origins = [
        "*",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post("/langserve/dhti_elixir_template/cds-services/dhti-service")
async def invoke_chain(payload: dict):
    _input = {}
    _input["input"] = {}
    _input["input"]["input"] = payload
    # return dhti_elixir_template_chain(_input) # type: ignore
    # Call the route handler directly to ensure callbacks are used
    client = TestClient(app)
    response = client.post("/langserve/dhti_elixir_template/invoke", json=_input)
    cards = {
        "cards": [response.json().get("output", {})]
    }
    return cards


# https://cds-hooks.org/specification/current/#discovery
@app.get("/langserve/dhti_elixir_template/cds-services")
async def read_root():
    return get_di("cds_hook_discovery") or { "services": [] }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
