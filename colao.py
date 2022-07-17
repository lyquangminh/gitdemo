import turtle

p = turtle.Turtle()
p.hideturtle()
p.speed(20)

p.penup()
p.backward(250)
p.pendown()
# lá cờ
p.fillcolor('red')
p.begin_fill()
for i in range(2):
    p.forward(500)
    p.left(90)
    p.forward(250)
    p.left(90)
p.end_fill()
# khoảng cách
p.penup()
p.right(90)
p.backward(200)
p.pendown()
# phông xanh
p.fillcolor('blue')
p.begin_fill()
for i in range(2):
    p.forward(150)
    p.left(90)
    p.forward(500)
    p.left(90)
p.end_fill()
#tâm cờ
p.penup()
p.forward(135)
p.left(90)
p.forward(250)
p.pendown()
p.color('white')
p.begin_fill()
p.circle(60)
p.end_fill()

turtle.done()