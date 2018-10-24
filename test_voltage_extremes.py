
def test_voltage_extremes():
    """
    unit test for voltage_extremes function
    creates input in form of dictionary
    :return: asserts that a tuple was created
    of the form (min(list), max(list))
    """
    from voltage_extremes import voltage_extremes

    data = {'time': [1, 2, 3], 'voltage': [1, 2, 3]}

    v_extremes = voltage_extremes(data)

    assert v_extremes == (1, 3)
