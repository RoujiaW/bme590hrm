import pytest
from voltage_extremes import voltage_extremes


@pytest.mark.parametrize("input, output", [
    ([1, 3, 12,  0, 3.5, -2], (-2, 12)),
    ([0, 3, -5, 9.6, 10], (-5, 10)),
])
def test_voltage_extremes(input, output):
    # placeholder for error message
    response = voltage_extremes(input)
    assert response == output
