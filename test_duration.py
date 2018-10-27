import pytest
from functions.duration import duration


def test_duration():
    input1 = [1, 0, 2.4, -2]
    output1 = -3
    input2 = [0, 3, -5, 9.7, 19]
    output2 = 19
    input3 = 1
    input4 = "badInput"
    assert duration(input1) == output1
    assert duration(input2) == output2
    with pytest.raises(TypeError):
        duration(input3)
    with pytest.raises(TypeError):
        duration(input4)
