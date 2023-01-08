from numb3rs import validate
import pytest

def test_format_1():
    assert validate("1.2.3.4") == True
def test_format_2():
    assert validate("1.2.3") == False
def test_format_3():
    assert validate("1.2") == False
def test_format_4():
    assert validate("1") == False


def test_range_1():
    assert validate("1000.255.255.255") == False
def test_range_2():
    assert validate("255.1000.255.255") == False
def test_range_3():
    assert validate("255.255.1000.255") == False
def test_range_4():
    assert validate("255.255.255.1000") == False
def test_range_5():
    assert validate("255.255.255.255") == True