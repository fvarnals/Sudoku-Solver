from box import Box

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
