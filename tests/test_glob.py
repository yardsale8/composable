from composable.glob import glob
import glob as g


def test_glob():
    all_files = g.glob('./for_glob/*')
    a_test = lambda s: (s >> glob()) == g.glob(s)
    assert a_test('./for_glob/*')
    assert a_test('./for_glob/a*')
    assert a_test('./for_glob/*_1.py')
    recursive_test = lambda s: (s >> glob(recursive = True)) == g.glob(s, recursive=True)
    assert recursive_test('./for_glob/*')
    assert recursive_test('./for_glob/a*')
    assert recursive_test('./for_glob/*_1.py')