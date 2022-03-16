import random
import time
import turtle


def move(direction: str, paddle: turtle.Turtle, screen: turtle.Screen):
    if paddle.xcor() > 7 and direction == "right":
        return
    elif paddle.xcor() < 1 and direction == "left":
        return
    paddle.setx(paddle.xcor() + (0.5 if direction == "right" else -0.5))
    screen.update()


def check_collision(ball: turtle.Turtle, paddle: turtle.Turtle, boxes: list, box: turtle.Turtle, missed: int) -> int:
    # ball and paddle
    # sometimes the math if off and the ball gets "stuck" in the paddle
    # i'm leaving it because the game is hard to finish, and you can use it getting stuck to control the ball
    if ball.ycor() < 0.2 and ball.xcor() > paddle.xcor() - 0.65 and ball.xcor() < paddle.xcor() + 0.55:
        ball.dy *= -1
    # ball does not hit paddle
    if ball.ycor() < -0.15:
        ball.goto(4, 3)
        time.sleep(1)
        missed += 1

    # ball hits brick
    # it only check if hitting from top or bottom, not sides
    # this leads to weird things happening when the ball gets stuck on the top layer
    # i'm leaving because the game is slow and this makes it faster
    m = {5.7: 0, 5.4: 1, 5.1: 2}
    if (y := round(ball.ycor(), 1)) in m.keys() and 0.5 < ball.xcor() < 7.49:
        rx = round(ball.xcor())
        if (b := boxes[m[y]][rx - 1]) != "done":
            box.clearstamp(b)
            boxes[m[y]][rx - 1] = "done"
            ball.dy *= -1
    return missed


def move_ball(
    ball: turtle.Turtle,
    screen: turtle.Screen,
    paddle: turtle.Turtle,
    boxes: list,
    box: turtle.Turtle,
    start: float,
    missed: int,
):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Bounce sides
    if ball.xcor() > 7.9 or ball.xcor() < 0:
        ball.dx *= -1
    # Bounce top
    if ball.ycor() > 5.9:
        ball.dy *= -1
    screen.update()
    missed = check_collision(ball, paddle, boxes, box, missed)
    if all(i == "done" for row in boxes for i in row):
        ball.goto(4, 3.5)
        ball.color("white")
        m, s = divmod(time.perf_counter() - start, 60)
        ball.write(
            f"Game over. Took {m:.0f} minute(s) and {s:.1f} seconds.\n\tYou missed the ball {missed} times.",
            align="center",
            font=("Arial", 21, "normal"),
        )
    else:
        screen.ontimer(lambda: move_ball(ball, screen, paddle, boxes, box, start, missed), 1)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.setworldcoordinates(0, 0, 8, 6)
    screen.title("Breakout")
    screen.bgcolor("#000000")

    paddle = turtle.Turtle()
    paddle.goto(4, 0)
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("grey")
    paddle.shapesize(1, 6)
    paddle.up()

    ball = turtle.Turtle()
    ball.goto(4, 3)
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.up()
    ball.dx = random.choice([0.005, 0.004, -0.005, -0.004])
    ball.dy = random.choice([0.005, 0.004, -0.005, -0.004])

    box = turtle.Turtle(visible=False)
    box.speed(0)
    box.shape("square")
    box.up()
    box.shapesize(1, 4)

    boxes = []
    for i, y in enumerate([5.8, 5.5, 5.2]):
        boxes.append([])
        for x in range(7):
            box.color(random.choice(["blue", "green", "yellow", "orange"]))
            box.goto(x + 1, y)
            boxes[i].append(box.stamp())

    screen.onkeypress(lambda: move("left", paddle, screen), "Left")
    screen.onkeypress(lambda: move("right", paddle, screen), "Right")
    screen.tracer(0)

    move_ball(ball, screen, paddle, boxes, box, time.perf_counter(), 0)

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
