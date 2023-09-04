# alien-invasion-crash-python
I'm going to create and write, then I'll do a final summary.

"""
Main file ALIEN_INVASION.py
class AlienInvasion
creates attributes used in the game

Settings file SETTING.py
class Settings -> with only one __init__() method. Initializes the attributes controlling appearance and ship speed.
SHIP.py spacecraft file
class Ship -> with __init__() method, update() that manages ship position and blitme() method to draw ship on the screen.
(*) The ship.bmp image of the spacecraft is in the IMAGEs folder.
Both files contain code imported into the main ALEIN_INVASION.py file.

In Python, a single _xxx underscore on the left means an auxiliary method, which only works inside a Class.
Auxiliary _methods should not be used outside the Class to which they belong.

Game display surface assigned to the SCREEN variable
Spacecraft instance created
Clock marking in each pass of the While Loop
Loop WHILE calls:
 _check_events(): detects relevant events, key presses and releases.
 Processes events with auxiliary METHODS
 _check_keydown_events(), and _check_keyup_events().
 Manage the movement of the spacecraft.
 ship.update(),
_update_screen(): redraws the screen each time it passes through the Main Loop.

HERITAGE
To create an instance of BULLET, __init__() needs an instance of the main file ALIEN_INVASION.py
called SUPER() to properly inherit the Sprite.
Defined attributes for OBJECT screens and settings for bullets.
created the REACT attribute for BULLET building a RETANGLE from scratch using the PYGAME.RECT() class
COORDINATES -> X and Y with the top left corner of the rect and the width and height of the rect.
Initialize with coordinates 0 x O
We obtain the width and height of the BULLET using the values stored in SELF.SETTINGs.

MIDTOP attribute of the BULLET to match the MIDTOP attribute of the spacecraft.
This will make the bullet appear in front of the spacecraft as if it is being fired from inside it.
 We use FLOAT for the y COORDINATES to adjust the speed of the bullets (it gets smaller and consumes memory as it goes up).

When we use a FOR loop with a LIST (pygame) Python expects the list to remain the SAME SIZE,
as long as the LOOP is running. WE CANNOT REMOVE ITEMS from a list (or group) inside a FOR loop.
We must create a copy method COPY() to set up the FOR loop and then modify the group of BULLETS in the looping.

LOOP WHILE -> run_game()
main loop, read the METHOD names
check the player's input
updates the position of the spacecraft and the fired bullets
Positions are updated to draw new SCREEN
Mark seconds on the clock for each looping pass
