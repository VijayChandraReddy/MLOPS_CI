import pytest

def square(n):
    return n**2
def cube(n):
    return n**3
def fivth(n):
    return n**5

def test_square():
    assert square(2) == 4 , 'square of 2 must be 4'
    assert square(3) == 9 , 'square of 3 must be 9'

def test_cube():
    assert cube(2) == 8 , 'cube of 2 must be 8'
    assert cube(3) == 27 , 'cube of 3 must be 27'

def test_fivth():
    assert fivth(2) == 32 , 'fivth of 2 must be 32'
    assert fivth(3) == 243 , 'fivth of 3 must be 243'

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
