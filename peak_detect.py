import numpy


def peak_detect(rawList):
    """
    import a list of processed voltage
    :param filename: a list
    :raises ImportError:  if the logging module not found
    :returns: return a list of R peaks and its index
    :rtype: lists
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    peak = []
    peakIndex = []
    index = 0
    step = 50
    threshold = 0.5
    try:
        maxPeak = numpy.max(rawList)
        for i in range(0, len(rawList) + step, step):
            start = i - step
            end = i + step
            if start > 0 and end <= len(rawList) + 1:
                tempList = rawList[start:end]
                temp = numpy.max(tempList)
                peakIndexNum = tempList.index(temp) + start
            elif start < 0:
                tempList = rawList[0:end]
                temp = numpy.max(tempList)
                peakIndexNum = tempList.index(temp)
            if index == 0 and temp > threshold * maxPeak:
                peak.append(temp)
                peakIndex.append(peakIndexNum)
                index = 1
            elif index > 0 and temp > threshold * maxPeak\
                    and (peakIndexNum - peakIndex[index - 1] > step * 2):
                peak.append(temp)
                peakIndex.append(peakIndexNum)
                index = index + 1
    except TypeError:
        print("Empty List is Given")
    return peak, peakIndex
