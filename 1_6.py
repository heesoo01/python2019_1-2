import turtle
t=turtle.Turtle()
def n_poly(n,len):
    for i in range(n):
        t.fd(len)
        t.left(360/n)
for i in range(10):
    t.left(20)
    n_poly(6,100)
