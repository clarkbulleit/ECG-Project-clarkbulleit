from readcsv import readcsv
from readcsv import validate_data
from processData import peak_detect


if __name__ == "__main__":
            raw_data = readcsv('test_data/test_data5.csv')
            validate_data(raw_data)
            peak_detect(raw_data, .3, .01)
