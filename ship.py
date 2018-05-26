# shows the ship on screen_width
import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting positon"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship and get its rectself.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)


        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag"""
        # update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current locations"""
        self.screen.blit(self.image, self.rect)
