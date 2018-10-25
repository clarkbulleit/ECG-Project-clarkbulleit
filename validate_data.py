class Error(Exception):
    """Base class for other exceptions"""
    pass


class DiffListLengthError(Error):
    """Raised when the x and y lists are different lengths"""
    pass


class NegTimeValueError(Error):
    """Raised when time values are negative"""
    pass


def validate_data(data):
    """
    :param data: Dictionary with lists under keys
    "time" and "voltage"
    :return: DiffListLengthError if the time
    and voltage lists are not equal
    :return: NegTimeValueError if negative time
    values are present
    """

    if len(data["time"]) != len(data["voltage"]):
        raise DiffListLengthError

    for x in data["time"]:
        if x < 0:
            raise NegTimeValueError
