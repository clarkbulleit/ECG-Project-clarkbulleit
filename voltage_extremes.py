
def voltage_extremes(data):
    """ Finds min and max of voltage ECG trace

    Args:
        :param data: Dictionary with list under key
        "voltage"

    Return:
        v_extremes: Tuple containing minimum of list in 0 index
        and maximum of list in 1 index

    """
    voltage = data["voltage"]

    v_extremes = (min(voltage), max(voltage))

    return v_extremes
