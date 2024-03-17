

import turtle as t
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

t.color("red")

t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
screen.update()

t.penup()
t.goto(5, 140)
t.color('black')
t.write("", align="center", font=("Arial", 20, "bold"))
# time.sleep(3)
# screen.bye()
screen.mainloop()