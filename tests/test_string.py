import composable.string as s
import pytest

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

def test_startswith():
    S = '12345'
    assert S >> s.startswith('1')
    assert S >> s.startswith('12')
    assert S >> s.startswith(('1', '12', '23'))
    assert not (S >> s.startswith('2'))
    assert S >> s.startswith('2', start = 1)
    assert S >> s.startswith('23', start = 1)
    assert S >> s.startswith(('1', '12', '23'), start=1)
    assert not (S >> s.startswith('3', start = 1))
    with pytest.raises(TypeError, match="Cannot specify an end without also specifying start"):
        S >> s.startswith('2', end = 2)
    assert S >> s.startswith('23', start = 1, end = 3)
    assert not(S >> s.startswith('23', start = 1, end = 2))
    assert not(S >> s.startswith('234', start = 1, end = 2))


def test_join():
    # Test addapted from python source
    assert ['ab', 'pq', 'rs'] >> s.join('.') == 'ab.pq.rs'
    assert ['a', 'b', 'c', 'd'] >> s.join(' ') == 'a b c d'
    assert ('a', 'b', 'c', 'd') >> s.join('') == 'abcd'
    assert ('', 'b', '', 'd') >> s.join('') == 'bd'
    assert ('a', '', 'c', '') >> s.join('') == 'ac'
    assert ('abc',) >> s.join('a') == 'abc', 'a'
    assert ['a', 'b', 'c'] >> s.join('.') == 'a.b.c'
    for i in [5, 25, 125]:
        assert (['a' * i] * i) >> s.join('-') == ((('a' * i) + '-') * i)[:-1]
        assert (('a' * i,) * i) >> s.join('-') == ((('a' * i) + '-') * i)[:-1]
    # self.assertRaises(TypeError, '.'.s.join, ['a', 'b', 3])
    # assert >> join() == str(BadSeq1()), ' ', 'join', BadSeq1())
    # assert >> join() == 'a b c', ' ', 'join', BadSeq2())

    # self.checkraises(TypeError, ' ', 'join')
    # self.checkraises(TypeError, ' ', 'join', None)
    # self.checkraises(TypeError, ' ', 'join', 7)
    # self.checkraises(TypeError, ' ', 'join', [1, 2, bytes()])
    # try:
    #     def f():
    #         yield 4 + ""
    #     self.fixtype(' ').join(f())
    # except TypeError as e:
    #     if '+' not in str(e):
    #         self.fail('join() ate exception message')
    # else:
    #     self.fail('exception not raised')
