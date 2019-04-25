# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyglet
import numpy as np

def make_label(window):
    """makes a label given a window"""
    x1 = np.random.random()
    y1 = np.random.random()
    font_size1 = np.random.choice([10,16,20,24,34])
    text = np.random.choice(["Heya","Bye","Booyah"])
    label = pyglet.text.Label(text,
            font_name='Comic Sans',
            font_size=font_size1,
            x=window.width*x1, y=window.height*y1,
            anchor_x='left', anchor_y='top',
            multiline=False)
    return label
    
window = pyglet.window.Window(800,600)
label = pyglet.text.Label('Andy is his own boss',
                          font_name='Verdana',
                          font_size=8,
                          x=window.width//2, y=window.height//2,
                          anchor_x='left', anchor_y='top',
                          multiline=False)

label3 = pyglet.text.Label('Key pressed',
                           font_name='Comic Sans',
                           font_size=16,
                           x=window.width//4, y=window.height//4,
                           anchor_x='left', anchor_y='top',
                           multiline=False)

label4 = pyglet.text.Label('9/11 was an inside job',
                           font_name='Comic Sans',
                           font_size=16,
                           x=window.width//4, y=window.height//4,
                           anchor_x='left', anchor_y='top',
                           multiline=False)

label5 = pyglet.text.Label('NO COLLUSION',
                           font_name='Comic Sans',
                           font_size=16,
                           x=window.width//4, y=window.height//4,
                           anchor_x='left', anchor_y='top',
                           multiline=False)

@window.event
def on_draw():
    label.draw()
       
from pyglet.window import key

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A pressed')
        window.clear()
        label3.draw()
    elif symbol == key.LEFT:
        window.clear()
        label4.draw()
    elif symbol == key.ENTER:
        window.clear()
        label5.draw()
    elif symbol == key.SPACE:
        print('Rando Calrissian')
        make_label(window).draw()     
    
pyglet.app.run()