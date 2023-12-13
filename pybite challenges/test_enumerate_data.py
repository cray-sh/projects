from textwrap import dedent

from enumerate_data import enumerate_names_countries

expected_output = dedent(
    """\
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico
"""
)


def test_enumerate_names_countries(capsys):
    enumerate_names_countries()
    output = capsys.readouterr().out
    assert output == expected_output

print('test')