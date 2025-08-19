import pygame
import sys

def run_game():
    pygame.init()
    screen_resolution = (1200,800)
    screen = pygame.display.set_mode(screen_resolution)
    pygame.display.set_caption("Blue background")
    screen_colour = 230,230,230
    screen.fill(screen_colour)
    image = pygame.image.load('images/ship.bmp')
    rect_image = image.get_rect()
    screen_rect = screen.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
        screen.blit(image,rect_image)


        pygame.display.flip()




run_game()




