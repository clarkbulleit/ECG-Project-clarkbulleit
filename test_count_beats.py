
def test_cound_beats():
    """
    Unit test for count_beats function
    :return: assertion that test outputs
    correct number of elements in array
    """
    from count_beats import count_beats
    import numpy as np

    list = np.array([1, 2, 3, 4])
    beats = count_beats(list)

    assert beats == 4
    assert beats != 3
