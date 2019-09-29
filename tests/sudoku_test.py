from lib import Number
number = Number((1,1))

def test_check():
    assert number.index == (1,1)
