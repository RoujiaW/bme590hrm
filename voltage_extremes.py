import numpy


def voltage_extremes(data):
    # type error
    # value error
    maximum = numpy.max(data)
    minimum = numpy.min(data)
    voltage_extremes = (minimum, maximum)
    return voltage_extremes
