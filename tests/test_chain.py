import pytest


@pytest.fixture
def chain():
    with pytest.raises(TypeError):
        from dhti_elixir_template.chain import chain
        return chain

def test_chain(chain):
    assert chain is None
