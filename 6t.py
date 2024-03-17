import turtle as t

screen = t.Screen()

screen.setup(height=700, width=700)
list1=['green','red','yellow','orange']
t.up()

t.goto(200,200)
for i in range(0,4):
    t.down()
    t.begin_fill()
    t.pensize(20)
    t.fillcolor(list1[i])
    t.circle(50)
    t.end_fill()
    t.up()
    t.bk(100)

screen.update()
screen.mainloop()
