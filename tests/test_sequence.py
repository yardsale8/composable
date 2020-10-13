from composable.pipeable import pipeable
import composable.sequence as l

def test_to_list():
    assert isinstance(l.to_list(range(5)), list) 
    assert l.to_list(range(5)) == list(range(5))
    assert range(5) >> l.to_list == list(range(5))
    assert l.to_list([]) == []
    assert [] >> l.to_list == []


def test_to_tuple():
    assert isinstance(l.to_tuple(range(5)), tuple) 
    assert l.to_tuple(range(5)) == tuple(range(5))
    assert range(5) >> l.to_tuple == tuple(range(5))
    assert l.to_tuple([]) == tuple([])
    assert [] >> l.to_tuple == tuple([])


def test_slice():
    L = list(range(5))
    assert l.slice(2, 4, L) == L[2:4]
    assert L >> l.slice(2, 4) == L[2:4]
    assert l.slice(2, 100, L) == L[2:100]

def test_join():
    start = list(map(str, range(5)))
    target = ','.join(start)
    assert l.join(',', start) == target
    assert start >> l.join(',') == target
    assert l.join(',', []) == ''
    assert [] >> l.join(',') == ''
    