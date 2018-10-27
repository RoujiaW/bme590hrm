import pytest
from mean_hr_bpm import mean_hr_bpm


@pytest.mark.parametrize("input1, input2, input3, output", [
    (20, 12, 2, 72),
    (10, 3, 1.5, 27),
    (60, 52, 100000000, 52),
    (40, 32, "test", None),
])
def mean_hr_bpm(input1, input2, input3, output):
    response = mean_hr_bpm(input1, input2, input3)
    assert response == output
