import turtle
import random
import numpy as np
from math import sin, cos, radians, degrees, pi

def rotate(p, angle): # angle in radians
    m = np.array([[cos(angle), sin(angle)],[-sin(angle), cos(angle)]])
    return np.matmul(p,m)

def draw_point(p, size=8, color='blue'):
    turtle.pu()
    turtle.goto(p)
    turtle.pd()
    turtle.dot(size, color)

def draw_background(radius, start, end):
    turtle.speed(8)
    turtle.degrees()
    turtle.pu()
    turtle.goto(radius,0)

    turtle.pd()
    turtle.setheading(90)
    turtle.circle(radius)

    draw_point(start)
    draw_point(end)
    turtle.pu()
    turtle.goto(start)
    turtle.pd()

if __name__ == "__main__":
    radius = 300.0
    omega = 1.0 #rad/s

    start = np.array([random.random() * radius, 0.0])
    end = np.array([random.random() * radius, 0.0])
    end_angle = 2 * pi * random.random()
    end = rotate(end, end_angle)

    #end = np.array([-150, -150])
    #end_angle = 225 * pi / 180

    a = (end[1] - start[1]) / (end[0] - start[0])

    draw_background(radius, start, end)

    d_angle = min(end_angle, 2 * pi - end_angle)
    t_s = np.linspace(0.0, d_angle / omega, num = 120)

    if end_angle > pi:
        rs = map(lambda t: (a * start[0]) / (a * cos(-omega * t) - sin(-omega * t)), t_s)
        angles = map(lambda t: -omega * t, t_s)
    else:
        rs = map(lambda t: (a * start[0]) / (a * cos(omega * t) - sin(omega * t)), t_s)
        angles = map(lambda t: omega * t, t_s)

    zipped = list(zip(rs, angles))

    _ = input()

    screen = turtle.Screen()
    screen.tracer(0)
    turtle.speed(0)
    turtle.hideturtle()

    turtle.pd()
    for i in range(len(zipped)):
        turtle.clear()
        draw_background(radius, start, end)
        for j in range(i + 1):
            r, angle = zipped[j]
            pt = np.array([r * cos(angle), r * sin(angle)])
            turtle.goto(pt)

        turtle.pu()
        turtle.goto(0,0)
        turtle.setheading(degrees(zipped[i][1]))
        turtle.pensize(10)
        turtle.pd()
        turtle.fd(radius)
        r = zipped[i][0]
        angle = zipped[i][1]
        pt = np.array([r * cos(angle), r * sin(angle)])
        draw_point(pt, size=12, color='red')
        turtle.pensize(1)

        screen.update()

    _ = input()
