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


def check_collision(ball: turtle.Turtle, paddle: turtle.Turtle, boxes: list, box: turtle.Turtle):
    # ball and paddle
    if ball.ycor() < 0.3 and ball.xcor() > paddle.xcor() - 0.65 and ball.xcor() < paddle.xcor() + 0.55:
        ball.dy *= -1
    if ball.ycor() < -0.2:
        ball.goto(5, 5)
        time.sleep(1)

    m = {11.5: 0, 11: 1, 10.5: 2}
    if ball.ycor() > 10.3:
        # if (b := boxes[int(ball.ycor() - 11.5)][int(ball.xcor() - 0.45)]) != "done":
        if (b := boxes[m[round(ball.ycor() * 2)/2]][int(ball.xcor() - 0.45)]) != "done":
            box.clearstamp(b)
            boxes[m[round(ball.ycor() * 2)/2]][int(ball.xcor() - 0.45)] = "done"
            ball.dy *= -1
 

def move_ball(ball: turtle.Turtle, screen: turtle.Screen, paddle: turtle.Turtle, boxes: list, box: turtle.Turtle):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Bounce sides 
    if ball.xcor() > 9.9 or ball.xcor() < 0:
        ball.dx *= -1
    # Bounce top 
    if ball.ycor() > 11.7:
        ball.dy *= -1
    screen.update()
    check_collision(ball, paddle, boxes, box)
    screen.ontimer(lambda: move_ball(ball, screen, paddle, boxes, box), 1)


def main():
    screen = turtle.Screen()
    screen.setup(900, 700)
    screen.setworldcoordinates(0, 0, 10, 12)
    screen.title("Breakout")
    screen.bgcolor("#000000")

    boxes = []

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
    ball.dx = random.choice([0.005, 0.004, -0.005, -0.004])
    ball.dy = random.choice([0.005, 0.004, -0.005, -0.004])

    box = turtle.Turtle(visible=False)
    box.speed(0)
    box.shape("square")
    box.up()
    box.shapesize(1, 4)

    for i, y in enumerate([11.5, 11, 10.5]):
        boxes.append([])
        for x in range(10):
            box.color(random.choice(["blue", "green", "yellow"]))
            box.goto(x + 0.45, y)
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
