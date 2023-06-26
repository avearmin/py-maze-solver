from gui import Window
from maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(40, 35, 13, 18, 40, 40, window)
    maze.solve()
    window.wait_for_close()

main()