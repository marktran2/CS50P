from fuel import gauge, convert


def test_X_greater():
    assert convert("5/4") == "ValueError"

def test_non_integer():
    assert convert("cat/dog") == "ValueError"

def test_division_zero():
    assert convert("4/0") == "ZeroDivisionError"

def test_empty():
    assert gauge(convert("1/100")) == "E"
    
def test_full():
    assert gauge(convert("99/100")) == "F"

def test_percentage():
    assert gauge(convert("4/5")) == "80%"