import pytest

from bmi import create_parser, handle_args


@pytest.fixture
def parser():
    return create_parser()


def test_help_flag_exits(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(["-h"])


def test_no_args_exits(parser, capfd):
    args = parser.parse_args([])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_only_width_exits(parser, capfd):
    args = parser.parse_args(["-w", "80"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_only_length_exits(parser, capfd):
    args = parser.parse_args(["-l", "187"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert output.strip() == "Need both weight and length args"


def test_two_arg(parser, capfd):
    args = parser.parse_args(["-w", "80", "-l", "187"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_two_arg_reversed_order(parser, capfd):
    args = parser.parse_args(["-l", "187", "-w", "80"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 22.88" in output


def test_different_args(parser, capfd):
    args = parser.parse_args(["-l", "200", "-w", "100"])
    handle_args(args)
    output = capfd.readouterr()[0]
    assert "Your BMI is: 25.0" in output
