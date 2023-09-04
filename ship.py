import pygame


class Ship:
    """Class to take care of the ship"""

    def __init__(self, ai_game):
        """Initialize spacecraft and set home position (first position)"""
        # reference ai_game is an instance from AlienInvasion
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Game elements like rectangle (rect)
        self.screen_rect = ai_game.screen.get_rect()

        # Under (or above) the spaceship image get the rectangle (rect)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new spaceship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Horizontal position, store a float for the ship
        self.x = float(self.rect.x)

        # The movement Flag, when the ship will remain immobile
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the spacecraft at its current location."""
        # method blit() to draw the image | format .bmp | site: https://opwngameart.org/
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship position based on movement flag"""
        # Update the ship X value, do not update the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:

            # Update rect object from self.x. (setting module has a ship_speed 1.5 pixel)
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # Update rect object from self.x.
            self.x -= self.settings.ship_speed

        # Update rect object from self.x. This code look to the OBJECT first.
        self.rect.x = self.x

