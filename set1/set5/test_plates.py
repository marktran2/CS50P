from plates import is_valid

def test_too_short():
    assert is_valid("a0") == False

def test_too_long():
    assert is_valid("ab12345cde") == False

def test_proper():
    assert is_valid("abc123") == True

def test_invalid():
    assert is_valid("ab123c") == False