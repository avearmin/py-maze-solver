class InputHandler:
    def __init__(self, window, maze):
        self.window = window
        self.maze = maze
        self.i = 0
        self.j = 0

        self.window._root.bind("<KeyPress>", self.on_key_press)
        self.window._root.bind("<KeyRelease>", self.on_key_release)
        self.window._root.mainloop()

    def on_key_press(self, event):
        i = self.i
        j = self.j
        self.window.draw_cell(self.maze._cells[i][j], "blue")
        if event.keysym == "Left":
            if i > 0:
                if not self.maze._cells[i][j].has_left_wall:
                    if not self.maze._cells[i - 1][j].visited:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i - 1][j])
                        self.maze._cells[i - 1][j].visited = True
                        self.i = i - 1
                    else:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i - 1][j], True)
                        self.maze._cells[i - 1][j].visited = False
                        self.i = i - 1

        if event.keysym == "Right":
            if i < self.maze.num_cols - 1:
                if not self.maze._cells[i][j].has_right_wall:
                    if not self.maze._cells[i + 1][j].visited:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i + 1][j])
                        self.maze._cells[i + 1][j].visited = True
                        self.i = i + 1
                    else:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i + 1][j], True)
                        self.maze._cells[i + 1][j].visited = False
                        self.i = i + 1

        if event.keysym == "Up":
            if j > 0:
                if not self.maze._cells[i][j].has_top_wall:
                    if not self.maze._cells[i][j - 1].visited:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i][j - 1])
                        self.maze._cells[i][j - 1].visited = True
                        self.j = j - 1
                    else:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i][j - 1], True)
                        self.maze._cells[i][j - 1].visited = False
                        self.j = j - 1

        if event.keysym == "Down":    
            if j < self.maze.num_rows - 1:
                if not self.maze._cells[i][j].has_bottom_wall:
                    if not self.maze._cells[i][j + 1].visited:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i][j + 1])
                        self.maze._cells[i][j + 1].visited = True
                        self.j = j + 1
                    else:
                        self.window.draw_move(self.maze._cells[i][j], self.maze._cells[i][j + 1], True)
                        self.maze._cells[i][j + 1].visited = False
                        self.j = j + 1
        
    def on_key_release(self, event):
        pass 

