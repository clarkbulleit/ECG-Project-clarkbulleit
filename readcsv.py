
def readcsv(file):
    """

    :param: .csv file
    :return: dictionary with lists of floats for time and voltage

    Function does not import line from file if the data type isn't float
    Prints warning with number of rows not imported because of invalid inputs
    """
    import csv
    import logging
    logging.basicConfig(filename="Main_Log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    with open(file) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        raw_data = {}
        raw_data["time"] = []
        raw_data["voltage"] = []
        nn = 0

        for row in readCSV:
            try:
                t = float(row[0])
                v = float(row[1])
                raw_data["time"].append(t)
                raw_data["voltage"].append(v)
            except ValueError:
                nn = nn + 1
                continue

        if nn != 0:
            logging.warning("Warning: " + str(nn) + ' ' +
                            "Rows with non-numeric "
                            "inputs were not imported")

    return raw_data
