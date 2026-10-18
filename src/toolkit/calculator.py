from toolkit.errors import (
    DivisionZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidExpressionError,
)


def is_number(token: str) -> bool:
    """функция для проверки на число"""
    try:
        float(token)
        return True
    except ValueError:
        return False


def tokenization(line: str) -> list[str]:
    """разбиваем входную строку на список с элементами"""
    itog = []
    ch = ""
    for i in line:
        if i.isdigit() or i == ".":
            ch = ch+i
        elif i == " " and ch != "":
            itog.append(ch)
            ch = ""
        elif i == " " and ch == "":
            continue
        elif i in "+/-*" and ch != "":
            itog.append(ch)
            ch = ""
            itog.append(i)
        elif i in "+/-*" and ch == "":
            itog.append(i)
        else:
            raise InvalidCharacterError("Недопустимый символ")
    if ch != "":
        itog.append(ch)

    return itog


def validation(tokens: list[str]) -> None:
    """проверяем выражение на корректность"""
    if len(tokens) == 0:
        raise EmptyExpressionError("Передано пустое выражение")

    # ex - expect number, ожидаем мы сейчас на вход число или нет
    # true - сейчас ожидаем на вход число,
    # false - сейчас ожидаем на вход оператор
    ex = True
    for token in tokens:
        if ex:
            if is_number(token):
                ex = False
            elif token in "-+":
                ex = True
            else:
                raise InvalidExpressionError("Неправильное выражение")
        else:
            if token in "+-*/":
                ex = True
            else:
                raise InvalidExpressionError("Неправильное выражение")
    if ex:
        raise InvalidExpressionError("Неправильное выражение")




def unary(order: list[str]) -> list[str]:
    """учитывает унарные + и -
    идет по получившейся строке с токенами и если видит унарную операцию то прибавляет знакск впередистоящему числу к которому относится эта операция"""
    if order[0] == "+":
        del order[0]
    elif order[0] == "-":
        order[1] = "-" + order[1]
        del order[0]

    i = 0
    while i < len(order) - 2:
        if order[i] in "+-/*" and order[i + 1] == "-":
            order[i + 2] = "-" + order[i + 2]
            del order[i + 1]
        elif order[i] in "+-/*" and order[i + 1] == "+":
            del order[i+1]
        i += 1
    return order


def priority(oper: str) -> int:
    """вводим приоритет операций */ над +-"""
    if oper in "+-":
        return 1
    else:
        return 2



def to_rpn(exp: list[str]) -> list[str]:
    """перевод в обратную польскую запись (алгоритм сортировочной станции дейкстра)"""
    output = []
    operators: list[str] = []

    for symbol in exp:
        if is_number(symbol):
            output.append(symbol)
        else:
            while len(operators) > 0 and priority(operators[-1]) >= priority(symbol):
                    output.append(operators.pop())
            operators.append(symbol)


    operators = operators[::-1]
    output.extend(operators)
    return output



def from_rpn(order: list[str]) -> float:
    """функция получает на вход постфиксную запись и возвращает посчитанное значение"""
    stack = []
    for el in order:
        if is_number(el):
            stack.append(float(el))
        else:
            if el == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif el == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif el == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif el == "/":
                b = stack.pop()
                a = stack.pop()
                if b != 0:
                    stack.append(a/b)
                else:
                    raise DivisionZeroError("Деление на ноль")
    return stack[0]


def calculate(expression: str) -> float:
    """итоговая сборка калькулятора"""
    tokens = tokenization(expression)
    validation(tokens)

    tokens = unary(tokens)
    dxt = to_rpn(tokens)
    result = from_rpn(dxt)

    return result

def postfix_command(expression: str) -> list[str]:
    """вывод выражение в обратной польской записи"""
    tokens = tokenization(expression)
    validation(tokens)

    tokens = unary(tokens)
    dxt = to_rpn(tokens)

    return dxt
