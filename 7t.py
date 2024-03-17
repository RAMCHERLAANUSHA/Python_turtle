import turtle as t

screen = t.Screen()

screen.setup(height=700, width=700)
list1=['green','blue','red','yellow','orange']
t.up()
for i in range(200):
    t.down()
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

screen.update()
screen.mainloop()