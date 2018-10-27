def duration(rawData):
    """
    import a list of time points from ECG
    :param rawData: a list
    :raises ImportError:  if the logging module not found
    :raises IndexError: if a empty list is given
    :raises TypeError: if the input is not a list
    :returns: return the time difference
    :rtype: float
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    if type(rawData) is not list:
        raise TypeError("Input type is not list")
        logging.error("Wrong input type for duration")
    try:
        return rawData[len(rawData) - 1] - rawData[0]
        logging.info("Return duration successfully")
    except IndexError:
        print("List is empty. Index out of range")
