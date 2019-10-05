from box import Box
from sudoku import Sudoku

print('Please provide a 9x9 Sudoku to solve')

sudoku_input = []
row = []

numbers = input('>\n')

# iterate through input, compiling numbers into rows of 9 and appending them
# to sudoku_input
for character in numbers:
    if character.isdigit():
        row.append(int(character))
        if len(row) == 9:
            sudoku_input.append(row)
            row = []

sudoku = Sudoku(sudoku_input)

iterations = 0
while any(0 in row for row in sudoku.show):
    for box in sudoku.unresolved_values.values():
        sudoku.check_possible_values(box)
    sudoku.update_values()
    iterations += 1

print('\nSudoku Solved!\nSolution:\n')
row_number = 0
for row in sudoku.show:
    formatted_row = ''

    current_number_index = 0
    for number in row:
        current_number_index += 1
        if current_number_index == 3 or current_number_index == 6:
            formatted_row += (str(number) + ' | ')
        else:
            formatted_row += (str(number) + ' ')
    row_number += 1
    if row_number == 3 or row_number == 6:
        print(formatted_row+'\n---------------------')
    else:
        print(formatted_row)

print('\nSudoku Solved in {} iterations'.format(iterations))
