import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen  = screen
        #create rect for the bullets
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #position the bullet at the center of the screen
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #store the bullets position on the y coordinate as a float
        self.y = float(self.rect.y)
        #initializing the bullets speed factor and color
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Move the bullet up the screen
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        #Update the rect position.
        #new position of bullet rect on the y axis is equal to self.y
        self.rect.y = self.y

    def draw_bullets(self):
        pygame.draw.rect(self.screen,self.color,self.rect)