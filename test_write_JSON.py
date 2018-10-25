

def test_write_JSON():
    """ Unit test for write_JSON file

    Writes a dictionary to a JSON file
    Then reads that file and asserts that
    it is equal to the original dictionary
    """
    from write_JSON import write_JSON
    import json
    metrics = {'beats': [1, 2, 3, 4], 'duration': 1, 'num_beats': [1, 2]}

    write_JSON(metrics, 'test_write_Json')

    with open('test_write_Json.json') as read_file:
        m = json.load(read_file)

    assert metrics == m
