from turtle import Turtle
t=Turtle()
x = 60
y = -80
t.penup()
t.goto(x,y)
t.pendown()
for i in range (10):
    for j in range(i+3):
        t.left(360/(i+3))
        t.forward(120)
    x += 0.1
    y -= 15
    t.penup()
    t.goto(x,y)
    t.pendown()