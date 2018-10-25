import numpy
import pandas
import matplotlib.pyplot as plt
from scipy import signal 


def peak_detect(data)
#  place holder for peak detect method
#  place holder for finding error type
    """
    detect the peak value and index based on processed ECG peak data
    
    :param data: data is a list of floats
    :raises ImportError:
    :raises TypeError: if data is not a list
    :raises ValueError:

    :returns: two lists: peak value and index
    """
    peak = []
    peakIndex = []
    index = 0
    step = 50
    threshold = 0.5
    for i in range(0, len(rawList), step):
        start = i - step
        end = i + step
        if start >= 0 and end <= len(rawList) - 1: 
            temp = numpy.max(rawList[start : end])
        elif start < 0:
            temp = numpy.max(rawList[0 : end])
        elif end > len(rawList) - 1: 
            temp = numpy.max(rawList[start : len(rawList) - 1])   
            
        if temp > threshold * maxPeak and index == 0:
            peak.append(temp)
            peakIndex.append(rawList.index(temp))
            index = 1
        elif temp > threshold * maxPeak and index > 0 and (temp is not peak[index]):
            if rawList.index(temp) - peakIndex[index - 1] > step * 2:
                peak.append(temp)
                peakIndex.append(rawList.index(temp))
                index = index + 1
    return peak, peakIndex
