def  test_method():
    x = 5
    y = 2
    #w "" ustalamy co ma się pojawic w przypadku bledu
    assert x+y == 7, "Assertion failed, Expected 7"
    assert x-y == 3, "Assertion failed, Expected 3"