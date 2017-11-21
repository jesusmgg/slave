from engine.engine import *
from pong_test.components.ball_script import BallScript


#####GAME OBJECTS##################################################
#Game controller:
controller = GameObject()
controller.add_component(EventManager())

#Ball:
ball = GameObject()

ball.add_component(Sprite())
ball.get_component(Sprite).set_image("assets/ball.gif")

ball.add_component(BallScript())
ball.get_component(BallScript).controller = controller
###################################################################


####SCENE##########################################################
#Create scene:
scene = Scene()

#Add game objects to scene:
scene.add_child(controller)
scene.add_child(ball)
###################################################################