import pytest


@pytest.mark.parametrize("a,expected", [
    ({'voltage': [1, 2, 3]}, (1, 3)),
    ({'voltage': [1, 2, 3, 3]}, (1, 3)),
    ({'voltage': [-1, 2, 3]}, (-1, 3)),
    ({'voltage': [-1, -3]}, (-3, -1)),
])
def test_voltage_extremes(a, expected):
    from voltage_extremes import voltage_extremes

    assert voltage_extremes(a) == expected
