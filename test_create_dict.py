
def test_create_dict():
    from create_dict import create_dict
    import numpy as np

    mean_hr_bpm = 60
    voltage_extremes = (0, 10)
    duration = 33.5
    num_beats = 40
    beats = np.array([1, 2, 3, 4, 5])

    metrics = create_dict(mean_hr_bpm, voltage_extremes, duration, num_beats, beats)

    assert metrics == {'mean_hr_bpm': 60, 'voltage_extremes': (0, 10), 'duration': 33.5, 'num_beats': 40,
                       'beats': np.array([1, 2, 3, 4, 5])}
