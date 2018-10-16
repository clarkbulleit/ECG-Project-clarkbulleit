import csv


def readcsv(file):

    """
    :param file: insert name of file
    :return: strings with info from files
    """


with open('test_data1.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    times = []
    voltages = []

    for row in readCSV:
        time = row[0]
        voltage = row[1]

        times = times.append(time)
        voltages = voltages.append(voltage)
