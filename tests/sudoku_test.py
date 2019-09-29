import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../lib')

from box import Box
box = Box((1,1))

def test_check():
    assert box.index == (1,1)
