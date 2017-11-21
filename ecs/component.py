class Component(object):
    screen = None
    
    def __init__(self):
        self.enabled = True
        self.game_object = None
    
    def start(self):
        pass
    
    def update(self):
        pass