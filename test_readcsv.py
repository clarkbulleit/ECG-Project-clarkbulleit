file = 'test_readcsv.csv'

def test_readcsv(file):
    from readcsv import readcsv
    readcsv(file)
    assert times[0] == 'Test'
