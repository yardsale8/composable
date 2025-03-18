import composable.dict as d
from composable.strict import map

def test_split_by():
    fs = {'s':str, 'f': float}
    assert (1 >> d.split_by(fs)) == {'s': '1', 'f': 1.0}
    assert (range(3) >> map(d.split_by(fs))) == [{'s': '0', 'f': 0.0}, {'s': '1', 'f': 1.0}, {'s': '2', 'f': 2.0}]