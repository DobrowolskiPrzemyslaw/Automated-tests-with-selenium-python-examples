import pytest

def  test_random():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed, Expected 7 but was " + str(x+y)
    assert x-y == 3, "Assertion failed, Expected 2 but was " + str(x-y)

def  test_random2():
    x = 5
    y = 2
    assert x+y == 8, "Assertion failed, Expected 7 but was " + str(x+y)
    assert x-y == 1, "Assertion failed, Expected 2 but was " + str(x-y)

def test_random3():
    x = 5
    y = 2
    assert x + y == 8, "Assertion failed, Expected 7 but was " + str(x + y)
    assert x - y == 2, "Assertion failed, Expected 2 but was " + str(x - y)