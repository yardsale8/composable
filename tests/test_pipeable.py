from composable.pipeable import pipeable

def test_pipeable_lambda():
    my_pow = pipeable(lambda x, y: x**y)
    assert callable(my_pow(3))
    assert (2 >> my_pow(3)) == my_pow(3, 2)
    assert my_pow(3)(2) == my_pow(3, 2)



def test_pipeable_decorator():
    @pipeable
    def my_pow(x, y):
        return x**y
    assert callable(my_pow(3))
    assert (2 >> my_pow(3)) == my_pow(3, 2)
    assert my_pow(3)(2) == my_pow(3, 2)