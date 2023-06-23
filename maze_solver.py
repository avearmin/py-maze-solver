class Movement:
    def __init__(self, cell_1, cell_2):
        self.cell_1 = cell_1
        self.cell_2 = cell_2

class MazeSolver:
    def __init__(self, maze):
        self.route = []
        self.solve(maze)
        self.route.reverse()
    
    def solve(self, maze):
        return self.__solve_r(maze)
    
    def __solve_r(self, maze, i=0, j=0):
        maze._cells[i][j].visited = True
        if i == maze.num_cols - 1 and j == maze.num_rows - 1:
            return True

        next_indexs = []

        if i > 0 and not maze._cells[i - 1][j].visited and not maze._cells[i][j].has_left_wall:
            next_indexs.append((i - 1, j))
            
        if i < maze.num_cols - 1 and not maze._cells[i + 1][j].visited and not maze._cells[i][j].has_right_wall:
            next_indexs.append((i + 1, j))
            
        if j > 0 and not maze._cells[i][j - 1].visited and not maze._cells[i][j].has_top_wall:
            next_indexs.append((i, j - 1))
            
        if j < maze.num_rows - 1 and not maze._cells[i][j + 1].visited and not maze._cells[i][j].has_bottom_wall:
            next_indexs.append((i, j + 1))
        
        for indexs in next_indexs:
            next_i, next_j = indexs
            movement = Movement(maze._cells[i][j], maze._cells[next_i][next_j])

            if self.__solve_r(maze, next_i, next_j):
                self.route.append(movement)
                return True

        return False