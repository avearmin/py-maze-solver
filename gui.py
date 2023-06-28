from tkinter import Tk, BOTH, Canvas
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._canvas = Canvas(self._root, width=width, height=height, background="white")
        self._is_window_running = False
        
        self._root.title("Maze Solver")
        self._canvas.pack(fill=BOTH, expand=1)
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._is_window_running = True
        while self.__is_window_running:
            self.redraw()
    
    def close(self):
        self._is_window_running = False

    def draw_line(self, line, fill_color):
        self._canvas.create_line(
            line.p1.x, line.p1.y, line.p2.x, line.p2.y, 
            fill=fill_color, width=2
            )
        self._canvas.pack()

    def draw_cell(self, cell, fill_color="black"):
        if cell.has_left_wall:
            self._canvas.create_line(
                cell.x1, cell.y1, cell.x1, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self._canvas.create_line(
                cell.x1, cell.y1, cell.x1, cell.y2,
                fill="white", width=2
            )

        if cell.has_top_wall:
            self._canvas.create_line(
                cell.x1, cell.y1, cell.x2, cell.y1,
                fill=fill_color, width=2
            )
        else:
            self._canvas.create_line(
                cell.x1, cell.y1, cell.x2, cell.y1,
                fill="white", width=2
            )

        if cell.has_right_wall:
            self._canvas.create_line(
                cell.x2, cell.y1, cell.x2, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self._canvas.create_line(
                cell.x2, cell.y1, cell.x2, cell.y2,
                fill="white", width=2
            )

        if cell.has_bottom_wall:
            self._canvas.create_line(
                cell.x1, cell.y2, cell.x2, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self._canvas.create_line(
                cell.x1, cell.y2, cell.x2, cell.y2,
                fill="white", width=2
            )

        self._canvas.pack()
    
    def draw_move(self, cell_1, cell_2, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        x1, y1 = cell_1.get_center()
        x2, y2 = cell_2.get_center()
        line = Line(
            Point(x1, y1), Point(x2, y2)
        )
        self.draw_line(line, fill_color)

    def animate(self, num):
        self.redraw()
        time.sleep(num)