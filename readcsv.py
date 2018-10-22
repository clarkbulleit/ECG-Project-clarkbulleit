
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
    t = data["time"]
    v = data["voltage"]

    if len(t) == len(v):
        print("the lengths are equal")

    for x in data["time"]:
        if type(x) != float:
            print("non float data types found in code")
        if x < 0:
            print("negative time values present")




if __name__ == "__main__":
            raw_data = readcsv('test_data/test_data31.csv')
            print(raw_data)
            validate_data(raw_data)



