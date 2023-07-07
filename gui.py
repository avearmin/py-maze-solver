from tkinter import *
import time

class StartFrame:
    def __init__(self, root, width, height):
        self.frame = Frame(root, width=width, height=height)
        self.label = Label(self.frame, text="Python Maze Race", font=("helvetica", 24))
        self.start_button = Button(self.frame, text="Start Game", font=("helvetica", 24))

        self.frame.pack()

        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

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
    def __init__(self, root, width, height):
        self.frame = Frame(root, width=width, height=height)
        self.label = Label(self.frame, font=("helvetica", 24))
        self.close_button = Button(self.frame, text="Close", font=("helvetica", 24))

        self.frame.pack()

        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.close_button.place(relx=0.5, rely=0.5, anchor=CENTER)

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self.start_frame = StartFrame(self._root, width, height)
        self.game_frame = GameFrame(self._root, width, height)
        self.results_frame = ResultsFrame(self._root, width, height)
        self._is_window_running = False
        
        self._root.geometry(f"{width}x{height}")
        self._root.resizable(False, False)
        self._root.title("Maze Solver")

        self.display_start_frame()
    
    def display_frame(self, frame):
        self.start_frame.frame.pack_forget()
        self.game_frame.frame.pack_forget()
        self.results_frame.frame.pack_forget()
        frame.frame.pack(fill="both", expand=True)
    
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

    def animate(self, num):
        self.redraw()
        time.sleep(num)