from turtle import *


def spiral():
    n = 5
    for i in range(60):
        for j in range(4):
            forward(n)
            right(90)
        right(5)
        n += 5
            
spiral()
done()