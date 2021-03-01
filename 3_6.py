import turtle
def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.fd(height)
    t.write(str(height),font=('Times New Roman',16,'bold'))
    t.right(90)

    t.fd(40)
    t.right(90)
    t.fd(height)
    t.left(90)
    t.end_fill()
data=[12,34,12,45,13,45]
t=turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)
for d in data:
    drawBar(d)
