import pytest

from toolkit.converter import convert
from toolkit.errors import (
    IncompatibleUnitsError,
    TemperatureError,
)


#положительные тесты конвертера
def test_length_convert():
    assert convert(100, "cm", "m") == 1.0

def test_mass_convert():
    assert convert(2, "kg", "g") == 2000.0

def test_temperature_convert():
    assert convert(32, "f", "c") == 0.0

def test_units_convert():
    assert convert(100, "CM", "M") == 1.0




#негативные тесты конвертера
def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        convert(10, "kg", "m")

def test_below_absolute_zero():
    with pytest.raises(TemperatureError):
        convert(-300, "c", "k")
