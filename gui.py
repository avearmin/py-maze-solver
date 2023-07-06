from tkinter import Tk, BOTH, Canvas, Frame, Button
import time, sys

class StartFrame:
    def __init__(self, root):
        self.frame = Frame(root, bg="white")
        self.start_button = Button(self.frame, text="Start Game")
        self.start_button.pack()
    
class GameFrame:
    def __init__(self, root, width, height):
        self.frame = Frame(root, bg="blue")
        self.canvas = Canvas(self.frame, width=width, height=height, background="white")
        self.canvas.pack()
    
    def draw_cell(self, cell, fill_color="black"):
        if cell.has_left_wall:
            self.canvas.create_line(
                cell.x1, cell.y1, cell.x1, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self.canvas.create_line(
                cell.x1, cell.y1, cell.x1, cell.y2,
                fill="white", width=2
            )

        if cell.has_top_wall:
            self.canvas.create_line(
                cell.x1, cell.y1, cell.x2, cell.y1,
                fill=fill_color, width=2
            )
        else:
            self.canvas.create_line(
                cell.x1, cell.y1, cell.x2, cell.y1,
                fill="white", width=2
            )

        if cell.has_right_wall:
            self.canvas.create_line(
                cell.x2, cell.y1, cell.x2, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self.canvas.create_line(
                cell.x2, cell.y1, cell.x2, cell.y2,
                fill="white", width=2
            )

        if cell.has_bottom_wall:
            self.canvas.create_line(
                cell.x1, cell.y2, cell.x2, cell.y2,
                fill=fill_color, width=2
            )
        else:
            self.canvas.create_line(
                cell.x1, cell.y2, cell.x2, cell.y2,
                fill="white", width=2
            )

        self.canvas.pack()
    
    def move_img(self, img_id, to_cell):
        x, y = to_cell.get_center()
        self.canvas.coords(img_id, x, y)

class ResultsFrame:
    def __init__(self, root):
        self.frame = Frame(root, bg="white")

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self.start_frame = StartFrame(self._root)
        self.game_frame = GameFrame(self._root, width, height)
        self.results_frame = ResultsFrame(self._root)
        self._is_window_running = False
        
        self._root.geometry(f"{width}x{height}")
        self._root.resizable(False, False)
        self._root.title("Maze Solver")

        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self.display_start_frame()
    
    def display_frame(self, frame):
        self.start_frame.frame.grid_forget()
        self.game_frame.frame.grid_forget()
        self.results_frame.frame.grid_forget()
        frame.frame.grid(row=0, column=0, sticky="nsew")
    
    def display_start_frame(self):
        self.display_frame(self.start_frame)

    def display_game_frame(self):
        self.display_frame(self.game_frame)

    def display_results_frame(self):
        self.display_frame(self.results_frame)

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

    def animate(self, num):
        self.redraw()
        time.sleep(num)