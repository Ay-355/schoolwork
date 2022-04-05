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


def draw_numbers(pointer: turtle.Turtle, board: list, screen: turtle.Screen, final: list, turns: list):
    pointer.clear()
    for x in range(4):
        for y in range(4):
            pointer.goto(x + 0.5, y + 0.32)
            cur = board[::-1][y][x]
            if cur != 0:
                pointer.write(cur, align="center", font=("Arial", 34, "normal"))
    screen.update()

    if board == final:
        pointer.goto(2, 2)
        pointer.color("white")
        pointer.write(f"You got it! Took you {turns[0]} turns.", align="center", font=("Arial", 29, "bold"))


def move_click(x: float, y: float, board: list, text: turtle.Turtle, screen: turtle.Screen, final: list, turns: list):
    if board == final:
        return

    ix, iy = None, None
    for i in range(4):
        if 0 + i <= x < 1 + i:
            ix = i
    for i in range(4):
        if 0 + i <= y < 1 + i:
            iy = i
    if any(i is None for i in [ix, iy]):
        return
    iy = [3, 2, 1, 0].index(iy)

    for i in range(4):
        for j in range(4):
            if board[j][i] == 0:
                ex, ey = i, j

    if ((ey + 1 == iy or ey - 1 == iy) and ex == ix) or ((ex + 1 == ix or ex - 1 == ix) and ey == iy):
        board[ey][ex], board[iy][ix] = board[iy][ix], 0
        turns[0] += 1

    draw_numbers(text, board, screen, final, turns)


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
    text.up()

    turns = [0]
    final_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    board = [i for j in final_board for i in j]
    random.shuffle(board)
    board = [board[i:i + 4] for i in range(0, len(board), 4)]

    draw_board()
    draw_numbers(text, board, screen, final_board, turns)

    screen.onclick(lambda x, y: move_click(x, y, board, text, screen, final_board, turns))
    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
