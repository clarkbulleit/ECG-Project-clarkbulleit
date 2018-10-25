import pytest


@pytest.mark.parametrize("a,b,expected", [
    (40, 30, 80),
    (40.25, 97.8, 25),
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

    bad_num1 = 0
    bad_dur = 10

    bad_num2 = 'c'

    with pytest.raises(NoBeatsDetected):
        calc_mean_hr(bad_num1, bad_dur)

    with pytest.raises(TypeError):
        calc_mean_hr(bad_num2, bad_dur)
