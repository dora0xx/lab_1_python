from typing import Annotated

import typer

from toolkit.calculator import calculate, postfix_command
from toolkit.converter import convert
from toolkit.errors import ToolkitError

app = typer.Typer(
    help = "Набор консольных утилит, калькулятор и конвертер величин",
    no_args_is_help=True
)

@app.command()
def calc(
    expression: Annotated[str, typer.Argument(help = "выражение которое надо вычислить")]):
    """Вычислить выражение"""
    try:
        result = calculate(expression)
        typer.echo(result)
    except ToolkitError as error:
        typer.echo(f"Ошибка: {error}", err=True)
        raise typer.Exit(code=2)



@app.command("convert", context_settings={"ignore_unknown_options": True})
def convert_command(
    value: Annotated[float, typer.Argument(help = "числовое значение для конвертации")],
    from_unit: Annotated[str, typer.Option("--from", help = "Исходная единица измерения")],
    to_unit: Annotated[str, typer.Option("--to", help = "Итоговая единица измерения")]):
    """Конвертировать из одной величины в другую"""
    try:
        result = convert(value, from_unit, to_unit)
        typer.echo(result)
    except ToolkitError as error:
        typer.echo(f"Ошибка: {error}", err = True)
        raise typer.Exit(code = 2)

@app.command()
def postfix(
    expression: Annotated[str, typer.Argument(help = "выражение которое надо перевести в постфиксную запись")]
):
    """получить постфиксную запись выражения"""
    try:
        result = postfix_command(expression)
        typer.echo(result)
    except ToolkitError as error:
        typer.echo(f"Ошибка: {error}", err=True)
        raise typer.Exit(code=2)


if __name__ == "__main__":
    app()
