import turtle

win = turtle.Screen()
win.screensize()
win.bgcolor("red")
t = turtle.Turtle()
t.color("blue")
t.penup()
t.setpos(-200,100)
t.pendown()
t.pensize("5")

for i in range (2):
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)

t.pensize(1)
t.penup()
t.setpos(-20,-12)
t.pendown()

t.color("white")
t.fillcolor("white")
t.begin_fill()

for i in range(3):
    t.forward(40)
    t.left(120)

t.end_fill()

t.penup()
t.setpos(-20,12)
t.pendown()
t.color("white")
t.fillcolor("white")
t.begin_fill()

for i in range(3):
    t.forward(40)
    t.right(120)

t.ht()
t.end_fill()
win.exitonclick()