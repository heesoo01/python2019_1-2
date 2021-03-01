import turtle
def tree(len):
    if len>5:
        t.fd(len)
        t.right(20)
        tree(len-15)
        t.left(4)
        tree(len-15)
        t.right(20)
        t.backward(len)
        t.write(len)
t=turtle.Turtle()
t.left(90)
t.color("green")
t.speed(1)
tree(90)
