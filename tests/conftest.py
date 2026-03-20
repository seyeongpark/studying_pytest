# tests/conftest.py

from apps.calculator import Calculator
import pytest
from tests.data_loader import load_test_data

@pytest.fixture(scope="session")
def calculator_instance():
    print("\n -- Calculator instance setup (conftest.py) --")
    calc = Calculator()
    return calc

def pytest_generate_tests(metafunc):
    print(f"-----metafunc: {metafunc.fixturenames}")
    if "ADDCASE" in metafunc.fixturenames:
        cases = load_test_data("add.csv")
        metafunc.parametrize("ADDCASE", cases)
    elif "SUBCASE" in metafunc.fixturenames:
        cases = load_test_data("sub.csv")
        metafunc.parametrize("SUBCASE", cases)
    elif "MULCASE" in metafunc.fixturenames:
        cases = load_test_data("mul.csv")
        metafunc.parametrize("MULCASE", cases)
    elif "DIVCASE" in metafunc.fixturenames:
        cases = load_test_data("div.csv")
        metafunc.parametrize("DIVCASE", cases)
        