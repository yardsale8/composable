from composable import maybe
from toolz.curried.operator import add
from composable.strict import map


def test_with_default():
    assert (None >> maybe.with_default('a')) == 'a'
    assert ('b' >> maybe.with_default('a')) == 'b'


def test_map():
    assert None >> maybe.map(add(2)) is None
    assert 3 >> maybe.map(add(2)) == 5
    assert [1,2,None,4] >> map(maybe.map(add(2))) == [3, 4, None, 6]