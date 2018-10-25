import pytest


@pytest.mark.parametrize("a,expected", [
    ({'voltage': [1, 2, 3]}, (1, 3)),
    ({'voltage': [1, 2, 3, 3]}, (1, 3)),
    ({'voltage': [-1, 2, 3]}, (-1, 3)),
    ({'voltage': [-1, -3]}, (-3, -1)),
])
def test_voltage_extremes(a, expected):
    """
    Unit test for voltage_extremes function
    creates input in form of dictionary
    :return: Asserts that a tuple was created
    of the form (min(list), max(list))
    Tests multiple max values, single negatives,
    and doule negatives
    """
    from voltage_extremes import voltage_extremes

    assert voltage_extremes(a) == expected
