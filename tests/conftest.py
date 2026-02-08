import pytest


@pytest.fixture
def python_venv():
    venv = ".venv/bin/python"
    return venv
