import turtle
import random
import numpy as np
from math import sin, cos, radians, degrees, pi, atan, sqrt

def phi(p):
    phi = atan(p[1] / p[0])
    if phi < 0 and p[1] > 0:
        return phi + pi
    elif phi < 0 and p[1] < 0:
        return phi + 2 * pi
    elif phi > 0 and p[0] < 0 and p[1] < 0:
        return phi + pi
    return phi

def rotate(p, angle): # angle in radians
    m = np.array([[cos(angle), sin(angle)],[-sin(angle), cos(angle)]])
    return np.matmul(p,m)

def draw_point(p, size=8, color='blue'):
    turtle.pu()
    turtle.goto(p)
    turtle.pd()
    turtle.dot(size, color)

def draw_background(radius, start, end):
    turtle.speed(10)
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
    # start = rotate(start, 2 * pi * random.random())
    r0 = sqrt(start[0]**2 + start[1]**2)

    end = np.array([random.random() * radius, 0.0])
    end_angle = 2 * pi * random.random()
    end = rotate(end, end_angle)

    start_angle = phi(start)
    end_angle = phi(end)
    # alfa = 2.15
    start_rot = rotate(start, -start_angle)
    end_rot = rotate(end, -start_angle)
    a = (end_rot[1] - start_rot[1]) / (end_rot[0] - start_rot[0])

    draw_background(radius, start, end)

    # calculate d_angle
    d_angle = abs(phi(start) - phi(end))
    d_angle = min(d_angle, 2 * pi - d_angle)
    t_s = np.linspace(0.0, d_angle / omega, num = 300)

    if end_angle > pi:
        angles = map(lambda t: -omega * t, t_s)
        rs = map(lambda phi: (a * r0) / (a * cos(phi) - sin(phi)), angles)

    else:
        angles = map(lambda t: omega * t, t_s)
        rs = map(lambda phi: (a * r0) / (a * cos(phi) - sin(phi)), angles)


    angles = map(lambda p: p + start_angle, angles)
    zipped = list(zip(rs, angles))

    # _ = input()

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