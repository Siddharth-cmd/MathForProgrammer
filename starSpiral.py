from turtle import *

def starSpiral():
    n = 50
    for i in range(60):
        for j in range(5):
            forward(n)
            right(144)
        n += 5
        right(5)

starSpiral()
done()