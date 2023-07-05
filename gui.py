from tkinter import Tk, BOTH, Canvas
import time, sys

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
        while self._is_window_running:
            self.redraw()
    
    def close(self):
        self._is_window_running = False
        self._root.destroy()
        sys.exit()

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
    
    def move_img(self, img_id, to_cell):
        x, y = to_cell.get_center()
        self._canvas.coords(img_id, x, y)

    def animate(self, num):
        self.redraw()
        time.sleep(num)