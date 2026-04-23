from app import add, subtract, multiply, average, odd_even_difference

def test_add():
    assert add(10, 3) == 13

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(7, 2) == 14

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0

def test_odd_even_difference():
    assert odd_even_difference([1,2,3,4,5,6,7,8,9,10]) == -5