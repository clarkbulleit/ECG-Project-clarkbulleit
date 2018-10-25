
def write_JSON(metrics, filename):
    import json
    with open(filename + '.json', "w") as write_file:
        json.dump(metrics, write_file, sort_keys=True, indent=4)


if __name__ == "__main__":
    metrics = {'num_beats': (1, 2), 'beats': [1, 2, 3, 4], 'duration': 1}
    write_JSON(metrics, 'firstJSON')