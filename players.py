from tkinter import PhotoImage

class Human:
    def __init__(self, window, maze):
        self.window = window
        self.maze = maze
        self.i = 0
        self.j = 0
        self.img = PhotoImage(file="images/heart.png").subsample(
            maze.cell_size_x // 2, maze.cell_size_y // 2
            )
        x, y = self.maze._cells[0][0].get_center()
        self.img_id = self.window._canvas.create_image(x, y, image=self.img)

    def start(self):
        self.window._root.bind("<KeyPress>", self.on_key_press)
        self.window._root.bind("<KeyRelease>", self.on_key_release)
        self.window._root.mainloop()

    def on_key_press(self, event):
        i = self.i
        j = self.j

        if event.keysym == "Left":
            if i > 0:
                if not self.maze._cells[i][j].has_left_wall:
                    self.window.move_img(self.img_id, self.maze._cells[i - 1][j])
                    self.i = i - 1

        if event.keysym == "Right":
            if i < self.maze.num_cols - 1:
                if not self.maze._cells[i][j].has_right_wall:
                    self.window.move_img(self.img_id, self.maze._cells[i + 1][j])
                    self.i = i + 1

        if event.keysym == "Up":
            if j > 0:
                if not self.maze._cells[i][j].has_top_wall:
                    self.window.move_img(self.img_id, self.maze._cells[i][j - 1])
                    self.j = j - 1

        if event.keysym == "Down":    
            if j < self.maze.num_rows - 1:
                if not self.maze._cells[i][j].has_bottom_wall:
                    self.window.move_img(self.img_id, self.maze._cells[i][j + 1])
                    self.maze._cells[i][j + 1].visited = True
                    self.j = j + 1
        
    def on_key_release(self, event):
        pass 

class Computer:
    def __init__(self, window, maze):
        self.window = window
        self.maze = maze
        self.img = PhotoImage(file="images/computer.png").subsample(
            maze.cell_size_x // 2, maze.cell_size_y // 2
            )
        x, y = self.maze._cells[0][0].get_center()
        self.img_id = self.window._canvas.create_image(x, y, image=self.img)
    
    def solve(self):
        return self.__solve_r()
    
    def __solve_r(self, i=0, j=0):
        self.maze._cells[i][j].visited = True
        if i == self.maze.num_cols - 1 and j == self.maze.num_rows - 1:
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

            self.window.move_img(self.img_id, self.maze._cells[next_i][next_j])
            self.window.animate(0.05)
            if self.__solve_r(next_i, next_j):
                return True
            self.window.move_img(self.img_id, self.maze._cells[next_i][next_j])
            self.window.animate(0.2)

        return False


        



