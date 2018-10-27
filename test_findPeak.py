import pytest
import numpy
from findPeak import findPeak


def test_findPeak():
    output1 = numpy.zeros(shape=50, dtype=float)
    input1 = numpy.zeros(shape=50, dtype=float) + 1.5
    output2 = numpy.zeros(shape=300, dtype=float)
    input2 = numpy.zeros(shape=300, dtype=float) + 2
    assert set(output1) == set(findPeak(input1))
    assert set(output2) == set(findPeak(input2))
