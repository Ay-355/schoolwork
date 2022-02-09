import turtle
import random


def main():
    screen = turtle.Screen()
    screen.setup(900, 700)
    screen.setworldcoordinates(0, 0, 10, 10)
    screen.title("Breakout")
    screen.bgcolor("#000000")

    paddle = turtle.Turtle()
    paddle.goto(5, 0)
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("grey")
    paddle.shapesize(1, 5)
    paddle.up()

    ball = turtle.Turtle()
    ball.goto(5, 5)
    ball.speed(0)
    ball.shape("circle")
    ball.color("grey")
    ball.up()

    box = turtle.Turtle(visible=False)
    box.speed(0)
    box.shape("square")
    box.up()
    box.shapesize(1, 4)


    for y in [9.5, 9, 8.5]:
        for x in range(10):
            box.color(random.choice(["blue", "green", "yellow"]))
            box.goto(x + 0.45, y)
            box.stamp()


    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
