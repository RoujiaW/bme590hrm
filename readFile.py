import pandas


def fileImport(filename):
    # logging
    # import error
    data = pandas.read_csv(filename, names=["time", "voltage"])
    time = data.time.tolist()
    voltage = data.voltage.tolist()
    return time, voltage
