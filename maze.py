import random

class Cell:
    def __init__(self, x1, x2, y1, y2):
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def get_center(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2
        
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window, 
            seed
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._window = window
        self.seed = random.seed(seed)
        self._cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            
            for j in range(self.num_rows):
                cell = self.__create_cell(i, j)
                self._cells[i].append(cell)
                self._window.draw_cell(cell)

        self.__create_entrance_and_exit()
        self.__create_pathways()
        self.__reset_cells_visited()

    def __create_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        return Cell(x1, x2, y1, y2)

    def __create_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._window.draw_cell(self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._window.draw_cell(self._cells[-1][-1])

    def __create_pathways(self, i=0, j=0):
        self._cells[i][j].visited = True
        while True:
            next_indexs = []

            if i > 0 and not self._cells[i - 1][j].visited:
                next_indexs.append((i - 1, j))
            
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_indexs.append((i + 1, j))
            
            if j > 0 and not self._cells[i][j - 1].visited:
                next_indexs.append((i, j - 1))
            
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_indexs.append((i, j + 1))
            
            possible_directions = len(next_indexs)
            if possible_directions == 0:
                self._window.draw_cell(self._cells[i][j])
                return
            
            direction = random.randrange(possible_directions)
            next_i, next_j = next_indexs[direction]

            if i - 1 == next_i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            
            if i + 1 == next_i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            
            if j - 1 == next_j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False

            if j + 1 == next_j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            self.__create_pathways(next_i, next_j)
    
    def __reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False