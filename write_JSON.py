
def write_JSON(metrics, filename):
    """

    :param metrics: dictionary with appropriate metrics
    :param filename: filename that JSON is being
    written to
    :return: JSON file with dictionary entered in
    alphabetic order
    """
    import json
    metrics["beats"] = metrics["beats"].tolist()
    metrics["num_beats"] = int(metrics["num_beats"])
    metrics['mean_hr_bpm'] = int(metrics['mean_hr_bpm'])

    with open(filename + '.json', "w") as write_file:
        json.dump(metrics, write_file, sort_keys=True, indent=4)
