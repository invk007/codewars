import pytest

from problems.stacks.strip_comments import strip_comments


@pytest.mark.parametrize(
    'string, markers, expected',
    [
        (
            "  '\n= avocados = lemons oranges\n! , cherries strawberries bananas avocados\ncherries pears ! # #\nwatermelons . # apples ? ,",
            ['-', '^', '#', '=', '.', '!', "'", '@', ','],
            "\n\n\ncherries pears\nwatermelons",
        ),
        (
            "apples, pears # and bananas\ngrapes\nbananas !apples",
            ['#', '!'],
            "apples, pears\ngrapes\nbananas",
        )
    ],
)
def test_strip_comments(string, markers, expected):
    assert strip_comments(string, markers) == expected
