import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    def __init__(self,ai_settings,screen):
        super(Aliens, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        #load the image file
        self.image = pygame.image.load('images/alien.bmp')
        #get the rect of the image
        self.rect = self.image.get_rect()
        #get the rect of the screen
        self.screen_rect = screen.get_rect()
        #place the alien at a distance from the top and left side of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store the x position
        self.rect_x = self.rect.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)