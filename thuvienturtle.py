import turtle

pen = turtle.Turtle()
pen.speed(4)
pen.hideturtle()
pen.pensize('5')

pen.forward(300)
pen.left(90)
pen.forward(180)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(180)
pen.left(90)
pen.penup()
pen.forward(210)
pen.left(90)
pen.forward(90)
pen.pendown()
pen.fillcolor('red')
pen.begin_fill()
pen.circle(60)
pen.end_fill()

turtle.done()