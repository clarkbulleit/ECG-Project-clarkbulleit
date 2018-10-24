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

    :param data: dictionary with lists under the keys for
    "time" and "voltage"
    :return:
    """
    t = data["time"]
    v = data["voltage"]
    exceeds_range = []

    if len(t) != len(v):
        raise DiffListLengthError

    for x in t:
        if x < 0:
            raise NegTimeValueError
