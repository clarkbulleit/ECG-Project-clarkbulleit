

def test_readcsv():
    from readcsv import readcsv
    raw_data = readcsv('test_readcsv.csv')
    t = raw_data["time"]
    v = raw_data["voltage"]

    assert t[0] == 1
    assert len(t) == 2

    for x in t:
        assert type(x) == float

    for y in v:
        assert type(y) == float