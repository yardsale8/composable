import composable.string as s

def test_split():
    start = ', '.join(map(str, range(5)))
    end = list(map(str, range(5)))
    assert s.split(', ', start) == end
    assert start >> s.split(', ') == end
    assert s.split(', ', '') == ['']
    assert '' >> s.split(', ') == ['']

def test_split_re():
    start = ', '.join(map(str, range(5)))
    end = list(map(str, range(5)))
    assert s.split_re(', ')(start) == end
    assert start >> s.split_re(', ') == end
    assert s.split_re(', ')('') == ['']
    assert '' >> s.split_re(', ') == ['']

def test_replace():
    assert 'abc' >> s.replace('b', 'c') == 'acc'
    assert 'aaaabbbcc' >> s.replace('b', 'c', count=2) == 'aaaaccbcc'