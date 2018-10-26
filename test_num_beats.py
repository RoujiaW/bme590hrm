import pytest
from num_beats import num_beats


@pytest.mark.parametrize("input, output", [
    ([1, 2, 3, 4], 4),
    ([1, 3], 2),
    ([2], 1),
    ([], 0),
])
def test_num_beats(input, output):
    response = num_beats(input)
    assert response == output
