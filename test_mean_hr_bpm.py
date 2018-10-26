import pytest
from mean_hr_bpm import mean_hr_bpm


"""
@pytest.mark.parametrize("input, output", [
    (test, NameError),
    ('test', FileNotFoundError),
    (1, ValueError),
])
"""
@pytest.mark.parametrize("input1, input2, output", [
    (60, 36, 36),
    (50, 40, 75),
    (42.5, 55.5, 60),
])
def test_mean_hr_bpm(input1, input2, output):
    response = mean_hr_bpm(input1, input2)
    assert response == output
