import numpy


def time_beats(peakIndex, time):
    """
    find the time series for a beat
    :param peakIndex: the input of peak index
    :param time: the input of time range
    :raises ImportError:  if the logging  not found
    :raises ValueError: if the input is empty
    :returns: return a list of time
    :rtype: numpy array
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    try:
        interval = numpy.zeros(shape=(len(peakIndex)), dtype=float)
        for i in range(len(peakIndex)):
            timePoint = time[peakIndex[i]]
            interval[i] = timePoint
        logging.info("Returning numpy array include time series")
        return interval
    except ValueError:
        print("Empty list is given.")
        logging.error("Empty input and output")
