from box import Box
import numpy as np

class Sudoku:

    def __init__(self,list):
        self.boxes = {}
        self.list = list

        # set up hash of all number boxes
        for x in range(0,9):
            for y in range(0,9):
                self.boxes[(x,y)] = Box((x,y))

                # if value is already provided, assign that value to given box
                if list[x][y] != 0:
                    self.boxes[(x,y)].possible_values = [list[x][y]]

    def get_numbers_in_row(self,box):
        # get list of numbers in same row as box
        row_index = box.index[0]
        row = self.list[row_index]
        return row

    def get_numbers_in_column(self,box):
        # get list of numbers same column as box
        column_index = box.index[1]
        column = []
        for row in self.list:
            column.append(row[column_index])
        return column

    def get_subgrid(self,box):
        # get subgrid of given box (0 indexed with coordinates (x,y))
        row_index = box.index[0]
        column_index = box.index[1]
        if row_index/3 < 1:
            subgrid_x = 0
        elif 1 <= row_index/3 < 2:
            subgrid_x = 1
        else:
            subgrid_x = 2

        if column_index/3 < 1:
            subgrid_y = 0
        elif 1 <= column_index/3 < 2:
            subgrid_y = 1
        else:
            subgrid_y = 2
        return (subgrid_x,subgrid_y

        )

    def get_numbers_in_subgrid(self,box):
        subgrid = self.get_subgrid(box)
        subgrid_numbers = []
        if subgrid[0] == 0:
            rows = [0,1,2]
        elif subgrid[0] == 1:
            rows = [3,4,5]
        else:
            rows = [6,7,8]

        if subgrid[1] == 0:
            cols = [0,1,2]
        elif subgrid[1] == 1:
            cols = [3,4,5]
        else:
            cols = [6,7,8]

        for row in rows:
            for col in cols:
                subgrid_numbers.append(self.list[row][col])

        return subgrid_numbers

    def check_possible_values(self,box):
      row = self.get_numbers_in_row(box)
      column = self.get_numbers_in_column(box)
      subgrid = self.get_numbers_in_subgrid(box)
      for number in range(1,10):
          if not number in row and not number in column and number not in subgrid:
              box.possible_values.append(number)
