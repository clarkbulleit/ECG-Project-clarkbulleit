class Error(Exception):
    """Base class for other exceptions"""
    pass


class DiffVectorLengthError(Error):
    """Raised when the input value is too small"""
    pass


class NegTimeValueError(Error):
    """Raised when the input value is too large"""
    pass