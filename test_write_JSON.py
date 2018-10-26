

def test_write_JSON():
    from write_JSON import write_JSON
    import json
    import numpy as np
    metrics = {'beats': np.array([1, 2, 3, 4]), 'duration': 1,
               'num_beats': 10, 'mean_hr_bpm': 60}

    write_JSON(metrics, 'test_write_Json')

    with open('output_data/test_write_Json.json') as read_file:
        m = json.load(read_file)

    assert metrics == m
