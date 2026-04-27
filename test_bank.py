from bank import value

def test_islower():
    assert value('hello, there') == 0
    assert value('howdy') == 20
    assert value('good morning, what can I help you with?') == 100

def test_capslock():
    assert value('HELLO MY FRIEND') == 0
    assert value('HOW ARE YOU?') == 20
    assert value('GOOD MORNING, NIGHT CITY!') == 100

def test_isupper():
    assert value('Hello my friend') == 0
    assert value('Hola hermanito') == 20
    assert value('What\'s up?') == 100
