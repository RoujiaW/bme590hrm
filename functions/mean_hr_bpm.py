def mean_hr_bpm(duration, num_beats, inputTime):
    """
    find mean heart rate based on user input
    :param duration: a int
    :param num_beats: a int
    :param inputTime: a string
    :raises ImportError:  if the logging module not found
    :raises ValueError:  if inputTime is not pure number
    :returns: mean heart rate based on inputTime
    :rtype: int
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
        inputTime = float(inputTime)
        if inputTime <= 0 or inputTime >= 1e+6:
            print("Time out of range. Assume 1 minute for heart rate")
            inputTime = 1
        return int(num_beats/duration * 60 * inputTime)
        logging.info("Find the mean heart rate")
    except ValueError:
        print("Please enter a number with any punctuations such as 2")
        logging.error("value error: input is not pure number")
