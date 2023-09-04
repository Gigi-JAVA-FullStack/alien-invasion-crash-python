import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """General Class for managing game assets and behavior"""

    def __init__(self):
        """Initializes the game and creates game resources"""
        pygame.init()
# Set the boot method clock (ensuring it works once on each pass through the MAIN loop). class CLOCK, module pygame.time
        self.clock = pygame.time.Clock()
        # Create a instance Setting and self.setting receive that instance
        self.settings = Settings()
# Create a display window, the arguments iS a TUPLE(width x height pixels) attributes screen (setting to access color)
        # Surface screen -> Parameter -> PYGAME.
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # This surface will be drawn on each pass through the loop so that it can be updated
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # self.dragon = Dragon(self)

    def run_game(self):
        """Main loop initialization, it controls the game"""
        while True:
            # One underline means that it is an auxiliary methods inside the Class (cannot be used outside).
            self._check_events()
            self.ship.update()
            # call bullet.update() for each projectile we insert in the 'bullet group'.
            self._update_bullets()
            self._update_screen()
            # Frame rate per game 60 times : seconds.
            self.clock.tick(60)

    def _check_events(self):
        """Answer the keyboards (keypresses) and mouse events"""
        # Observe keyboard and mouse events. EVENT is all about the user actions.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Answer to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Answer to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """"Create a new projectile and insert in the Bullet Group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            # when spacebar is pressed (active bullets)
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update both: screen images and any changes | flip to the new screen"""
# (RE)draws the Screen during each pass through the loop. RGB color: red(255,0,0), green(0,255,0), blue(0,0,255).
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Method image
        self.ship.blitme()
        # Leave the most recently drawn canvas visible. method fill() the background with the color.
        pygame.display.flip()

    def _update_bullets(self):
        """Updates bullet positions and discards old bullets"""
        # Discard bullets that disappear on top screen,to deactivate the Y-coordinate that is consuming memory.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # Print to find out how many bullets are left in the game
            # print(len(self.bullets))
