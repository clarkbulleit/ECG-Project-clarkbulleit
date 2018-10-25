from readcsv import readcsv
from validate_data import validate_data, \
    DiffListLengthError, NegTimeValueError
from peak_detect import peak_detect
from time_duration import time_duration
from voltage_extremes import voltage_extremes
from count_beats import count_beats
from calc_mean_hr import calc_mean_hr, NoBeatsDetected
from create_dict import create_dict
from write_JSON import write_JSON
import logging


if __name__ == "__main__":
    """ Takes user inputted .csv file 
        Outputs metrics from ECG data
    """
    Successful_Read = False

    while Successful_Read is False:
        filename = input("Enter filename: ")

        try:
            raw_data = readcsv('test_data/' + filename + '.csv')
        except FileNotFoundError:
            print("File not found, enter new filename")
            continue

        try:
            validate_data(raw_data)
        except DiffListLengthError:
            print("File contains lists of different lengths, "
                  "enter new filename")
            continue
        except NegTimeValueError:
            print("File contains negative time values, "
                  "enter new filename")
            continue
        Successful_Read = True

    beats = peak_detect(raw_data)
    duration = time_duration(raw_data)
    voltage_extremes = voltage_extremes(raw_data)
    num_beats = count_beats(beats)

    try:
        mean_hr_bpm = calc_mean_hr(num_beats, duration)
    except NoBeatsDetected:
        logging.basicConfig(filename='Main_Log.log', level=logging.DEBUG)
        logging.warning("No beats were detected")
        mean_hr_bpm = 0

    metrics = create_dict(mean_hr_bpm, voltage_extremes, duration,
                          num_beats, beats)
    write_JSON(metrics, filename)
