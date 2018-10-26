
def time_duration(data):
    """ Finds time duration of ECG trace

    Args:
        :param data: Dictionary with lists under
        keys "time" and "voltage"

    Return:
        Duration: time duration of list under
        key "time"

    """
    t = data["time"]
    duration = t[-1] - t[0]

    return duration
