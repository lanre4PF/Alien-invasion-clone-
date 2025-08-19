import pygame
from settings import Settings
from ship import Ship
import game_functions as g_f
from pygame.sprite import Group
from alien import Aliens

def run_game():
    # creating an instance of the settings class
    ai_settings = Settings()


    #initialize game and screen object
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    # making the ship appear on the screen
    ship = Ship(screen,ai_settings)
    # making a Group() from the sprite class
    bullet = Group()

    #making a group for the aliens
    aliens = Group()

    while True:
        g_f.check_events(ai_settings,screen,ship,bullet )
        ship.update_position()
        g_f.update_bullet(bullet)
        g_f.update_screen(ai_settings,screen,ship,bullet,aliens)

run_game()



