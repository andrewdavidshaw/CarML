# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyglet

window = pyglet.window.Window(1600,1200)
label = pyglet.text.Label('Andy is his own boss',
                          font_name='Verdana',
                          font_size=8,
                          x=window.width//2, y=window.height//2,
                          anchor_x='left', anchor_y='top',
                          multiline=False)

label2 = pyglet.text.Label('Bman is a wage slave',
                           font_name='Comic Sans',
                           font_size=12,
                           x=window.width//4, y=window.height//4,
                           anchor_x='left', anchor_y='top',
                           multiline=False)

@window.event
def on_draw():
    window.clear()
    label.draw()
    label2.draw()
    
pyglet.app.run()