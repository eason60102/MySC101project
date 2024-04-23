"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='whack_a_mole')
score = 0
score_label = GLabel('Score=>' + str(score))


def main():
    score_label.font = '-90'
    window.add(score_label, x=0, y=score_label.height)
    onmouseclicked(remove_mole)
    while True:
        img = GImage('mole.png')
        random_x = random.randint(0, window.width - img.width)
        random_y = random.randint(0, window.height - img.height)
        window.add(img, x=random_x, y=random_y)
        pause(DELAY)


def remove_mole(mouse):
    global score
    maybe_object = window.get_object_at(mouse.x, mouse.y)
    if maybe_object is not None and maybe_object is not score_label:
        window.remove(maybe_object)
        score += 1
        score_label.text = 'Score=>' + str(score)


if __name__ == '__main__':
    main()
