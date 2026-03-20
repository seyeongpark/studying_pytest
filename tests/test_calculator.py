#tests/test_calculator.py

from apps.calculator import Calculator
import pytest

#FIXTURE - 테스트 함수에서 공통적으로 사용되는 객체나 데이터를 생성하는 함수
# @pytest.fixture
# def calculator_fixture():
#     calc = Calculator()
#     return calc

def test_calculator_add(calculator_instance):
    calc = calculator_instance
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(2.5, 3.5) == 6.0

def test_calculator_substract(calculator_instance):
    calc = calculator_instance
    assert calc.substract(5, 2) == 3
    assert calc.substract(0, 5) == -5
    assert calc.substract(4, -3) == 7
    
def test_calculator_divide(calculator_instance):
    calc = calculator_instance
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 3) == -2

def test_calculator_divide_by_zero(calculator_instance):
    calc = calculator_instance
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)