file = 'test_readcsv.csv'

def test_readcsv(file):
    from readcsv import readcsv
    readcsv(file)
    assert time[0] == 'Test'
