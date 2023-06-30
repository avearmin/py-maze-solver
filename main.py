from gui import Window
from maze import Maze
from input_handler import InputHandler
import threading

def main():
    window = Window(1600, 600)
    computer = Maze(40, 35, 13, 18, 40, 40, window, 1)
    player = Maze(800, 35, 13, 18, 40, 40, window, 1)

    threading.Thread(target=computer.solve, daemon=True).start()
    input_handler = InputHandler(window, player)
    
    window.wait_for_close()

main()