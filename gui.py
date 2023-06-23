from tkinter import Tk, BOTH, Canvas
from geometry import Line
import time

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
        self.__canvas.create_line(
            line.p1.x, line.p1.y, line.p2.x, line.p2.y, 
            fill=fill_color, width=2
            )
        self.__canvas.pack()

    def draw_cell(self, cell, fill_color):
        if cell.has_left_wall:
            self.__canvas.create_line(
                cell.get_x1(), cell.get_y1(), cell.get_x1(), cell.get_y2(),
                fill=fill_color, width=2
            )
        if cell.has_top_wall:
            self.__canvas.create_line(
                cell.get_x1(), cell.get_y1(), cell.get_x2(), cell.get_y1(),
                fill=fill_color, width=2
            )
        if cell.has_right_wall:
            self.__canvas.create_line(
                cell.get_x2(), cell.get_y1(), cell.get_x2(), cell.get_y2(),
                fill=fill_color, width=2
            )
        if cell.has_bottom_wall:
            self.__canvas.create_line(
                cell.get_x1(), cell.get_y2(), cell.get_x2(), cell.get_y2(),
                fill=fill_color, width=2
            )
        self.__canvas.pack()

    def draw_maze(self, maze, fill_color):
        for col in maze._cells:
            for cell in col:
                self.draw_cell(cell, fill_color)
    
    def draw_route(self, maze_solver_route):
        for movement in maze_solver_route:
            move_line = Line(movement.cell_1.get_center(), movement.cell_2.get_center())
            self.draw_line(move_line, "red")
            self._animate()

    def _animate(self):
        self.redraw()
        time.sleep(0.05)