from gui import Window
from maze import Maze
import players, threading, sys

class GameApp:
    def __init__(self):
        self.window = Window(800, 600)
        self.maze = Maze(40, 35, 13, 18, 40, 40, self.window)
        self.player_manager = players.PlayerManager(self.window, self.maze)

        self.window.start_frame.start_button.config(command=self.wrapper)
        self.window.results_frame.close_button.config(command=self.close)

        self.window._root.protocol("WM_DELETE_WINDOW", self.close)

    
        self.window.wait_for_close()

    def close(self):
        self.player_manager.terminate = True
        self.player_manager.human_stop()
        self.window._root.destroy()
        sys.exit()

    def wrapper(self):
        self.window.display_game_frame()
        self.start_game()

    def start_game(self):
        thread = threading.Thread(target=self.player_manager.computer_start, daemon=True)

        thread.start()
        self.player_manager.human_start()

        thread.join()

        self.window.display_results_frame()