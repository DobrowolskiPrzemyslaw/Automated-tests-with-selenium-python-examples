def  test_method():
    x = 5
    y = 2
    #assert aktualny_wynik = oczekiwany_wynik
    assert x+y == 7, "Assertion failed, Expected 7 but was " + str(x+y)
    assert x-y == 2, "Assertion failed, Expected 2 but was " + str(x-y)