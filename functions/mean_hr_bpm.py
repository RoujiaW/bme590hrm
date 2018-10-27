def mean_hr_bpm(duration, num_beats, inputTime):
    try:
        inputTime = float(inputTime)
        if inputTime <= 0 or inputTime >= 1e+6:
            print("Time out of range. Assume 1 minute for heart rate")
            inputTime = 1
        return int(num_beats/duration * 60 * inputTime)
    except ValueError:
        print("Please enter a number with any punctuations such as 2")
