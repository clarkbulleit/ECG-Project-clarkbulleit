
def validate_data(data):
    """

    :param data: receives input of a dictionary with lists under the keys for
    "time" and "voltage"
    :return:
    """
    t = data["time"]
    v = data["voltage"]
    exceeds_range = []

    if len(t) != len(v):
        print("the lengths are not equal")

    for x in t:
        if x < 0:
            print("negative time values present")

    for y in v:
        if y > 300:
            exceeds_range.append(y)
