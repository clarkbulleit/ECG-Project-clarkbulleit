

def test_readcsv():
    from readcsv import readcsv
    raw_data = readcsv('test_readcsv.csv')
    assert raw_data["time"][0] == 1
