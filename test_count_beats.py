
def test_cound_beats():
    from count_beats import count_beats
    import numpy as np

    list = np.array([1, 2, 3, 4])
    beats = count_beats(list)

    assert beats == 4

