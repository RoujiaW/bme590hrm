import numpy
impot pandas
import matplotlib.pyplot as plt
from scipy import sign

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
    ""
    peak = []
    peakIndex = []
    index = 0
    step = 50
    threshold = 0.5
    for i in range(0, len(rawList) + step, step):
        start = i - step
        end = i + step 
        if start > 0 and end <= len(rawList) + 1:
            tempList = rawList[start : end]
            temp = numpy.max(tempList)
            peakIndexNum = tempList.index(temp) + start
        elif start < 0:
            tempList = rawList[0 : end]
            temp = numpy.max(tempList)
            peakIndexNum = tempList.index(temp)            
        if index == 0 and temp > threshold * maxPeak:
            peak.append(temp)
            peakIndex.append(peakIndexNum)
            index = 1
        elif index > 0 and temp > threshold * maxPeak and (peakIndexNum - peakIndex[index - 1] > step * 2):
            peak.append(temp)
            peakIndex.append(peakIndexNum)
            index = index + 1
    return peak, peakIndex
