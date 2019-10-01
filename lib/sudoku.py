from box import Box

class Sudoku:

    def __init__(self,size=9):
        self.boxes = {}
        for x_coord in range(1,size+1):
            for y_coord in range(1,size+1):
                self.boxes[(x_coord,y_coord)] = Box((x_coord,y_coord))
