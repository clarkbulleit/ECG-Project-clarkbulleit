
def test_calc_mean_hr():
    """
    Unit test for calc_mean_hr
    :return: Asserts that the function outputs
    the correct hr as an integer
    """
    from calc_mean_hr import calc_mean_hr

    num_beats = 50
    duration = 30.2

    mean_hr_bpm = calc_mean_hr(num_beats, duration)

    assert mean_hr_bpm == 99
