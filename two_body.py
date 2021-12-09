import math
import turtle


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def grav_mag(m1, x1, y1, m2, x2, y2):
    return m1 * m2 / distance(x1, y1, x2, y2) ** 2


def main():
    x1, y1 = 3, 0
    x2, y2 = -3, 0
    m1, m2 = 1, 1
    vx1, vy1 = 0, 0.25
    vx2, vy2 = 0, -0.25

    screen = turtle.Screen()
    screen.screensize(700, 700)
    screen.setworldcoordinates(-5, -5, 5, 5)

    pointer1 = turtle.Turtle()
    pointer1.up()
    pointer1.speed(0)
    pointer1.goto(x1, y1)
    pointer1.color("red")
    pointer1.shape("circle")
    pointer1.down()

    pointer2 = turtle.Turtle()
    pointer2.up()
    pointer2.speed(0)
    pointer2.goto(x2, y2)
    pointer2.color("blue")
    pointer2.shape("circle")
    pointer2.down()

    t_step = 0.001
    i = 0
    while True:
        f12_mag = grav_mag(m1, x1, y1, m2, x2, y2)
        f12_dir = math.atan2(y2 - y1, x2 - x1)
        x1, y1 = x1 + vx1 * t_step, y1 + vy1 * t_step
        x2, y2 = x2 + vx2 * t_step, y2 + vy2 * t_step

        vx1 += f12_mag * math.cos(f12_dir) * t_step / m1
        vy1 += f12_mag * math.sin(f12_dir) * t_step / m1
        vx2 += f12_mag * math.cos(f12_dir + math.pi) * t_step / m2
        vy2 += f12_mag * math.sin(f12_dir + math.pi) * t_step / m2

        if i % 1000 == 0:
            pointer1.goto(x1, y1)
            pointer2.goto(x2, y2)
        i += 1


if __name__ == "__main__":
    main()
