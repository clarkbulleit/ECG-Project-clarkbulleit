
def test_time_duration():
    """
    tests time_duration function
    :return: assertion that the function returns
    the proper values
    """
    from time_duration import time_duration

    data = {'time': [0, 1.2, 1.7, 1.9, 2], 'voltage': [1, 2,
                                                       3, 4, 5]}

    duration = time_duration(data)

    assert duration == 2
