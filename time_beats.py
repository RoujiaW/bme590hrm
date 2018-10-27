def time_beats(peakIndex, time):
    """
    find the time series for a beat
    :param peakIndex: the input of peak index
    :param time: the input of time range
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string
    :returns: return a tuple include minimum and maximum of the list
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
        interval = numpy.zeros(shape=(len(peakIndex) - 1), dtype=float)
        for i in range(len(peakIndex)-1):
            timePoint = time[peakIndex[i + 1]] - time[peakIndex[i]]
            interval[i] = timePoint
        logging.info("Returning numpy array include time series")
        return interval
    except ValueError:
        print("Empty list is given.")
