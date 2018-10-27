import numpy


def voltage_extremes(data):
    """
    import a list of data
    :param data: a list
    :raises ImportError:  if the logging module not found
    :raises ValueError:  if the input is not empty
    :returns: return a tuple including two floats
    :rtype: tuple
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    voltage_extremes = ()
    try: 
        maximum =  numpy.max(rawData)
        minimum = numpy.min(rawData)
        voltage_extremes = (minimum, maximum)
        return voltage_extremes
    except ValueError:
        print("Empty Input received")
