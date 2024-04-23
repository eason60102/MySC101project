"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmousedragged, onmouseclicked

# This constant controls the size of the GRect
SIZE = 100
rect = GRect(SIZE, SIZE)
window = GWindow()


def main():
	rect.filled = True
	rect.fill_color = "blue"
	window.add(rect)
	onmousemoved(reset_rect_position)
	onmousedragged(draw)
	onmouseclicked(draw)


def reset_rect_position(event):
	rect.x = event.x - SIZE/2
	rect.y = event.y - SIZE/2


def draw(mouse):
	pen_stoke = GRect(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
	pen_stoke.filled = True
	window.add(pen_stoke)


if __name__ == '__main__':
	main()
