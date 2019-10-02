import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from box import Box
from sudoku import Sudoku
box = Box((2,2))

def test_box_index():
    assert box.index == (2,2)
    # assert box.possibilities == []

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku = Sudoku(puzzle)
def test_sudoku_has_box():
    assert sudoku.boxes[(1,1)].index == (1,1)
    assert sudoku.boxes[(3,7)].index == (3,7)

def test_box_values():
    assert sudoku.boxes[(0,0)].possible_values == [5]
    assert sudoku.boxes[(8,8)].possible_values == [9]

def test_get_numbers_in_row():
    box = sudoku.boxes[(4,4)]
    assert sudoku.get_numbers_in_row(box) == [4,0,0,8,0,3,0,0,1]

def test_get_numbers_in_column():
    box = sudoku.boxes[(4,4)]
    assert sudoku.get_numbers_in_column(box) == [7,9,0,6,0,2,0,1,8]

def test_get_subgrid():
    box = sudoku.boxes[(4,4)]
    box2 = sudoku.boxes[(0,0)]
    assert sudoku.get_subgrid(box) == (1,1)
    assert sudoku.get_subgrid(box2) == (0,0)

def test_get_numbers_in_subgrid():
    box = sudoku.boxes[(4,4)]
    assert sudoku.get_numbers_in_subgrid(box) == [0,6,0,8,0,3,0,2,0]
    box2 = sudoku.boxes[(0,0)]
    assert sudoku.get_numbers_in_subgrid(box2) == [5,3,0,6,0,0,0,9,8]
