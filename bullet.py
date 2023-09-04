import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manager the bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create an object bullet in the current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect (0, 0) -> set the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Storage bullet position as FLOAT (y)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet UP Screen"""
        # Update the exact position of the bullet y-coordinate
        self.y -= self.settings.bullet_speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Drawn Bullets to show Screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)