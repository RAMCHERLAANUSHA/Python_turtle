import turtle as t


screen = t.Screen()
screen.setup(width=800, height=800)
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

screen.update()
screen.mainloop()