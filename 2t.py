import turtle as t


screen = t.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("blue")

t.color('white')
t.begin_fill()
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.forward(120)
t.right(90)
t.end_fill()

screen.update()



screen.mainloop()