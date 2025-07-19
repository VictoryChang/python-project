import pytest

from tests.calculator_client import CalculatorClient


@pytest.fixture(scope="session")
def client():
    return CalculatorClient()
