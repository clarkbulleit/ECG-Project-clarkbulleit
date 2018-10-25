
def time_duration(data):
    """
    :param data: Dictionary with list under
    key "time"
    :return: Duration of the time list
    """
    t = data["time"]
    duration = t[-1] - t[0]

    return duration
