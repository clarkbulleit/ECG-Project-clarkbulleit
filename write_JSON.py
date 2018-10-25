
def write_JSON(metrics, filename):
    import json
    with open(filename + '.json', "w") as write_file:
        json.dump(metrics, write_file, sort_keys=True, indent=4)
