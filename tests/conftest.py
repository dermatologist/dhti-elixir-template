from dhti_elixir_template.bootstrap import bootstrap


def pytest_configure(config):
    print("Bootstrapping...")
    bootstrap()

