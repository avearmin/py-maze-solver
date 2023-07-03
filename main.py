from gui import Window
from maze import Maze
import players, threading

def main():
    window = Window(1600, 600)
    maze = Maze(40, 35, 13, 18, 40, 40, window, 1)
    
    computer = players.Computer(window, maze)
    human = players.Human(window, maze)

    threading.Thread(target=computer.solve, daemon=True).start()
    human.start()
    
    
    window.wait_for_close()

main()