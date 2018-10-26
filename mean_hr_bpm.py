def mean_hr_bpm(duration, num_beats):
    inputTime = 0
    try:
        while inputTime <= 0:
            inputTime = input("Time range in minutes (>0) for heart rate: ")
            inputTime = float(inputTime)
        return int(num_beats/duration * 60 * inputTime)
    except ValueError:
        print("Please enter a number with any punctuations such as 2")
