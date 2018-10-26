
def write_JSON(metrics, filename):
    """ Writes dictionary to JSON file

    Formats the keys of the dictionary in alphabetical
    order. Writes the file with the same name as the
    input filename into the folder outpud_data.

    Args:
        :param metrics: Dictionary with appropriate metrics
        :param filename: Filename that JSON is being
        written to

    Return:
        JSON file with dictionary entered in
        alphabetic order

    """
    import json
    metrics["beats"] = metrics["beats"].tolist()
    metrics["num_beats"] = int(metrics["num_beats"])
    metrics['mean_hr_bpm'] = int(metrics['mean_hr_bpm'])

    with open('output_data/' + filename + '.json', "w") as write_file:
        json.dump(metrics, write_file, sort_keys=True, indent=4)
