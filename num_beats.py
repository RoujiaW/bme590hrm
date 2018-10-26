def num_beats(data):
    try:
        return len(data)
    except TypeError:
        print("Wrong type of input")
