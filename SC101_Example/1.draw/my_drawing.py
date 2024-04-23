"""
File: my_drawing.py
Name: Eason
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800, height=500, title='Myface')
    face = GOval(200, 250, x=350, y=200)
    window.add(face)
    l_eye = GOval(50, 50, x=450, y=230)
    window.add(l_eye)
    r_eye = GOval(50, 50, x=390, y=230)
    window.add(r_eye)
    mouth = GRect(120, 40, x=390, y=360)
    window.add(mouth)
    face.filled = True
    face.fill_color = "yellow"
    l_eye.filled = True
    r_eye.filled = True
    mouth.color = "azure"
    mouth.filled = True
    mouth.fill_color = "red"

    label = GLabel("Hello world")
    label.font = '-40'
    label.color = 'red'

    window.add(label, x=0, y=label.height)


if __name__ == '__main__':
    main()
