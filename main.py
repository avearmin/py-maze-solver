from gui import Window
from maze import Maze
import players, threading

def main():
    window = Window(800, 600)
    
    window.start_frame.start_button.config(command=lambda: wrapper(window))
    
    window.wait_for_close()


def wrapper(window):
    window.display_game_frame()
    start_game(window)

def start_game(window):
    maze = Maze(40, 35, 13, 18, 40, 40, window)
    
    player_manager = players.PlayerManager(window, maze)

    thread = threading.Thread(target=player_manager.computer_start, daemon=True)

    thread.start()
    player_manager.human_start()

    thread.join()

    window.display_results_frame()

main()