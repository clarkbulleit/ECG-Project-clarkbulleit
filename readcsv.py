import csv


with open('test_data/test_data1.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    times = []
    voltages = []

    for row in readCSV:
        times.append(row[0])
        voltages.append(row[1])
