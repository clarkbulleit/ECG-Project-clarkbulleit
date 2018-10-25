
def test_calc_mean_hr():
    """
    Unit test for calc_mean_hr
    :return: Asserts that the function outputs
    the correct hr as an integer
    """
    from calc_mean_hr import calc_mean_hr, NoBeatsDetected
    import pytest

    num_beats = 50
    duration = 30.2
    bad_num = 0

    assert calc_mean_hr(num_beats, duration) == 99

    with pytest.raises(NoBeatsDetected):
        calc_mean_hr(bad_num, duration)
