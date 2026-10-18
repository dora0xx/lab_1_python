from toolkit.constants import absolute_zero_c, all_units, lengh, mass, temperature
from toolkit.errors import (
    IncompatibleUnitsError,
    LenghError,
    MassError,
    TemperatureError,
    UnknownUnitError,
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """итоговая сборка конвертера величин"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    def convert_length(value: float, from_unit: str, to_unit: str) -> float:
        """конвертировать длину"""
        if value < 0:
            raise LenghError("длина не может быть отрицательной!")
        else:
            to_meters = value * lengh[from_unit]
            result = to_meters / lengh[to_unit]
            return result


    def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
        """конвертировать массу"""
        if value < 0:
            raise MassError("масса не может быть отрицательной!")
        else:
            to_grams = value * mass[from_unit]
            result = to_grams / mass[to_unit]
            return result


    # за основу для перевода берем температуру по цельсию
    def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
        """ковертировать температуру"""
        # блок для перевода в цельсий
        if from_unit == "f":
            c = (value - 32) * 5 / 9
        elif from_unit == "k":
            c = value - 273.15
        else:
            c = value
        if value < absolute_zero_c:
            raise TemperatureError("Температура ниже абсолютного нуля недопустима")

        # блок для перевода из цельсия в другую систему
        if to_unit == "f":
            f = c * 9 / 5 + 32
            return f
        elif to_unit == "k":
            k = c + 273.15
            return k
        return c


    if from_unit in lengh and to_unit in lengh:
        return convert_length(value, from_unit, to_unit)

    elif from_unit in mass and to_unit in mass:
        return convert_mass(value, from_unit, to_unit)

    elif from_unit in temperature and to_unit in temperature:
        return convert_temperature(value, from_unit, to_unit)

    elif from_unit not in all_units or to_unit not in all_units:
        raise UnknownUnitError("Неизвестная единица")
    else:
        raise IncompatibleUnitsError("несопоставимые единицы измерения")
