

def test_readcsv():
    from readcsv import readcsv
    raw_data = readcsv('test_readcsv.csv')
    assert raw_data["time"][0] == 1

    for x in raw_data["time"]:
        assert type(x) == float

    for y in raw_data["voltage"]:
        assert type(y) == float
