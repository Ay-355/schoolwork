import turtle
import random
import time


def move(direction: str, paddle: turtle.Turtle, screen: turtle.Screen):
    if paddle.xcor() > 9 and direction == "right":
        return
    elif paddle.xcor() < 1 and direction == "left":
        return
    paddle.setx(paddle.xcor() + (0.5 if direction == "right" else -0.5))
    screen.update()


def check_collision(ball: turtle.Turtle, paddle: turtle.Turtle):
    if ball.ycor() < 0.3 and ball.xcor() > paddle.xcor() - 0.5 and ball.xcor() < paddle.xcor() + 0.5:
        ball.dy *= -1
        print("collision")
    elif ball.ycor() < -0.2:
        print("END")
        ball.goto(5, 5)
        time.sleep(1)


def move_ball(ball: turtle.Turtle, screen: turtle.Screen, paddle: turtle.Turtle):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() > 9.9 or ball.xcor() < 0:
        ball.dx *= -1
    if ball.ycor() > 11.9:
        ball.dy *= -1
    screen.update()
    check_collision(ball, paddle)
    screen.ontimer(lambda: move_ball(ball, screen, paddle), 1)


def main():
    screen = turtle.Screen()
    screen.setup(900, 700)
    screen.setworldcoordinates(0, 0, 10, 12)
    screen.title("Breakout")
    screen.bgcolor("#000000")

    boxes = []
    for _ in range(3):
        boxes.append([True] * 10)

    paddle = turtle.Turtle()
    paddle.goto(5, 0)
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("grey")
    paddle.shapesize(1, 6)
    paddle.up()

    ball = turtle.Turtle()
    ball.goto(5, 5)
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.up()
    ball.dx = 0.004
    ball.dy = 0.004

    box = turtle.Turtle(visible=False)
    box.speed(0)
    box.shape("square")
    box.up()
    box.shapesize(1, 4)

    for y in [11.5, 11, 10.5]:
        for x in range(10):
            box.color(random.choice(["blue", "green", "yellow"]))
            box.goto(x + 0.45, y)
            box.stamp()

    screen.onkey(lambda: move("left", paddle, screen), "Left")
    screen.onkey(lambda: move("right", paddle, screen), "Right")
    screen.onclick(lambda x, y: print(x, y))
    screen.tracer(0)
    move_ball(ball, screen, paddle)

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
