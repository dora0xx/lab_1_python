import pytest

from toolkit.calculator import calculate
from toolkit.errors import (
    DivisionZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidExpressionError,
)


#положительные тесты калькулятора
#сложение
def test_add():
    assert calculate("2 + 3") == 5.0

#умножение
def test_multiply():
    assert calculate("2 * 4") == 8.0

#приоритет операций
def test_operation_priority():
    assert calculate("2 + 3 * 4") == 14.0




# негативные тесты калькулятора
#деление на ноль
def test_negative_division_zero():
    with pytest.raises(DivisionZeroError):
        calculate("10 / 0")

#неверное выражение
def test_negative_epmty_exp():
    with pytest.raises(EmptyExpressionError):
        calculate("")

def test_negative_inval_exp_1():
    with pytest.raises(InvalidExpressionError):
        calculate("10 + * 1000")

def test_negative_invalid_exp_3():
    with pytest.raises(InvalidExpressionError):
        calculate("10 *")

def test_negative_wrong_character():
    with pytest.raises(InvalidCharacterError):
        calculate("10 / a")
