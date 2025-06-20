# dhti-elixir-template

* [DHTI](https://github.com/dermatologist/dhti) Elixir Template
* WIP

## Using the template
* Use the template to create a new repository on GitHub with the default branch set to develop
* Clone the repository to your local machine
* rename `elixir-template` to your elixir-packagename
* rename `elixir_template` to your elixir_packagename
* rename the directory `src/dhti_elixir_template` to your `src/dhti_elixir_packagename`

## Installation
* pip install -e .[dev]

## Testing Environment Setup

Override [`tests/bootstrap.py`](tests/bootstrap.py) with your own configuration.

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add --repo https://github.com/dermatologist/dhti-elixir-template --branch develop
```

And add the following code to your `server.py` file after [bootstrapping](tests/bootstrap.py):
```python

from dhti_elixir_template.chain import chain as dhti_elixir_template_chain

add_routes(app, dhti_elixir_template_chain, path="/dhti-elixir-template")
```

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/dhti-elixir-template/playground](http://127.0.0.1:8000/dhti-elixir-template/playground)

We can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/dhti-elixir-template")
```