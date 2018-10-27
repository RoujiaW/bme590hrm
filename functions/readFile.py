import pandas


def readFile(filename):
    """
    import a ECG CSV file based on the string given
    :param filename: a string
    :raises ImportError:  if the logging module not found
    :raises TypeError:  if the input is not a string
    :returns: return a list of time and a list of voltage of ECG signal
    :rtype: lists
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    time = []
    voltage = []
    if type(filename) is not str:
        raise TypeError("Please input filename as \'test_data1.csv'")
        logging.error("Wrong type of input")
    try:
        data = pandas.read_csv(filename, names=["time", "voltage"])
        time = data.time.tolist()
        voltage = data.voltage.tolist()
        logging.info("Read CSV file and retrieve time and voltage information")
    except FileNotFoundError:
        print("File doesn't exist. Please try again")
        logging.error("No file associated with this name")
    return (time, voltage)
