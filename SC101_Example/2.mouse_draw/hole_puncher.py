"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30
# Global Variable
window = GWindow()


def main():
    onmouseclicked(create_hole)


def create_hole(mouse):
    hole = GOval(SIZE, SIZE)
    hole.filled = True
    window.add(hole, x=mouse.x, y=mouse.y)


if __name__ == '__main__':
    main()
