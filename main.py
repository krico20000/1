import turtle
import random

def burst():
    t.hideturtle()
    turtle.tracer(0, 0)
    t.color(random.choice(colors))
    for x in range(50):
        t.forward(100)
        t.right(190)
        turtle.update()
    turtle.tracer(1, 1)
    t.showturtle()

t = turtle.Turtle()
t.shape("arrow")
t.screen.bgcolor("midnight blue")
colors = ["red", "green", "yellow", "salmon", "pink", "white", "orange", "purple", "violet", "cyan"]
t.speed(0)
turtle.title("Фейерверки")
t.hideturtle()
t.up()
t.goto(0, -400)
t.left(90)
t.down()
t.showturtle()
for h in range(50):
    for d in range(30):
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()
    t.clear()
    burst()
    t.hideturtle()
    t.up()
    t.home()
    t.left(90)
    t.goto(random.randint(-320, 320), -400)
    t.showturtle()
    t.color("black")

turtle.mainloop()