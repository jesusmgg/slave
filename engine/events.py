import pygame
import pygame.locals

from ecs.component import Component


class EventType(object):
    quit = 1
    
    key_down = 2
    key_up = 3
    
    mouse_down = 4
    mouse_up = 5
    mouse_motion = 6
    

class Event(object):
    def __init__(self):
        self.type = None
        self.data = None
        
        #Data:
        #- Quit: no data
        #- Key down and up: key, modifier
        #- Mouse down and up: button, position
        #- Mouse motion: buttons, position, relative movement (from previous position)
        
        #Examples:
        #- Key down: "a", "ctrl"
        #- Mouse down: 0, (45,100)
        #- Mouse motion: (1), (90,90), (45,-10)


class EventManager(Component):
    def __init__(self):
        Component.__init__(self)
        
        self.events = []
        
    def update(self):
        Component.update(self)
        
        del self.events[:]
        
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                e = Event()
                e.type = EventType.quit
                e.data = None
                self.events.append(e)
           
            elif event.type == pygame.locals.KEYDOWN:
                e = Event()
                e.type = EventType.key_down
                key = None
                modifier = None
                if event.key == pygame.locals.K_SPACE: key = "space"
                elif event.key == pygame.locals.K_UP: key = "up"
                elif event.key == pygame.locals.K_DOWN: key = "down"
                elif event.key == pygame.locals.K_LEFT: key = "left"
                elif event.key == pygame.locals.K_RIGHT: key = "right"
                elif event.key == pygame.locals.K_ESCAPE: key = "escape"
                e.data = (key, modifier)
                self.events.append(e)
    
    def get_events(self):
        return self.events
    
    def get_key_down(self, key):
        for event in self.events:
            if event.type == EventType.key_down:
                if event.data[0] == key:
                    return True
