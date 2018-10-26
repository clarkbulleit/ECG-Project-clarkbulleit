from readcsv import readcsv
from validate_data import validate_data, \
    DiffListLengthError, NegTimeValueError
from peak_detect import peak_detect
from time_duration import time_duration
from voltage_extremes import voltage_extremes
from count_beats import count_beats
from calc_mean_hr import calc_mean_hr
from create_dict import create_dict
from write_JSON import write_JSON
import logging


if __name__ == "__main__":
    """ Calculates 5 metrics from raw data imported from a .csv file
    
    Prompts user to input a filename. If the file cannot be found
    in the test_data folder, the user is prompted again until a 
    correct filename is entered.
    
    Attempts to read the file, if custom errors are raised, the function
    prompts the user to input a new filename. Once a file is properly
    read and validated, a log is written to Main_Log.txt.
    
    Prompts user to input window size for mean heart rate calculation.
    If the input is not an integer, the user is prompted again. A third
    wrong input will break the code.

    Beats, duration, voltage extremes are calculated. If the max voltage
    exceeds the normal range of -10 to 10 V, a warning is entered into
    the log.
    
    Num_beats and mean_hr_bpm are calculated. If the heart rate is outside
    of normal ranges or equal to zero, warnings are entered into the
    logs. 
    
    The calculated values are compiled into a dictionary called metrics and
    written into a JSON file under the same name as the input in the folder
    output_data. Once the file is properly written to the json file, a new
    message is entered into the log. 

    """
    logging.basicConfig(filename="Main_Log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
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
        logging.warning("Info: " + filename + ".csv was read and validated")
        Successful_Read = True

    try:
        user_average = int(input("Enter number of minutes used for the "
                                 "average heart rate calculation: "))
    except ValueError:
        user_average = int(input("Please enter an integer: "))

    beats = peak_detect(raw_data)
    duration = time_duration(raw_data)

    voltage_extremes = voltage_extremes(raw_data)
    if voltage_extremes[1] > 10:
        logging.warning("Warning: Voltage exceeds normal range")

    num_beats = count_beats(beats)
    mean_hr_bpm = calc_mean_hr(num_beats, duration, beats, user_average)

    if mean_hr_bpm == 0:
        logging.warning("Warning: No beats were detected")

    elif mean_hr_bpm < 30 and mean_hr_bpm != 0:
        logging.warning("Warning: The heart rate is below normal range")

    elif mean_hr_bpm > 200:
        logging.warning("Warning: The hear rate exceeds normal range")

    metrics = create_dict(mean_hr_bpm, voltage_extremes, duration,
                          num_beats, beats)
    write_JSON(metrics, filename)
    logging.warning("Info: Metrics have been written to " + filename +
                    ".json in the output_data folder")
