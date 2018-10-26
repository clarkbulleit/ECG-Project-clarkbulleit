# ECG-Project-clarkbulleit
# Heart Rate Monitor


## How to Run
* Run main.py file
* Input name of file from test_data folder (ex. test_data1)
  * If the file cannot be found, input a new filename
* Input number of minutes for the window used to calculate mean heart rate
  * If the input is not an integer, type an integer
* Open JSON file in output_data folder under the same filename as the input to see the metrics

## Log Warning and Info Messages
* Warning: n Rows with non-numeric inputs were not imported
* Info: test_data.csv was read and validated
* Warning: No beats were detected: 
* Warning: The heart rate is below normal range
* Warning: The hear rate exceeds normal range
* Info: Metrics have been written to test_data.json in the output_data folder


## Functions
* readcsv.py
* validate_data.py
* peak_detect.py
* time_duration.py
* voltage_extremes.py
* count_beats.py
* calc_mean_hr.py
* create_dict.py
* write_JSON.py



