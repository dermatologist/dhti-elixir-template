# dhti-elixir-template for [DHTI](https://github.com/dermatologist/dhti)

## Deprecated. Use the [new monorepo instead.](https://github.com/dermatologist/dhti-elixir)

<p align="center">
  <img src="https://github.com/dermatologist/openmrs-esm-dhti-template/blob/develop/notes/conch.jpg" />
</p>

This [DHTI](https://github.com/dermatologist/dhti) elixir template is a simple but functional EMR chatbot too!* 👉 [Try it out today!](https://github.com/dermatologist/dhti/blob/feature/fix-copy-1/README.md#try-it-out). Create [DHTI](https://github.com/dermatologist/dhti) elixirs by using the [cookiecutter](https://github.com/dermatologist/cookiecutter-uv)

There are three branches available:
* feature/chain-1: A simple chain example using Langchain. For beginners.
* feature/agent-1: A simple agent example using Langchain. The MCP agent automatically detects available tools using MCPX (included in DHTI).
* feature/agent-2: An advanced agent example using Langchain. The MCP agent automatically detects available tools using MCPX (included in DHTI) and uses a more advanced branching strategy with agent in the loop.

[See the example bootstrapping code here](/src/dhti_elixir_template/bootstrap.py)

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

### Manual Usage

- Write your code in `src/dhti_elixir_template/chain.py` (replace `dhti_elixir_template` with your elixir name) as DhtiChain class.
- Follow the same (chain) pattern for agents as well.

### Using AI Agent Skills

This repository includes AI agent skills that can automatically generate new DHTI elixir projects from this template. The skills are available in two locations for compatibility:

- **Preferred location**: `.github/skills/elixir-generator/`
- **Legacy location**: `.claude/skills/elixir-generator/`

**To use the agent skill:**

1. Provide your elixir requirements to an AI agent with access to these skills
2. The agent will automatically:
   - Set up the development environment
   - Scaffold a new project using cookiecutter
   - Implement your requested functionality with FHIR integration
   - Create tests and documentation
   - Follow DHTI architectural patterns

**Example request:**
```
Please create a DHTI elixir that monitors blood glucose and HbA1c levels 
for diabetes patients over the last 6 months and provides clinical recommendations.
Project name: dhti-elixir-glycemic
```

See [examples](.github/skills/elixir-generator/examples/) for more detailed request templates.

## Give us a star ⭐️
If you find this project useful, give us a star. It helps others discover the project.

## Contributors

* [Bell Eapen](https://nuchange.ca) | [![Twitter Follow](https://img.shields.io/twitter/follow/beapen?style=social)](https://twitter.com/beapen)
