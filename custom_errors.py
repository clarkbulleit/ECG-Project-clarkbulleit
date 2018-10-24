class Error(Exception):
    """Base class for other exceptions"""
    pass


class DiffListLengthError(Error):
    """Raised when the x and y lists are different lengths"""
    pass


class NegTimeValueError(Error):
    """Raised when time values are negative"""
    pass