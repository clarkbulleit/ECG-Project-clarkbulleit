

def test_write_JSON():
    """ Unit test for write_JSON file

    Writes a dictionary to a JSON file
    Then reads that file and asserts that
    it is equal to the original dictionary
    Especially tests that numpy arrays can
    be written to file
    """
    from write_JSON import write_JSON
    import json
    import numpy as np
    metrics = {'beats': np.array([1, 2, 3, 4]), 'duration': 1,
               'num_beats': 10, 'mean_hr_bpm': 60}

    write_JSON(metrics, 'test_write_Json')

    with open('output_data/test_write_Json.json') as read_file:
        m = json.load(read_file)

    assert metrics == m
