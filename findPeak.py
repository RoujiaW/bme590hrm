import numpy
from scipy import signal


def findPeak(data):
    try:
        data = data - numpy.mean(data)
        b, a = signal.butter(1, [0.001, 0.6], btype='bandpass', analog=False)
        dataNew = signal.lfilter(b, a, data)
        threshold = 0.3
        maxPeakIndex = dataNew.argmax()
        samplePeak = data[maxPeakIndex - 13:maxPeakIndex + 13]
        corData = numpy.correlate(data, samplePeak, 'same')
        peakList = []
        for i in corData:
            if i > threshold * max(corData):
                peakList.append(i)
            else:
                peakList.append(0)
        return peakList
    except ValueError:
        print("Empty List is Given")
