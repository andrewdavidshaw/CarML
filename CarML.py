# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Andy is his own boss',
                          font_name='Verdana',
                          font_size=36,
                          width=10,
                          x=window.width//2, y=window.height//2,
                          anchor_x='left', anchor_y='top',
                          multiline=True)
@window.event
def on_draw():
    window.clear()
    label.draw()
    
pyglet.app.run()