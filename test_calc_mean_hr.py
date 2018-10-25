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
    from calc_mean_hr import calc_mean_hr, NoBeatsDetected
    import pytest

    assert calc_mean_hr(a, b) == expected

    with pytest.raises(NoBeatsDetected):
        calc_mean_hr()
