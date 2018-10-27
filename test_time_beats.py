import pytest
from time_beats import time_beats


@pytest.mark.parametrize("input1, input2, output", [
    ([0, 1, 3], [1, 2, 3, 4, 6], [1, 2, 4]),
    ([1, 3], [2, 9, 10, 12], [9, 12]),
    ([2], [2, 4, 7, 9], [7]),
])
def test_time_beats(input1, input2, output):
    response = time_beats(input1, input2)
    assert set(response) == set(output)
