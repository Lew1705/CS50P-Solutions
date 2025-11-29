import pytest
from fuel import convert, gauge



def test_convert_normal():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_values():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/")
    with pytest.raises(ValueError):
        convert("/3")
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"
    assert gauge(2) == "2%"
