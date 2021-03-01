import turtle
t=turtle.Turtle()
t.shape("turtle")

color_list=["yellow","red","blue","green"]
i=0
for i in range(4):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.fd(50)
    i+=1
