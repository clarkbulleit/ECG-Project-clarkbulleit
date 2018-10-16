
def readcsv(file, num):
    import csv
    with open(file) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        rawdata = {}
        rawdata["time"] = []
        rawdata["voltage"] = []

        for row in readCSV:
            t = float(row[0])
            v = float(row[1])
            rawdata["time"].append(t)
            rawdata["voltage"].append(v)

    return rawdata


if __name__ == "__main__":
        readcsv('test_data/test_data1.csv', 1)
