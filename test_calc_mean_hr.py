import pytest


@pytest.mark.parametrize("a,b,expected", [
    (40, 30, 80),
])
def test_calc_mean_hr(a, b, expected):
    """
    Unit test for calc_mean_hr
    :return: Asserts that the function outputs
    the correct hr as an integer
    """
    from calc_mean_hr import calc_mean_hr

    assert calc_mean_hr(a, b) == expected


def test_calc_mean_hr_raises():
    import pytest
    from calc_mean_hr import calc_mean_hr, NoBeatsDetected

    bad_num = 0
    bad_dur = 10

    with pytest.raises(NoBeatsDetected):
        calc_mean_hr(bad_num, bad_dur)
