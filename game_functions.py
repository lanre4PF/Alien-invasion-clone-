import sys
import pygame
from Bullet import Bullet
from alien import Aliens



def check_events(ai_settings, screen, ship, bullet):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYUP:
            check_events_keyup(ship, event)

        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event,ai_settings,screen,ship,bullet)



def check_events_keydown(event, ai_settings, screen, ship, bullet):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        #create new bullet
        new_bullet = Bullet(ai_settings,screen,ship)
        if len(bullet) < ai_settings.bullets_allowed:
            bullet.add(new_bullet)

    elif event.key == pygame.K_q:
        sys.exit()



def check_events_keyup(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullet(bullet):
    # updating bullets and deleting the bullets not shown on the screen
    bullet.update()
    for bullets in bullet.copy(2):
        if bullets.rect.y <= 0:
            bullet.remove(bullets)


def create_fleet(aliens,ai_settings,screen):
    # making an instance of the alien class
    alien = Aliens(ai_settings,screen)
    alien_width = alien.rect.width
    #calculations to determine the number of aliens that can fit on the screen
    availale_space = ai_settings.screen_width - 2 * alien_width
    no_of_aliens = int(availale_space/2*alien_width)



def update_screen(ai_settings,screen,ship,bullet,aliens):
    # change background colour
    screen.fill(ai_settings.bg_colour)    #draw bullets on the screen
    for bullets in bullet.sprites():
        bullets.draw_bullets()
    # display ship at the center of the screen
    ship.blitme()
    #display alien at the top left corner of the screen
    aliens.draw(screen)

    # redraw screen
    pygame.display.flip()

