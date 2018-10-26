
def readcsv(file):
    """ Fetches columns from .csv files

    Imports .csv columns into a dictionary. Function
    excludes rows with non-numeric inputs. Logs
    number of excluded rows.

    Args:
        :param: .csv file

    Returns:
        Dictionary: lists of floats under keys "time" and "voltage"

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
