class ToolkitError(Exception):
    """Ошибка приложения"""


class CalculatorError(ToolkitError):
    """Ошибка калькулятора"""


class EmptyExpressionError(CalculatorError):
    """Пустое выражение"""


class InvalidExpressionError(CalculatorError):
    """Некорректное выражение"""


class InvalidCharacterError(CalculatorError):
    """Недопустимый символ в выражении"""


class DivisionZeroError(CalculatorError):
    """Ошибка при делении на ноль"""


class ConverterError(ToolkitError):
    """Ошибка конвертера величин"""


class UnknownUnitError(ConverterError):
    """Неизвестная единица измерения"""


class IncompatibleUnitsError(ConverterError):
    """Ошибка конвертации между несовместимыми единицами"""


class TemperatureError(ConverterError):
    """недопустимое значение температуры"""

class LenghError(ConverterError):
    """длина не может быть отрицательной"""

class MassError(ConverterError):
    """Масса не может быть отрицательной"""
