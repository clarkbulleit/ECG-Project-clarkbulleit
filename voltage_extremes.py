
def voltage_extremes(data):
    """
    :param data: Dictionary with list under key
    "voltage"
    :return: Tuple containing minimum of list in 0 index
    and maximum of list in 1 index
    """
    voltage = data["voltage"]

    v_extremes = (min(voltage), max(voltage))

    return v_extremes
