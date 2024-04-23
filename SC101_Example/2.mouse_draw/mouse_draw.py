"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the pen stroke
SIZE = 30
# Global Variable
window = GWindow()


def main():
	onmousedragged(draw)
	onmouseclicked(draw)


def draw(mouse):
	pen_stoke = GOval(SIZE, SIZE)
	pen_stoke.filled = True
	window.add(pen_stoke, x=mouse.x - (SIZE/2), y=mouse.y - (SIZE/2))


if __name__ == '__main__':
	main()
