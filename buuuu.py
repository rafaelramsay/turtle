# Step 1: Make all the "turtle" commands available to us.
import turtle
import random


from turtle import *
pensize('5')
shape('turtle')
color('red', 'green')
begin_fill()
while True:
    goto(random.random(), random.random())

    right(1000)
    forward(99)
    left(500)
    penup()
    stamp()
    if abs(pos()) < 1:
        break
end_fill()
done()
