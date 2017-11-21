from engine.engine import *


class BallScript(Component):
    def __init__(self):
        Component.__init__(self)
        
        self.controller = None  #Game controller
        
        self.speed = 10
    
    def start(self):
        Component.start(self)
        pass
    
    def update(self):
        Component.update(self)
        
        if self.controller:
            if self.controller.get_component(EventManager).get_key_down("right"):
                self.game_object.get_component(Sprite).x += self.speed
                
                print "Current X:", self.game_object.get_component(Sprite).x 
    
    