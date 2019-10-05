import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from box import Box
from sudoku import Sudoku
box = Box(2,3,0)

def test_box_row():
    assert box.row == 2

def test_box_column():
    assert box.column == 3

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
def test_sudoku_stores_unresolved_values():
    assert type(sudoku.unresolved_values) is dict

def test_get_numbers_in_row():
    box = sudoku.unresolved_values['20']
    assert sudoku.get_numbers_in_row(box) == [0,9,8,0,0,0,0,6,0]

def test_get_numbers_in_column():
    box = sudoku.unresolved_values['36']
    assert sudoku.get_numbers_in_column(box) == [0,0,0,0,0,0,2,0,0]

def test_get_subgrid():
    box = sudoku.unresolved_values['11']
    box2 = sudoku.unresolved_values['47']
    box3 = sudoku.unresolved_values['18']
    assert sudoku.get_subgrid(box) == (0,0)
    assert sudoku.get_subgrid(box2) == (1,2)
    assert sudoku.get_subgrid(box3) == (0,2)

def test_get_numbers_in_subgrid():
    box = sudoku.unresolved_values['11']
    box2 = sudoku.unresolved_values['47']
    box3 = sudoku.unresolved_values['18']
    assert sudoku.get_numbers_in_subgrid(box) == [5,3,0,6,0,0,0,9,8]
    assert sudoku.get_numbers_in_subgrid(box2) == [0,0,3,0,0,1,0,0,6]
    assert sudoku.get_numbers_in_subgrid(box3) == [0,0,0,0,0,0,0,6,0]

def test_check_possible_values():
    box = sudoku.unresolved_values['44']
    sudoku.check_possible_values(box)
    assert box.possible_values == [5]
    box = sudoku.unresolved_values['63']
    sudoku.check_possible_values(box)
    assert box.possible_values == [3,5,7]

def test_update_values():
    assert sudoku.show[4][4] == 0
    assert sudoku.show[7][7] == 0
    box = sudoku.unresolved_values['77']
    sudoku.check_possible_values(box)
    sudoku.update_values()
    assert sudoku.show[4][4] == 5
    assert sudoku.show[7][7] == 3
