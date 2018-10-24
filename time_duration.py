
def time_duration(data):
    """

    :param data: dictionary with list under
    key "time"
    :return: duration of the time list
    """
    t = data["time"]
    duration = t[-1] - t[0]

    return duration
