import turtle
import random
import time

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("space_.png")
space.addshape("sprite.gif")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")

while True:

    space.update()
    time.sleep(0.2)

