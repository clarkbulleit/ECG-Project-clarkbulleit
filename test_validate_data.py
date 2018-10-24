
def test_validate_data():
    """
    Unit test for validate_data function
    :return: proper errors for two bad inputs
    Makes sure validate_data throws DiffListLengthError
    if the two lists are not the same length
    Makes sure validate_data throws NegTimeValueError
    if the time list contains negative time values
    """
    from validate_data import validate_data, \
        DiffListLengthError, NegTimeValueError
    import pytest

    bad_input1 = {'time': [1, 1, 3], 'voltage': [1, 2]}
    bad_input2 = {'time': [-1, 1], 'voltage': [1, 2]}

    with pytest.raises(DiffListLengthError):
        validate_data(bad_input1)

    with pytest.raises(NegTimeValueError):
        validate_data(bad_input2)
