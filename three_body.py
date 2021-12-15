import math
import turtle


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def grav_mag(m1, x1, y1, m2, x2, y2):
    return m1 * m2 / distance(x1, y1, x2, y2) ** 2


def main():

    r = 1
    m1, m2, m3 = 1, 1, 1
    vx3, vy3 = -0.93240737 * r, -0.86473146 * r
    vx1, vy1 = -vx3 / 2, -vy3 / 2
    vx2, vy2 = vx1, vy1
    x1, y1 = 0.97000436 * r, -0.24308753 * r
    x2, y2 = -x1, -y1
    x3, y3 = 0, 0
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

    pointer3 = turtle.Turtle()
    pointer3.up()
    pointer3.speed(0)
    pointer3.goto(x3, y3)
    pointer3.color("green")
    pointer3.shape("circle")
    pointer3.down()

    t_step = 0.0001
    i = 0
    while True:
        f12_mag = grav_mag(m1, x1, y1, m2, x2, y2)
        f12_dir = math.atan2(y2 - y1, x2 - x1)
        f13_mag = grav_mag(m1, x1, y1, m3, x3, y3)
        f13_dir = math.atan2(y3 - y1, x3 - x1)
        f23_mag = grav_mag(m2, x2, y2, m3, x3, y3)
        f23_dir = math.atan2(y3 - y2, x3 - x2)

        x1, y1 = x1 + vx1 * t_step, y1 + vy1 * t_step
        x2, y2 = x2 + vx2 * t_step, y2 + vy2 * t_step
        x3, y3 = x3 + vx3 * t_step, y3 + vy3 * t_step
        vx1 += (
            f12_mag * math.cos(f12_dir) * t_step / m1
            + f13_mag * math.cos(f13_dir) * t_step / m1
        )
        vy1 += (
            f12_mag * math.sin(f12_dir) * t_step / m1
            + f13_mag * math.sin(f13_dir) * t_step / m1
        )
        vx2 += (
            f12_mag * math.cos(f12_dir + math.pi) * t_step / m2
            + f23_mag * math.cos(f23_dir) * t_step / m2
        )
        vy2 += (
            f12_mag * math.sin(f12_dir + math.pi) * t_step / m2
            + f23_mag * math.sin(f23_dir) * t_step / m2
        )
        vx3 += (
            f23_mag * math.cos(f23_dir + math.pi) * t_step / m3
            + f13_mag * math.cos(f13_dir + math.pi) * t_step / m3
        )
        vy3 += (
            f23_mag * math.sin(f23_dir + math.pi) * t_step / m3
            + f13_mag * math.sin(f13_dir + math.pi) * t_step / m3
        )

        if i % 1000 == 0:
            pointer1.goto(x1, y1)
            pointer2.goto(x2, y2)
            pointer3.goto(x3, y3)
        i += 1


if __name__ == "__main__":
    main()
