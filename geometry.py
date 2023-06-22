import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Cell:
    def __init__(self, line):
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = line.p1.x
        self.__x2 = line.p2.x
        self.__y1 = line.p1.y
        self.__y2 = line.p2.y

    def get_x1(self):
        return self.__x1
    
    def get_x2(self):
        return self.__x2
    
    def get_y1(self):
        return self.__y1

    def get_y2(self):
        return self.__y2
    
    def get_center(self):
        return Point(
            (self.__x1 + self.__x2) / 2,
            (self.__y1 + self.__y2) / 2
        )
    
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            seed=0
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = self.__create_cells()
        self.seed = random.seed(0)

    def __create_cells(self):
        cells = []
        for i in range(self.num_cols):
            cells.append([])
            
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                line = Line(Point(x1, y1), Point(x2, y2))

                cells[i].append(Cell(line))

        self.__create_entrance_and_exit(cells)
        self.__create_pathways(cells)
        self.__reset_cells_visited(cells)
        return cells

    def __create_entrance_and_exit(self, cells):
        cells[0][0].has_top_wall = False
        cells[-1][-1].has_bottom_wall = False

    def __create_pathways(self, cells, i=0, j=0):
        cells[i][j].visited = True
        while True:
            next_indexs = []

            if i > 0 and not cells[i - 1][j].visited:
                next_indexs.append((i - 1, j))
            
            if i < self.num_cols - 1 and not cells[i + 1][j].visited:
                next_indexs.append((i + 1, j))
            
            if j > 0 and not cells[i][j - 1].visited:
                next_indexs.append((i, j - 1))
            
            if j < self.num_rows - 1 and not cells[i][j + 1].visited:
                next_indexs.append((i, j + 1))
            
            possible_directions = len(next_indexs)
            if possible_directions == 0:
                return
            
            direction = random.randrange(possible_directions)
            next_i, next_j = next_indexs[direction]

            if i - 1 == next_i:
                cells[i][j].has_left_wall = False
                cells[next_i][next_j].has_right_wall = False
            
            if i + 1 == next_i:
                cells[i][j].has_right_wall = False
                cells[next_i][next_j].has_left_wall = False
            
            if j - 1 == next_j:
                cells[i][j].has_top_wall = False
                cells[next_i][next_j].has_bottom_wall = False

            if j + 1 == next_j:
                cells[i][j].has_bottom_wall = False
                cells[next_i][next_j].has_top_wall = False

            self.__create_pathways(cells, next_i, next_j)
    
    def __reset_cells_visited(self, cells):
        for row in cells:
            for cell in row:
                cell.visited = False

        
