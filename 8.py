import turtle as t
screen = t.Screen()

t.up()

t.goto(0,-200)
t.down()
t.goto(0,200)
def rect(color):
    # t.pencolor('black')
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

rect('orange')
t.up()
t.goto(0,150)
t.down()
rect('white')
t.goto(0,100)
t.down()
rect('green')
t.up()

t.goto(100,100)
t.down()
t.fillcolor('blue')
t.begin_fill()
t.circle(25)
t.end_fill()


num_lines = 24
angle = 360 / num_lines
for i in range(num_lines):
    t.up()
    t.goto(100, 125)
    t.down()
    t.setheading(angle * i)
    t.forward(25)


screen.update()
screen.mainloop()

