import turtle
import random


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


def move(direction: str, board: list):
    # if direction in ["u", "d"]:
    #     for i in range(3):
    #         for j in range(3):
    #             if (board[i][j] == board[i + 1][j]) and board[i][j] != 0:
    #                 ...

    for i in range(3):
        for j in range(3):
            if (board[i][j] == board[i][j + 1]) and board[i][j] != 0:
                print("yes")


def setup_board():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 0, 0, 0],
    ]
    board[random.randint(0, 3)][random.randint(0, 3)] = 2
    board[random.randint(0, 3)][random.randint(0, 3)] = 2
    return board


def main():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 4, 4)
    screen.title("2048")
    screen.bgcolor("#c0b3a6")

    board = setup_board()
    draw_board(board)

    screen.onkey(lambda: move("u", board), "Up")
    screen.onkey(lambda: move("d", board), "Down")
    screen.onkey(lambda: move("l", board), "Left")
    screen.onkey(lambda: move("r", board), "Right")

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
