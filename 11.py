import turtle
t=turtle.Turtle()
t.width(3)
t.shape("turtle")
t.shapesize(3,3)
while True:
    command=input("명령을 입력하시오:")
    if command=="l":
        t.left(90)
    if command=="r":
        t.right(90)
    if command=="s":
        t.write("프로그램을 종료합니다.")
        break;
    t.fd(100)
