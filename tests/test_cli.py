from typer.testing import CliRunner

from toolkit.__main__ import app

runner = CliRunner()

def test_calc_cli():
    result = runner.invoke(app, ["calc", "2 + 3 * 4"])
    assert result.exit_code == 0
    assert "14.0" in result.stdout


def test_convert_cli():
    result = runner.invoke(
        app,
        ["convert", "100", "--from", "cm", "--to", "m"],
    )
    assert result.exit_code == 0
    assert "1.0" in result.stdout


def test_calc_cli_division_by_zero():
    result = runner.invoke(app, ["calc", "10 / 0"])
    assert result.exit_code == 2
    assert "Деление на ноль" in result.stderr

def test_converter_cli_absolute_zero():
    result = runner.invoke(app, ["convert", "-300", "--from", "c", "--to", "f"])
    assert result.exit_code == 2
    assert "Температура ниже абсолютного нуля недопустима" in result.stderr
