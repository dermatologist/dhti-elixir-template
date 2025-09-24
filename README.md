# dhti-elixir-template for [DHTI](https://github.com/dermatologist/dhti)

[![Release](https://img.shields.io/github/v/release/dermatologist/dhti-elixir-template)](https://img.shields.io/github/v/release/dermatologist/dhti-elixir-template)
[![Build status](https://img.shields.io/github/actions/workflow/status/dermatologist/dhti-elixir-template/pytest.yml?branch=develop)](https://github.com/dermatologist/dhti-elixir-template/actions/workflows/pytest.yml?query=branch%3Adevelop)
[![codecov](https://codecov.io/gh/dermatologist/dhti-elixir-template/branch/develop/graph/badge.svg)](https://codecov.io/gh/dermatologist/dhti-elixir-template)
[![Commit activity](https://img.shields.io/github/commit-activity/m/dermatologist/dhti-elixir-template)](https://img.shields.io/github/commit-activity/m/dermatologist/dhti-elixir-template)
[![License](https://img.shields.io/github/license/dermatologist/dhti-elixir-template)](https://img.shields.io/github/license/dermatologist/dhti-elixir-template)

This is a template repository for [DHTI Elixirs](https://github.com/dermatologist/dhti)

Create template by using the [cookiecutter template](https://github.com/dermatologist/cookiecutter-uv)

## Running the server for testing

```bash
uv run python tests/server.py
```

## Routes (Name `dhti_elixir_template` should be replaced with your elixir name)

- `GET /langserve`: A simple root endpoint that returns a welcome message.
- `GET /langserve/dhti_elixir_template/cds-services`: Endpoint to access CDS services discovery.
- `POST /langserve/dhti_elixir_template/cds-services/dhti-service`: Endpoint to invoke services.
- `POST /langserve/mcp/messages`: Endpoint for sending messages to the MCP server.
- `GET /langserve/mcp/sse`: Endpoint for Server-Sent Events (SSE) to receive real-time updates.
- `GET /langserve/mcp` : Base path for MCP server functionalities (for configuration of MCP client using SSE).

## Testing

Test using [cds-hooks sandbox](https://github.com/dermatologist/cds-hooks-sandbox). Use the endpoint to access CDS services discovery.

## How to use this template

- Write your code in `src/dhti_elixir_template/chain.py` (replace `dhti_elixir_template` with your elixir name) as DhtiChain class.
- Follow the same (chain) pattern for agents as well.

## Give us a star ⭐️
If you find this project useful, give us a star. It helps others discover the project.

## Contributors

* [Bell Eapen](https://nuchange.ca) | [![Twitter Follow](https://img.shields.io/twitter/follow/beapen?style=social)](https://twitter.com/beapen)