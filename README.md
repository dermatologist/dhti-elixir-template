# dhti-elixir-template for [DHTI](https://github.com/dermatologist/dhti)


<p align="center">
  <img src="https://github.com/dermatologist/openmrs-esm-dhti-template/blob/develop/notes/conch.jpg" />
</p>

This [DHTI](https://github.com/dermatologist/dhti) elixir template is a simple but functional EMR chatbot too!* 👉 [Try it out today!](https://github.com/dermatologist/dhti/blob/feature/fix-copy-1/README.md#try-it-out). Create [DHTI](https://github.com/dermatologist/dhti) elixirs by using the [cookiecutter](https://github.com/dermatologist/cookiecutter-uv)

There are three branches available:
* feature/chain-1: A simple chain example using Langchain. For beginners.
* feature/agent-1: A simple agent example using Langchain. The MCP agent automatically detects available tools using MCPX (included in DHTI).
* feature/agent-2: An advanced agent example using Langchain. The MCP agent automatically detects available tools using MCPX (included in DHTI) and uses a more advanced branching strategy with agent in the loop.

### Installation into DHTI

```
npx dhti-cli elixir install -g https://github.com/dermatologist/dhti-elixir-template.git -n dhti-elixir-template -b <branch-name>
```
[Read more about DHTI elixirs here](https://github.com/dermatologist/dhti)

## Running the server for testing

```bash
python tests/server.py
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