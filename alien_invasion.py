# Alien invasion game
# main window

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make an alien
    # alien = Alien(ai_settings, screen)

    # make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # set the background color
    bg_color = (230, 230, 230)

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keybord and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
