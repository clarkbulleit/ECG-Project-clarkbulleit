
def readcsv(file):
    """

    :param: .csv file
    :return: dictionary with lists of floats for time and voltage

    Function does not import line from file if the data type isn't float
    """
    import csv
    with open(file) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        raw_data = {}
        raw_data["time"] = []
        raw_data["voltage"] = []

        for row in readCSV:
            try:
                t = float(row[0])
                v = float(row[1])
                raw_data["time"].append(t)
                raw_data["voltage"].append(v)
            except ValueError:
                continue

    return raw_data
