import composable.strict as strict
from operator import add

def test_map():
    f = lambda x: x**2
    l = [ 1, 2, 3 ]
    assert strict.map(f, []) == []
    assert [] >> strict.map(f) == []
    assert strict.map(f, l) == [1, 4, 9] 
    assert l >> strict.map(f) == [1, 4, 9] 


def test_filter():
    p = lambda x: x % 2 == 1
    l = [ 1, 2, 3 ]
    m = [2, 4, 6]
    n = [1, 3, 5]
    assert strict.filter(p, []) == []
    assert [] >> strict.filter(p) == []
    assert strict.filter(p, l) == [1, 3] 
    assert l >> strict.filter(p) == [1, 3] 
    assert strict.filter(p, m) == []
    assert m >> strict.filter(p) == []
    assert strict.filter(p, n) == n
    assert n >> strict.filter(p) == n


def test_zipWith():
    l = [1,2,3,4]
    m = [5, 6, 7]
    assert strict.zipWith(l, m) == list(zip(m, l))
    assert strict.zipWith(l, []) == []
    assert strict.zipWith([], l) == []
    assert m >> strict.zipWith(l) == list(zip(m, l))
    assert [] >> strict.zipWith(l) == []
    assert l >> strict.zipWith([]) == []
    
    
def test_zipOnto():
    l = [1,2,3,4]
    m = [5, 6, 7]
    assert strict.zipOnto(l, m) == list(zip(l, m))
    assert strict.zipOnto(l, []) == []
    assert strict.zipOnto([], l) == []
    assert m >> strict.zipOnto(l) == list(zip(l, m))
    assert [] >> strict.zipOnto(l) == []
    assert l >> strict.zipOnto([]) == []


def test_enumerate():
    L = [ 1, 2, 3]
    assert strict.enumerate([]) == []
    assert strict.enumerate(L) == list(enumerate(L))
    assert L >> strict.enumerate == list(enumerate(L))

def test_star_map():
    vals = [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]
    assert (vals >> strict.star_map(add)) == [2, 4, 6, 8, 10]

def test_sorted():
    vals = [3, 2, 1, 5, 4]
    assert (vals >> strict.sorted()) == [1, 2, 3, 4, 5]
    assert (vals >> strict.sorted(reverse=True)) == [5, 4, 3, 2, 1]