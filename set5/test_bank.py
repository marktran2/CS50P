from bank import value


def test_proper_greeting():
    assert value("Hello, how can I help you?") == 0

def test_partial_greeting():
    assert value("Hey, what can I help you with today?") == 20

def test_improper_greeting():
    assert value("Bonjour") == 100