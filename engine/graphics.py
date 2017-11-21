import pygame

from ecs.component import Component

class Sprite(Component):
    def __init__(self):
        Component.__init__(self)
        
        self._image = None
        self._rect = None
        
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    
    def set_image(self, image_path):
        self._image = pygame.image.load(image_path)
        self._rect = self._image.get_rect()
        
        self.x = self._rect.x
        self.y = self._rect.y
        self.width = self._rect.width
        self.height = self._rect.height
    
    def update(self):
        Component.update(self)
        
        if self._image and self._rect:
            self._rect.x = self.x
            self._rect.y = self.y
            self._rect.width = self.width
            self._rect.height = self.height
            
            self.screen.blit(self._image, self._rect)