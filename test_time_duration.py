
def test_time_duration():
    """
    Tests time_duration function
    :return: Assertion that the function returns
    the proper value for duration
    """
    from time_duration import time_duration

    data = {'time': [0.0, 1.2, 1.7, 1.9, 2.7], 'voltage': [1, 2, 3, 4, 5]}

    duration = time_duration(data)

    assert duration == 2.7
