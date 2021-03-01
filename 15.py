import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","도형을 입력하시오:")
if s=="사각형":
    s=turtle.textinput("","가로:")
    w=int(s)
    s=turtle.textinput("","세로:")
    h=int(s)
    t.fd(w)
    t.left(90)
    t.fd(h)
    t.left(90)
    t.fd(w)
    t.left(90)
    t.fd(h)
if s=="삼각형":
    s=turtle.textinput("","한변 길이:")
    w=int(s)
    for i in range(3):
        t.fd(w)
        t.left(120)
if s=="원":
    s=turtle.textinput("","반지름 길이:")
    w=int(s)
    t.circle(w)
    
    
    
    
    
