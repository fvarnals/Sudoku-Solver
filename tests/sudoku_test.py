import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../lib')

from box import Box
from sudoku import Sudoku
box = Box((2,2))

def test_box_index():
    assert box.index == (2,2)
    # assert box.possibilities == []

sudoku = Sudoku()
def test_sudoku_has_box():
    assert sudoku.box.index == (1,2)
