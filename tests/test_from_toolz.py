from composable import from_toolz as tlz


def test_get():
    assert range(5) >> tlz.get(2) == 2