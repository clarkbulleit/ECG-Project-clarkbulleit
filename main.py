from readcsv import readcsv
from readcsv import validate_data
from processData import peak_detect


if __name__ == "__main__":
            raw_data = readcsv('test_data/test_data1.csv')
            print(raw_data)
            validate_data(raw_data)
            peak_detect(raw_data, .5, 1)
