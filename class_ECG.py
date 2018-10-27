from functions import readFile
from functions import beats
from functions import voltage_extremes
from functions import peak_detect
from functions import duration
from functions import findPeak
from functions import num_beats
from functions import mean_hr_bpm
from functions import userInput
from functions import time_beats
import json


class ECG():
    """
        returns various attributes
        :param self: the name of test sample
        :type self: str
        :param self.time: the list of test time
        :param self.voltage: the list of test voltage
        :param self.voltage_extremes: tuple containing minimum and
                                        maximum lead voltages
        :param self.durationtime: time duration of the ECG strip
        :param self.num_beat:number of detected beats in the strip
        :param self.time_beat:numpy array of times when a beat occurred
        :return: different attributes
    """
    def __init__(self, filename='test'):
        self.filename = filename
        (self.time, self.voltage) = (None, None)
        self.mean_hr_bpm = None
        self.voltage_extremes = None
        self.durationtime = None
        self.num_beat = None
        self.time_beat = None
        self.peaks = [None, None]

        self.collectdata()
        self.peak()
        self.beats()
        self.mean_bpm()
        self.time_beats()
        self.min_max_voltage()
        self.duration()
        self.writejson()

    def collectdata(self):
        (self.time, self.voltage) = collectdata(self.filename)
        return self.time, self.voltage

    def peak(self):
        self.peaks = peakFind(cb)
        return self.peaks

    def mean_bpm(self):
        self.mean_hr_bpm = mean_bpm(self.peaks[1], self.time)
        return self.mean_hr_bpm

    def voltage_extremes(self):
        self.voltage_extremes = voltage_extremes(self.voltage)
        return self.voltage_extremes

    def duration(self):
        self.durationtime = duration(self.time)
        return self.durationtime

    def time_beats(self):
        self.time_beat = time_beats(self.peaks[1], self.voltage)
        return self.time_beat

    def beats(self):
        self.num_beat = beats(self.peaks[1])
        return self.num_beat

    def writejson(self):
        figures = {"mean_hr_bpm": "self.mean_hr_bpm",
                   "voltage_extremes": "self.voltage_extremes",
                   "duration": "self.durationtime",
                   "num_beat": "self.numbeat",
                   "beats": "self.time_beat"}
        a = self.filename
        b = a.replace('.csv', '.json')
        with open(b, "w") as f:
            json.dump(figures, f)
        return
