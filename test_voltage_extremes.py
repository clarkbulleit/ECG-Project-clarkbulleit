
def test_voltage_extremes():
    from voltage_extremes import voltage_extremes

    data = {'time': [1, 2, 3], 'voltage': [1, 2, 3]}

    v_extremes = voltage_extremes(data)

    assert v_extremes == (1, 3)
