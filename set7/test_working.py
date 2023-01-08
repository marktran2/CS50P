from working import convert
import pytest

def test_working_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_working_hours_with_minutes():
    assert convert("8:30 AM to 5:00 PM") == "08:30 to 17:00"

def test_sleeping_hours():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_sleeping_hours_with_minutes():
    assert convert("10:30 PM to 7:00 AM") == "22:30 to 07:00"

def test_invalid_time_1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_time_2():
    with pytest.raises(ValueError):
        convert("-1:30 AM to 13:40 PM")

def test_invalid_time_3():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_invalid_format_1():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_format_2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00PM")

def test_invalid_format_3():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00PM")