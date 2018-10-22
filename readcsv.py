
def readcsv(file):
    import csv
    import numpy as np
    with open(file) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        raw_data = {}
        raw_data["time"] = []
        raw_data["voltage"] = []

        for row in readCSV:
            t = float(row[0])
            v = float(row[1])
            raw_data["time"].append(t)
            raw_data["voltage"].append(v)

        np.array(raw_data["time"])
        np.array(raw_data["voltage"])

    return raw_data

def validate_data(raw_data):
    time = np.array(raw_data["time"])

if __name__ == "__main__":
        print(readcsv('test_data/test_data1.csv'))
