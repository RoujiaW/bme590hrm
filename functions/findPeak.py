import numpy
from scipy import signal


def findPeak(data):
    """
    import a list of voltage to perform denoise and correlation
    :param filename: a list
    :raises ImportError:  if the logging module not found
    :returns: return a list of peak
    :rtype: list
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
        data = data - numpy.mean(data)
        b, a = signal.butter(1, [0.001, 0.6], btype='bandpass', analog=False)
        dataNew = signal.lfilter(b, a, data)
        threshold = 0.3
        maxPeakIndex = dataNew.argmax()
        samplePeak = data[maxPeakIndex - 13: maxPeakIndex + 13]
        corData = numpy.correlate(data, samplePeak, 'same')
        peakList = []
        for i in corData:
            if i > threshold * max(corData):
                peakList.append(i)
            else:
                peakList.append(0)
        logging.info("Find a list of ECG peaks")
        return peakList
    except ValueError:
        logging.error("Empty list for findPeak")
        print("Empty List is Given")
