from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value ("hello") == 0
    assert value("Hello there") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hola") == 20

def test_otherwise():
    assert value("What's up") == 100
    assert value("Good morning") == 100
    assert value("Zebra") == 100

def test_edge_cases():
    # Ensure exact matching works correctly
    assert value("hello!") == 0
    assert value("he") == 20
    assert value("h") == 20
