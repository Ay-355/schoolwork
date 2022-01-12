import turtle


def draw_board():
    box = turtle.Turtle()
    box.hideturtle()
    box.speed(0)
    box.width(2)
    box.up()
    box.goto(0, 2)
    box.down()
    box.forward(6)
    box.up()
    box.goto(0, 4)
    box.down()
    box.forward(6)
    box.up()
    box.left(90)
    box.goto(2, 0)
    box.down()
    box.forward(6)
    box.up()
    box.goto(4, 0)
    box.down()
    box.forward(6)
    box.up()


def check_win(board: list):

    # horizontal
    for x in board:
        if sum(x) == 3:
            return "square"
        elif sum(x) == -3:
            return "circle"

    diag = board[0][2] + board[1][1] + board[2][0]
    if diag == 3:
        return "square"
    elif diag == -3:
        return "circle"

    diag = sum(board[i][i] for i in range(3))
    if diag == 3:
        return "square"
    elif diag == -3:
        return "circle"

    # vertical
    for i in range(3):
        vert = board[0][i] + board[1][i] + board[2][i]
        if vert == 3:
            return "square"
        elif vert == -3:
            return "circle"

    # tie
    for i in board:
        if not all([v != 0 for v in i]):
            break
    else:
        return "tie"


# -1 = circle, 1 = square
def stamp_shape(x: float, y: float, pointer: turtle.Turtle):
    # OOP is so much better than globals
    global turn, board
    pointer.shape("square" if turn == 1 else "circle")
    xr, yr = None, None
    if 0 < x < 2:
        xr = 0
        xa = 1
    elif 2 < x < 4:
        xr = 1
        xa = 3
    elif 4 < x < 6:
        xr = 2
        xa = 5

    if 0 < y < 2:
        yr = 0
        ya = 1
    elif 2 < y < 4:
        yr = 1
        ya = 3
    elif 4 < y < 6:
        yr = 2
        ya = 5

    # dont count if they dont hit inside square
    if xr == None or yr == None:
        return

    if board[xr][yr] != 0:
        print("SPOT ALREADY USED")
        return
    else:
        board[xr][yr] = turn

    pointer.goto(xa, ya)
    pointer.stamp()
    turn = 1 if turn == -1 else -1
    if winner := check_win(board):
        print(winner)


def main():
    global turn, board
    turn = 1
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 6, 6)
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    screen.clear()

    pointer = turtle.Turtle()
    pointer.hideturtle()
    pointer.shapesize(5, 5)
    pointer.penup()
    pointer.pensize(15)
    pointer.speed(0)

    draw_board()

    screen.onclick(lambda x, y: stamp_shape(x, y, pointer))
    screen.onkey(main, "n")
    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
