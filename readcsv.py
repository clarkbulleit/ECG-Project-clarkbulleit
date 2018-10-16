import csv

file = 'test_data/test_data1.csv'


def readcsv(file):
    """

    :param file: csv file
    :return: lists compiled from csv file

    """


with open(file) as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    times = []
    voltages = []

    for row in readCSV:
        times.append(row[0])
        voltages.append(row[1])
