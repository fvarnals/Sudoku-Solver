## Sudoku Solver

I am using this project as a practice for coding in Python, following a TDD process.

### Details
- Language - Python

- Designed to solve 9x9 'Easy' Sudoku (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

- Function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

### How to run

- Fork or clone this repo, and run using from the command line using ```python3 src```
- Follow instructions provided, to enter unsolved sudoku.
- Input can be in any format, as long as it is a list of numbers starting from the top left corner of the sudoku, following through to the bottom right (punctuation, spaces etc make no difference).

### Example Output

```
Sudoku Solved!
Solution:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

Sudoku Solved in 10 iterations
```
