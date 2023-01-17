from turtle import *


def polygon(sides):
    if sides == 0:
        circle()
    else:
        for i in range(sides):
            forward(100)
            left(360/sides)


def circle():
    while True:
        forward(10)
        right(10)


polygon(10)

done()
