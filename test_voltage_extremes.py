import pytest


@pytest.mark.parametrize("a,expected", [
    ({'voltage': [1, 2, 3]}, (1, 3)),
    ({'voltage': [1, 2, 3, 3]}, (1, 3)),
    ({'voltage': [-1, 2, 3]}, (-1, 3)),
    ({'voltage': [-1, -3]}, (-3, -1)),
])
def test_voltage_extremes(a, expected):
    """
    unit test for voltage_extremes function
    creates input in form of dictionary
    :return: asserts that a tuple was created
    of the form (min(list), max(list))
    """
    from voltage_extremes import voltage_extremes

    assert voltage_extremes(a) == expected
