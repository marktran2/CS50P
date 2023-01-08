from seasons import calculate_time
import pytest

def test_input_format():
    with pytest.raises(SystemExit):
        calculate_time("December 31, 2003")

def test_one_year_ago():
    assert calculate_time("2021-12-31") == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years_ago():
    assert calculate_time("2020-12-31") == "One million, fifty-one thousand, two hundred minutes"