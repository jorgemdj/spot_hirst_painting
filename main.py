import colorgram
from turtle import Turtle, Screen
import random

def color(n):
    colors = colorgram.extract("spot_painting.jpg", n)
    rgb_database = []
    for c in range(0, len(colors)):
        rgb_database.append(colors[c].rgb)
    return rgb_database


def hist_painting(a=100, b=100, n=5, sd=10):
    teddy.penup()
    teddy.teleport(-a/2, -b/2)
    h_distance = a/n
    v_distance = b/n
    paint_color = color(20)
    for v in range(n):
        for h in range(n):
            teddy.pencolor(random.choice(paint_color))
            print(teddy.pos())
            teddy.forward(h_distance)
            teddy.dot(sd)
        teddy.teleport(-a/2, ((-b/2) + (v+1)*v_distance))
    teddy.hideturtle()


teddy = Turtle()
screen = Screen()
screen.colormode(255)
teddy.shape("turtle")
teddy.speed("fastest")

hist_painting(50, 50, 5, 10)


screen = Screen()
screen.exitonclick()
