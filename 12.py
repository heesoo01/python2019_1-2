import turtle
import random
screen=turtle.Screen()
image1="d:\\front.gif"
image2="d:\\back.gif"
screen.addshape(image1)
screen.addshape(image2)
t=turtle.Turtle()
coin=random.randint(0,1)
if coin==0:
    t.shape(image1)
else:
    t.shape(image2)
t.stamp()


