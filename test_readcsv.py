
def test_readcsv():
    """
    Reads in short, known .csv file
    Asserts that reader creates correct Dictionary
    """
    from readcsv import readcsv
    raw_data = readcsv('test_readcsv.csv')

    assert raw_data == {'time': [1, 7, 1.2], 'voltage': [2, 9, 4.5]}
    assert raw_data != {'time': [1, '', 7, 'c', 1.2], 'voltage': [2, 6,
                                                                  9, 10, 4.5]}
