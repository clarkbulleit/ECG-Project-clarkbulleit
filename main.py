from readcsv import readcsv
from readcsv import validate_data
from processData import plot_data


if __name__ == "__main__":
            raw_data = readcsv('test_data/test_data1.csv')
            print(raw_data)
            validate_data(raw_data)
            plot_data(raw_data)
