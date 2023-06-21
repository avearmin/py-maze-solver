from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__is_window_running = False
        
        self.__root.title("Maze Solver")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_window_running = True
        while self.__is_window_running:
            self.redraw()
    
    def close(self):
        self.__is_window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.__canvas, fill_color)
    
    def draw_move(self, cell_1, cell_2, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        cell_move_line = Line(cell_1.get_center(), cell_2.get_center())
        self.draw_line(cell_move_line, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, 
            fill=fill_color, width=2
            )
        canvas.pack()

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
    
    def get_center(self):
        return Point(
            (self.__x1 + self.__x2) / 2,
            (self.__y1 + self.__y2) / 2
        )

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            canvas.create_line(
                self.__x1, self.__y1, self.__x1, self.__y2,
                fill=fill_color, width=2
            )
        if self.has_top_wall:
            canvas.create_line(
                self.__x1, self.__y1, self.__x2, self.__y1,
                fill=fill_color, width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self.__x2, self.__y1, self.__x2, self.__y2,
                fill=fill_color, width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self.__x1, self.__y2, self.__x2, self.__y2,
                fill=fill_color, width=2
            )
        canvas.pack()