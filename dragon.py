import pygame


class Dragon:
    """Class to take care of the dragon"""

    def __init__(self, ai_dragon):
        """Initialize spacecraft and set home position (first position)"""
        # reference ai_game is an instance from AlienInvasion
        self.screen = ai_dragon.screen
        # Under (or above) the spaceship image get the rectangle (rect)
        self.image = pygame.image.load('images/dragon.bmp')
        self.bool = self.image.get_rect()

        # Start each new spaceship at the bottom center of the screen.
        self.bool.center = self.screen_rect.center


    def blitme(self):
        """Draw the spacecraft at its current location."""
        # method blit() to draw the image | format .bmp | site: https://opwngameart.org/
        self.screen.blit(self.image, self.bool)