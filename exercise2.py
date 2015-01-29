# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
A two-dimensional random walk simulator and animator.
'''

# The turtle package is part of Python's standard library. It provides some
# very primitive graphics capabilities. For more details see
#
#   https://docs.python.org/3/library/turtle.html
#
import turtle

import numpy as np

def random_walk(n, x_start = 0, y_start = 0):
    ''' Simulate a two-dimensional random walk.

    Args:
        n           number of steps

    Returns:
        Two Numpy arrays containing the x and y coordinates, respectively, at
        each step (including the initial position).
    '''

    # Your task: fill this in.
    directions = np.random.random_integers(1, 4, n)
    
    ver = [x == 1 or x == 2 for x in directions]
    hor = [x == 3 or x == 4 for x in directions]
    
    x_step = np.where(ver, 0, np.where(directions == 3, -1, 1))
    y_step = np.where(hor, 0, np.where(directions == 1, 1, -1))
    
    x = x_start + np.cumsum(x_step)
    y = y_start + np.cumsum(y_step)

    return x, y



# Notice that the documentation automatically shows up when you use ?
def draw_walk(x, y, speed = 'slowest', scale = 20):
    ''' Animate a two-dimensional random walk.

    Args:
        x       x positions
        y       y positions
        speed   speed of the animation
        scale   scale of the drawing
    '''
    # Reset the turtle.
    turtle.reset()
    turtle.speed(speed)

    # Combine the x and y coordinates.
    walk = zip(x * scale, y * scale)
    start = next(walk)

    # Move the turtle to the starting point.
    turtle.penup()
    turtle.goto(*start)

    # Draw the random walk.
    turtle.pendown()
    for _x, _y in walk:
        turtle.goto(_x, _y)

def main(n):
    test = random_walk(n)
    draw_walk(test[0], test[1])

