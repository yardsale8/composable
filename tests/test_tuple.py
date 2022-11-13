from composable.tuple import split_by
from composable.strict import map

def test_split_by():
    assert (1 >> split_by((str, float))) == ('1', 1.0)
    assert (range(3) >> map(split_by((str, float)))) == [('0', 0.0), ('1', 1.0), ('2', 2.0)]