def mainFile():
    from ECG_class import ECG
    signals = ECG(filename="test_data1.csv")
    signals.writejson()


if __name__ == "__main__":
    mainFile()
