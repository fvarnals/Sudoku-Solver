from box import Box

class Sudoku:

    def __init__(self,list):
        self.boxes = {}
        for x_coord in range(0,9):
            for y_coord in range(0,9):
                self.boxes[(x_coord,y_coord)] = Box((x_coord,y_coord))
