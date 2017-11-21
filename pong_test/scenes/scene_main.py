from engine.engine import *
from pong_test.components.ball_script import BallScript
from pong_test.components.game_controller_script import GameControllerScript


# ####GAME OBJECTS##################################################
# Game controller:
controller = GameObject()
controller.add_component(EventManager())
controller.add_component(GameControllerScript())

# Ball:
ball = GameObject()

ball.add_component(Sprite())
ball.get_component(Sprite).set_image("assets/ball.gif")

ball.add_component(BallScript())
ball.get_component(BallScript).controller = controller
# ##################################################################


# ###SCENE##########################################################
# Create scene:
scene = Scene()

# Add game objects to scene:
scene.add_child(controller)
scene.add_child(ball)
# ##################################################################
