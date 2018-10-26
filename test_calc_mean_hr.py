import pytest
import numpy as np


@pytest.mark.parametrize("a,b,c,d,expected", [
    (40, 30, np.array([1, 2]), 1, 80),
    (50, 70, np.array([1, 30, 40, 50, 70, 80]), 1, 4),
    (50, 70, np.array([1, 30, 40, 60, 70, 80]), 1, 3),
    (50, 60, np.array([1, 30, 40, 50, 70, 80]), 1, 50),
    (50, 130, np.array([1, 30, 40, 50, 121, 140]), 2, 2),
])
def test_calc_mean_hr(a, b, c, d, expected):
    from calc_mean_hr import calc_mean_hr

    assert calc_mean_hr(a, b, c, d) == expected


def test_calc_mean_hr_raises():
    """
    Unit test for calc_mean_hr
    :return: Asserts that a non numeric input raises a
    value error
    """
    import pytest
    from calc_mean_hr import calc_mean_hr

    bad_dur = 10

    bad_num = 'c'

    with pytest.raises(TypeError):
        calc_mean_hr(bad_num, bad_dur)
