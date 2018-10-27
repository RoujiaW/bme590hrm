from functions.readFile import readFile
from functions.peak_detect import peak_detect
from functions.findPeak import findPeak
from functions.duration import duration
from functions.voltage_extremes import voltage_extremes
from functions.num_beats import num_beats
from functions.userInput import userInput
from functions.time_beats import time_beats
from functions.mean_hr_bpm import mean_hr_bpm
import json


class ECG():
    """
    returns various attributes
    :param self: the name of data
    :type self: string
    :param self.time: the list of test time
    :param self.voltage: the list of test voltage
    :param self.extremes: tuple containing minimum and maximum voltages
    :param self.durationTime: time duration of the ECG strip
    :param self.beatNum:number of detected beats in the strip
    :param self.beatTime:numpy array of times when a beat occurred
    :return: different attributes
    """
    def __init__(self, filename=""):
        self.filename = filename
        self.time, self.voltage = None, None
        self.mean_hr = None
        self.extremes = None
        self.durationTime = None
        self.beatNum = None
        self.beatTime = None
        self.peaks = [None, None]
        self.data()
        self.peak()
        self.min_max()
        self.duration()
        self.time_beats()
        self.beat()
        self.mean_bpm()
        self.writejson()

    def data(self):
        self.time, self.voltage = readFile(self.filename)
        return self.time, self.voltage

    def peak(self):
        temp = findPeak(self.voltage)
        self.peaks = peak_detect(temp)
        return self.peaks

    def min_max(self):
        self.extremes = voltage_extremes(self.voltage)
        return self.extremes

    def duration(self):
        self.durationTime = duration(self.time)
        return self.durationTime

    def time_beats(self):
        self.beatTime = time_beats(self.peaks[1], self.voltage)
        return self.beatTime

    def beat(self):
        self.beatNum = num_beats(self.peaks[1])
        return self.beatNum

    def mean_bpm(self):
        inputTime = userInput()
        self.mean_hr = mean_hr_bpm(self.durationTime, self.beatNum, inputTime)
        return self.mean_hr

    def writejson(self):
        metrics = {"mean_hr_bpm": str(self.mean_hr),
                   "voltage_extremes": str(self.extremes),
                   "duration": str(self.durationTime),
                   "num_beats": str(self.beatNum),
                   "time_beats": str(self.beatTime)}
        name = self.filename.replace('.csv', '.json')
        with open(name, "w") as x:
            json.dump(metrics, x)
        return
