
class Settings:
    """Class to store all ALIEN INVASION game settings"""

    def __init__(self):
        """Initialize the game setting"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        # Define background color (default is black).
        self.bg_color = (230, 230, 255)
        # Ship settings 1.5 pixel
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_height = 15
        self.bullet_width = 15
        self.bullet_color = (60, 60, 60)
        # Storing the number of bullets allowed in the game
        self.bullets_allowed = 3
        self.bullet_speed = 2.0

