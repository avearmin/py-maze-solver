from gui import Window
from maze import Maze
import players, threading

def main():
    window = Window(1600, 600)
    maze = Maze(40, 35, 13, 18, 40, 40, window, 1)
    
    player_manager = players.PlayerManager(window, maze)

    thread = threading.Thread(target=player_manager.computer_start, daemon=True)

    thread.start()
    player_manager.human_start()

    thread.join()
    
    window.wait_for_close()

main()