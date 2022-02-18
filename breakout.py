import turtle
import random
import time


def move(direction: str, paddle: turtle.Turtle, screen: turtle.Screen):
    if paddle.xcor() > 7 and direction == "right":
        return
    elif paddle.xcor() < 1 and direction == "left":
        return
    paddle.setx(paddle.xcor() + (0.5 if direction == "right" else -0.5))
    screen.update()


def check_collision(ball: turtle.Turtle, paddle: turtle.Turtle, boxes: list, box: turtle.Turtle):
    # ball and paddle 
    if ball.ycor() < 0.2 and ball.xcor() > paddle.xcor() - 0.65 and ball.xcor() < paddle.xcor() + 0.55:
        ball.dy *= -1
    # ball does not hit paddle 
    if ball.ycor() < -0.15:
        ball.goto(4, 3)
        time.sleep(1)

    # ball hits brick
    m = {5.7: 0, 5.4: 1, 5.1: 2}
    # if want to double check top -   if (y := round(ball.ycor(), 1) - 0.2) in m.keys():
    if (y := round(ball.ycor(), 1)) in m.keys() and 0.5 < ball.xcor() < 7.49:
        rx = round(ball.xcor())
        if (b := boxes[m[y]][rx - 1]) != "done":
            box.clearstamp(b)
            boxes[m[y]][rx - 1] = "done"
            ball.dy *= -1


def move_ball(ball: turtle.Turtle, screen: turtle.Screen, paddle: turtle.Turtle, boxes: list, box: turtle.Turtle):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Bounce sides 
    if ball.xcor() > 7.9 or ball.xcor() < 0:
        ball.dx *= -1
    # Bounce top 
    if ball.ycor() > 5.9:
        ball.dy *= -1
    screen.update()
    check_collision(ball, paddle, boxes, box)
    if all(i == "done" for row in boxes for i in row):
        print("game over")
        return
    else:
        screen.ontimer(lambda: move_ball(ball, screen, paddle, boxes, box), 1)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.setworldcoordinates(0, 0, 8, 6)
    screen.title("Breakout")
    screen.bgcolor("#000000")

    boxes = []

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

    for i, y in enumerate([5.8, 5.5, 5.2]):
        boxes.append([])
        # 1-7 
        for x in range(7):
            box.color(random.choice(["blue", "green", "yellow"]))
            box.goto(x + 1, y)
            boxes[i].append(box.stamp())

    screen.onkeypress(lambda: move("left", paddle, screen), "Left")
    screen.onkeypress(lambda: move("right", paddle, screen), "Right")
    screen.onclick(print)
    screen.tracer(0)

    move_ball(ball, screen, paddle, boxes, box)

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
