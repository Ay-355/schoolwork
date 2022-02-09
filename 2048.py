import turtle


def draw_board(board: list):
    pointer = turtle.Turtle(visible=False)
    pointer.speed(0)
    pointer.color("#ac9c8f")
    pointer.width(7)

    def line(x: float, y: float):
        pointer.up()
        pointer.goto(x, y)
        pointer.down()
        pointer.forward(4)

    line(0, 1)
    line(0, 2)
    line(0, 3)
    pointer.left(90)
    line(1, 0)
    line(2, 0)
    line(3, 0)


def move(direction: str):
    print(direction)


def main():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 4, 4)
    screen.title("2048")
    screen.bgcolor("#c0b3a6")

    draw_board(board)

    screen.onkey(lambda: move("u"), "Up")
    screen.onkey(lambda: move("d"), "Down")
    screen.onkey(lambda: move("l"), "Left")
    screen.onkey(lambda: move("r"), "Right")

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
