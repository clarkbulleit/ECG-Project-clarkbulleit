import numpy as np
import pytest


@pytest.mark.parametrize("a,expected", [
    (np.array([1, 2, 3, 4]), 4),
    (np.array([1, 2]), 2),
])
def test_cound_beats(a, expected):
    """
    Unit test for count_beats function
    :return: assertion that test outputs
    correct number of elements in array
    """
    from count_beats import count_beats

    assert count_beats(a) == expected
