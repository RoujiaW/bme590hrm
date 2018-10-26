def num_beats(rawList):
    try:
        return len(rawList)
    except TypeError:
        print("Wrong type of input.")
