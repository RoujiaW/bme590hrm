def num_beats(rawList):
    """
    find the number of beats in whole ECG signal
    :param filename: a list
    :raises ImportError:  if the logging module not found
    :returns: total number of entries in the list
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
        return len(rawList)
        logging.info("Run num_beats")
    except TypeError:
        print("Wrong type of input")
        logging.error("Type error for num_beats")
