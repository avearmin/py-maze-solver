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
            cell_size_y
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = self.__create_cells()

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

        return cells