import sys
import pygame

from ecs.game_object import GameObject
from ecs.component import Component


class Scene(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        
        self.name = "Scene"


def start_game(scene, screen_width=640, screen_height=480, game_title="slave"):
    pygame.init()
    size = screen_width, screen_height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(game_title)
    
    Component.screen = screen

    scene.start()
    
    while 1:
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT: sys.exit()
        
        screen.fill((0, 0, 0))
        
        scene.update()

        pygame.display.flip()
