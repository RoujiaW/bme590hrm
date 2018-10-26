import pandas


def fileImport(filename):
    time = []
    voltage = []
    try:
        data = pandas.read_csv(filename, names=["time", "voltage"])
        time = data.time.tolist()
        voltage = data.voltage.tolist()
    except FileNotFoundError:
        print("No file found. Please try again")
    except NameError:
        print("Please input filename is this format: \'test1.csv'")
    except ValueError:
        print("Please input filenames as string")
    return time, voltage
