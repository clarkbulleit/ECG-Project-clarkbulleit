

def test_write_JSON():
    from write_JSON import write_JSON
    import json
    metrics = {'beats': [1, 2, 3, 4], 'duration': 1, 'num_beats': [1, 2]}

    write_JSON(metrics, 'test_write_Json')

    with open('test_write_Json.json') as read_file:
        m = json.load(read_file)

    assert metrics == m
