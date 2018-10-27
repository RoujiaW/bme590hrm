def mainFile():
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
	from class_ecg import ECG

	signals = ECG(filename = "test_data1.csv")
	signals.writejson()


if __name__ == "__main__":
	main()
