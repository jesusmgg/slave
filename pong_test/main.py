from engine.engine import *

from pong_test.scenes import scene_main


GAME_TITLE = "Slave Engine test program | Press ESC to exit"
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
INITIAL_SCENE = scene_main.scene


start_game(INITIAL_SCENE,
           screen_width=SCREEN_WIDTH,
           screen_height=SCREEN_HEIGHT,
           game_title=GAME_TITLE)
