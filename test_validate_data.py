
def test_validate_data():
    from validate_data import validate_data, \
        DiffListLengthError, NegTimeValueError
    import pytest

    bad_input1 = {'time': [1, 1, 3], 'voltage': [1, 2]}
    bad_input2 = {'time': [-1, 1], 'voltage': [1, 2]}

    with pytest.raises(DiffListLengthError):
        validate_data(bad_input1)

    with pytest.raises(NegTimeValueError):
        validate_data(bad_input2)
