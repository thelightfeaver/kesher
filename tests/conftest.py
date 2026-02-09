import pytest


@pytest.fixture
def python_venv():
    venv = ".venv/bin/python"
    return venv


@pytest.fixture(autouse=True)
def clean_state_before_each_test():
    from util import clean_state

    clean_state()
    yield
    clean_state()
