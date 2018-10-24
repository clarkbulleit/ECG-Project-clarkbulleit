
def test_validate_data():
    from validate_data import validate_data
    from validate_data import DiffListLengthError
    from validate_data import NegTimeValueError
    import pytest

    bad_input = {'time': [1, -1, 3], 'voltage': [1, 2]}

    with pytest.raises(DiffListLengthError):
        validate_data(bad_input)

    with pytest.raises(NegTimeValueError):
        validate_data(bad_input)
