from tkinter import PhotoImage

class PlayerManager:
    def __init__(self, window, maze):
        self.terminate = False
        self.window = window
        self.maze = maze
        self.human = Human()
        self.computer = Computer()

        self.human.initalize(window, maze)
        self.computer.initialize(window, maze)

    def human_start(self):
        self.window._root.bind("<KeyPress>", self.on_key_press)
        self.window._root.bind("<KeyRelease>", self.on_key_release)
        self.window._root.mainloop()

    def human_stop(self):
        self.window._root.unbind("<KeyPress>")
        self.window._root.unbind("<KeyRelease>")
        self.window._root.quit()

    def stop_player_manager(self):
        self.terminate = True
        self.human_stop()

    def on_key_press(self, event):
        i = self.human.i
        j = self.human.j

        if event.keysym == "Left":
            if i > 0:
                if not self.maze._cells[i][j].has_left_wall:
                    self.window.game_frame.move_img(self.human.img_id, self.maze._cells[i - 1][j])
                    self.human.i = i - 1
                    if self.human.i == self.maze.num_cols - 1 and self.human.j == self.maze.num_rows - 1:
                        self.stop_player_manager()
                        self.window.results_frame.label.config(text="The Human Wins!")

        if event.keysym == "Right":
            if i < self.maze.num_cols - 1:
                if not self.maze._cells[i][j].has_right_wall:
                    self.window.game_frame.move_img(self.human.img_id, self.maze._cells[i + 1][j])
                    self.human.i = i + 1
                    if self.human.i == self.maze.num_cols - 1 and self.human.j == self.maze.num_rows - 1:
                        self.stop_player_manager()
                        self.window.results_frame.label.config(text="The Human Wins!")

        if event.keysym == "Up":
            if j > 0:
                if not self.maze._cells[i][j].has_top_wall:
                    self.window.game_frame.move_img(self.human.img_id, self.maze._cells[i][j - 1])
                    self.human.j = j - 1
                    if self.human.i == self.maze.num_cols - 1 and self.human.j == self.maze.num_rows - 1:
                        self.stop_player_manager()
                        self.window.results_frame.label.config(text="The Human Wins!")

        if event.keysym == "Down":    
            if j < self.maze.num_rows - 1:
                if not self.maze._cells[i][j].has_bottom_wall:
                    self.window.game_frame.move_img(self.human.img_id, self.maze._cells[i][j + 1])
                    self.human.j = j + 1
                    if self.human.i == self.maze.num_cols - 1 and self.human.j == self.maze.num_rows - 1:
                        self.stop_player_manager()
                        self.window.results_frame.label.config(text="The Human Wins!")
        
    def on_key_release(self, event):
        pass 

    def computer_start(self):
        return self.__solve_r()
    
    def __solve_r(self, i=0, j=0):
        if self.terminate:
            return
        
        self.maze._cells[i][j].visited = True
        if i == self.maze.num_cols - 1 and j == self.maze.num_rows - 1:
            self.stop_player_manager()
            self.window.results_frame.label.config(text="The Computer Wins!")
            return True

        next_indexs = []

        if i > 0 and not self.maze._cells[i - 1][j].visited and not self.maze._cells[i][j].has_left_wall:
            next_indexs.append((i - 1, j))
            
        if i < self.maze.num_cols - 1 and not self.maze._cells[i + 1][j].visited and not self.maze._cells[i][j].has_right_wall:
            next_indexs.append((i + 1, j))
            
        if j > 0 and not self.maze._cells[i][j - 1].visited and not self.maze._cells[i][j].has_top_wall:
            next_indexs.append((i, j - 1))
            
        if j < self.maze.num_rows - 1 and not self.maze._cells[i][j + 1].visited and not self.maze._cells[i][j].has_bottom_wall:
            next_indexs.append((i, j + 1))
        
        for indexs in next_indexs:
            next_i, next_j = indexs

            if self.terminate:
                return
            
            self.window.game_frame.move_img(self.computer.img_id, self.maze._cells[next_i][next_j])
            self.window.animate(0.05)
            
            if self.__solve_r(next_i, next_j):
                return True
            
            if self.terminate:
                return
            
            self.window.game_frame.move_img(self.computer.img_id, self.maze._cells[next_i][next_j])
            self.window.animate(0.2)

        return False

class Human:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.img = None
        self.img_id = None

    def initalize(self, window, maze):
        self.img = PhotoImage(file="images/heart.png").subsample(
            maze.cell_size_x // 2, maze.cell_size_y // 2
            )
        x, y = maze._cells[0][0].get_center()
        self.img_id = window.game_frame.canvas.create_image(x, y, image=self.img)

class Computer:
    def __init__(self):
        self.img = None
        self.img_id = None

    def initialize(self, window, maze):
        self.img = PhotoImage(file="images/computer.png").subsample(
            maze.cell_size_x // 2, maze.cell_size_y // 2
            )
        x, y = maze._cells[0][0].get_center()
        self.img_id = window.game_frame.canvas.create_image(x, y, image=self.img)


        



