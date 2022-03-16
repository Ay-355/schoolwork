import random
import turtle


def draw_board():
    pointer = turtle.Turtle(visible=False)
    pointer.speed(0)
    pointer.color("#425CCD")
    pointer.width(7)

    def line(x: float, y: float):
        pointer.up()
        pointer.goto(x, y)
        pointer.down()
        pointer.forward(4)

    for i in range(1, 4):
        line(-0.04, i)
    pointer.left(90)
    for i in range(1, 4):
        line(i, -0.04)


def draw_numbers(pointer: turtle.Turtle, board: list):
    for i in range(4):
        for j in range(4):
            pointer.up()
            pointer.goto(i + 0.5, j + 0.32)
            pointer.down()
            cur = board[::-1][j][i]
            if cur != 0:
                pointer.write(cur, align="center", font=("Arial", 34, "normal"))


def check_win():
    ...


def main():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 4, 4)
    screen.title("15 Puzzle")
    screen.bgcolor("#101113")

    text = turtle.Turtle(visible=False)
    text.speed(0)
    text.color("#425CCD")

    # final
    final_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    draw_board()
    draw_numbers(text, final_board)

    screen.onclick(print)
    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
