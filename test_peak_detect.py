import pytest
from peak_detect import peak_detect


def test_peak_detect():
    input1 = [0, 0, 1, 2, 3, 1, 0, 3, 0]
    output1 = ([3], [4])
    input2 = [0, 0, 0, 0]
    output2 = ([], [])
    response = peak_detect(input1)
    assert output1 == response
    response = peak_detect(input2)
    assert output2 == response
