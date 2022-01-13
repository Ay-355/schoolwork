import turtle


def draw_board():
    box = turtle.Turtle(visible=False)
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
    box.goto(0, 6)
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
            return "Square"
        elif sum(x) == -3:
            return "Circle"

    diag = board[0][2] + board[1][1] + board[2][0]
    if diag == 3:
        return "Square"
    elif diag == -3:
        return "Circle"

    diag = sum(board[i][i] for i in range(3))
    if diag == 3:
        return "Square"
    elif diag == -3:
        return "Circle"

    # vertical
    for i in range(3):
        vert = board[0][i] + board[1][i] + board[2][i]
        if vert == 3:
            return "Square"
        elif vert == -3:
            return "Circle"

    # tie
    for i in board:
        if not all([v != 0 for v in i]):
            break
    else:
        return "Tie"


def write_text(content: str, text: turtle.Turtle):
    text.undo()
    text.speed(0)
    text.up()
    text.goto(3, 6.25)
    text.write(content, align="center", font=("Arial", 25, "normal"))


# -1 = circle, 1 = square
def stamp_shape(x: float, y: float, pointer: turtle.Turtle, text: turtle.Turtle):
    # OOP is so much better than globals
    global turn, board, won
    if won is True:
        return
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
    if xr is None or yr is None:
        return write_text("Please hit inside a spot.", text)

    if board[xr][yr] != 0:
        return write_text("Spot already used.", text)
    else:
        board[xr][yr] = turn

    pointer.goto(xa, ya)
    pointer.stamp()
    turn = 1 if turn == -1 else -1
    write_text(f"It is {'square' if turn == 1 else 'circle'}'s turn", text)

    if winner := check_win(board):
        if winner != "Tie":
            write_text(f"{winner} wins the game.", text)
        else:
            write_text("It is a tie", text)
        turtle.title(winner)
        won = True


def main():
    global turn, board, won

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    turn = 1
    won = False

    text = turtle.Turtle(visible=False)

    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0, 0, 6, 7)
    screen.title("Tic Tac Toe")
    screen.clear()

    pointer = turtle.Turtle(visible=False)
    pointer.shapesize(5, 5)
    pointer.penup()
    pointer.pensize(15)
    pointer.speed(0)

    draw_board()
    write_text(f"It is {'square' if turn == 1 else 'circle'}'s turn", text)

    screen.onclick(lambda x, y: stamp_shape(x, y, pointer, text))
    screen.onkey(main, "n")

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
