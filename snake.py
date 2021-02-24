import turtle
import time
import random

def balra():
    fej.left(90)

def jobbra():
    fej.right(90)

pálya = turtle.Screen()
pálya.setup(width=800, height=600)
pálya.title("SNAKE")
pálya.bgcolor("green")
pálya.tracer(0)
pálya.listen()
pálya.onkey(balra, "Left")
pálya.onkey(jobbra, "Right")

fej = turtle.Turtle() 
fej.shape("triangle")
fej.color("yellow")
fej.penup()

kijelzo = turtle.Turtle()
kijelzo.hideturtle()

alma = turtle.Turtle()
alma.shape("circle")
alma.color("red")
alma.penup()

kukac = []

szamlalo = 0

def hizik(x, y):
    testresz = turtle.Turtle()
    testresz.color("yellow")
    testresz.penup()
    testresz.shape("circle")
    testresz.setx(x)
    testresz.sety(y)
    kukac.append(testresz)

hizik(0, 0)

while True:
    fej_x = fej.xcor()
    fej_y = fej.ycor()
    fej.forward(20)   
    if fej.distance(alma.xcor(), alma.ycor()) < 15:
        x = random.randint(-380, 380)
        y = random.randint(-280, 280)
        alma.goto(x, y)
        hizik(fej_x, fej_y)
        szamlalo += 1
        kijelzo.clear()
        kijelzo.write(szamlalo, align="center", font=("Arial", 30, "bold"))

    if fej.xcor() > 390:
        kijelzo.write("Megdöglött a kukacod!", align="center", font=("Arial", 36, "bold"))
        time.sleep(0.2)
        kijelzo.clear()
    
    kukac[-1].setx(fej_x)
    kukac[-1].sety(fej_y)
    kukac = [kukac[-1]] + kukac[:-1]
    pálya.update()
    time.sleep(0.2)

    for resz in kukac:
        if fej.xcor() == resz.xcor() and fej.ycor() == resz.ycor():
            kijelzo.write("Megdöglött a kukacod!", align="center", font=("Arial", 36, "bold"))



