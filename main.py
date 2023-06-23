from gui import Window
from geometry import Maze
from maze_solver import MazeSolver

def main():
    window = Window(800, 600)
       
    maze = Maze(250, 125, 30, 30, 10, 10)

    maze_solver = MazeSolver(maze)

    window.draw_maze(maze, "black")
    window.draw_route(maze_solver.route)

    window.wait_for_close()

main()