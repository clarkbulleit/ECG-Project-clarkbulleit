
def readcsv(file):
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


def validate_data(data):

    if len(raw_data["time"]) == len(raw_data["voltage"]):
        print("the lengths are equal")

    for x in raw_data["time"]:
        if type(x) != float:
            print("the time values are not all floats")

if __name__ == "__main__":
            raw_data = readcsv('test_data/test_data31.csv')
            print(raw_data)
            print(len(raw_data["time"]))
            print(len(raw_data["voltage"]))




