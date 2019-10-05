from box import Box
from sudoku import Sudoku

print('Please provide a 9x9 Sudoku to solve')

sudoku_input = []
row = []

numbers = input('>')

# iterate through input, compiling numbers into rows of 9 and appending them
# to sudoku_input
for character in numbers:
    if character.isdigit():
        row.append(int(character))
        if len(row) == 9:
            sudoku_input.append(row)
            row = []

sudoku = Sudoku(sudoku_input)

while any(0 in row for row in sudoku.show):
    for box in sudoku.unresolved_values.values():
        sudoku.check_possible_values(box)
    sudoku.update_values()

print(sudoku.show)
