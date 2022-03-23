import random
import turtle


def draw_board(screen: turtle.Screen):
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
    screen.update()


def draw_numbers(pointer: turtle.Turtle, board: list):
    pointer.clear()
    for i in range(4):
        for j in range(4):
            pointer.up()
            pointer.goto(i + 0.5, j + 0.32)
            pointer.down()
            cur = board[::-1][j][i]
            if cur != 0:
                pointer.write(cur, align="center", font=("Arial", 34, "normal"))


def swap(board: list, empty: tuple, spot_y: int, spot_x: int):
    # need to check edges
    ok = True
    if ok:
        board[empty[1]][empty[0]], board[spot_y][spot_x] = board[spot_y][spot_x], board[empty[1]][empty[0]]


def move(board: list, direction: str, text: turtle.Turtle):
    for i in range(4):
        for j in range(4):
            if board[j][i] == 0:
                empty = (i, j)
    if direction == "u": swap(board, empty, empty[1] - 1, empty[0])
    if direction == "d": swap(board, empty, empty[1] + 1, empty[0])
    if direction == "l": swap(board, empty, empty[1], empty[0] - 1)
    if direction == "r": swap(board, empty, empty[1], empty[0] + 1)

    draw_numbers(text, board)
    if board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        print("done")


def move_click(x, y):
    ix = round(x) - 1
    iy = round(y) - 1


def main():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 4, 4)
    screen.title("15 Puzzle")
    screen.bgcolor("#101113")
    screen.tracer(0, 0)

    text = turtle.Turtle(visible=False)
    text.speed(0)
    text.color("#425CCD")

    final_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    board = [i for j in final_board for i in j]
    random.shuffle(board)
    board = [board[i : i + 4] for i in range(0, len(board), 4)]
    draw_board(screen)
    draw_numbers(text, board)

    screen.onkey(lambda: move(board, "u", text), "Up")
    screen.onkey(lambda: move(board, "d", text), "Down")
    screen.onkey(lambda: move(board, "l", text), "Left")
    screen.onkey(lambda: move(board, "r", text), "Right")
    screen.onclick(lambda x, y: move_click(x, y))
    screen.onclick(print)
    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
