
def readcsv(file):
    import csv
    with open(file) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')

        time = []
        voltage = []

        for row in readCSV:
            t = float(row[0])
            v = float(row[1])
            time.append(t)
            voltage.append(v)

    return time, voltage


if __name__ == "__main__":
    try:
        print(readcsv('test_data/test_data1.csv'))
    except TypeError:
        print("file contains non integer values")