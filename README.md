# bme590hrm
This software package is designed to process ECG signasl and output important parameters. It contains 9 basic functions. They are stored in the functions folder. 

To run the software, please use mainFile.py file to execute the operations. Users need to define their own filename inside this mainFile.py function, for example: "test_data20.csv". All csv files have to store under the same directory as the main.py file. 

Users are able to get a json file containing following information: mean_hr_bpm -- mean heart rate (beats per minutes)based on user input time range, duration -- total acquistion time of input ECG signal, voltage_extremes -- minimum and maximum voltages of whole ECG signal, time_beats -- estimated time points which each beat occurs, and num_beats -- total number of heart beat in the whole ECG signal. 
