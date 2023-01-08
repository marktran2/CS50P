from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str_empty_jar():
    jar = Jar()
    assert(str(jar)) == jar.size * "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6

def test_deposit_invalid():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_str_some_jar():
    jar = Jar()
    jar.deposit(4)
    assert(str(jar)) == 4 * "🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4

def test_withdraw_invalid():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(10)

