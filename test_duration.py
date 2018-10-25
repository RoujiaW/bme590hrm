import pytest
from duration import duration


@pytest.mark.parametrize("input, output", [
    ([1, 0, 3.5, -2], -3),
    ([0, 3, -5, 9.6, 10], 10),
])
def test_duration(input, output):
    """
    Test the duration function
    """
    response = duration(input)
    assert response == output
