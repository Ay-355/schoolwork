import turtle
import json
from math import inf
from pathlib import Path


def draw_board():
    def line(x: float, y: float):
        box.up()
        box.goto(x, y)
        box.down()
        box.forward(6)

    box = turtle.Turtle(visible=False)
    box.speed(0)
    box.width(2)
    line(0, 2)
    line(0, 4)
    line(0, 6)
    box.left(90)
    line(2, 0)
    line(4, 0)


def check_win(board: list):
    # horizontal
    for x in board:
        if sum(x) == 3:
            return "Square"
        elif sum(x) == -3:
            return "Circle"

    # diagonal
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


def empty_spots(board: list):
    return [(y, x) for y in range(3) for x in range(3) if board[y][x] == 0]


def minimax(board: list, spots: int, turn: int):
    if turn == -1:
        best = [-1, -1, inf]
    else:
        best = [-1, -1, -inf]

    if (winner := check_win(board)) or spots == 0:
        m = {"Square": 1, "Circle": -1, "Tie": 0}
        return [-1, -1, m[winner]]

    for c in empty_spots(board):
        y, x = c
        board[y][x] = turn
        score = minimax(board, spots - 1, -turn)
        board[y][x] = 0
        score[0], score[1] = y, x
        if turn == -1:
            if score[2] < best[2]:
                best = score
        else:
            if score[2] > best[2]:
                best = score
    return best


def ai_move(board: list, pointer: turtle.Turtle, text: turtle.Turtle):
    global turn, won
    spots = len(empty_spots(board))
    move = minimax(board, spots, -1)

    y, x, _ = move
    board[y][x] = turn
    xmap = {0: 1, 1: 3, 2: 5}
    ymap = {0: 5, 1: 3, 2: 1}

    pointer.shape("circle")
    pointer.goto(xmap[x], ymap[y])
    pointer.stamp()

    turn *= -1
    write_text("It is your turn.", text)

    if winner := check_win(board):
        m = {"Square": "Wow, you won the game somehow", "Circle": "AI wins the game.", "Tie": "It's a tie"}
        write_text(m[winner], text)
        turtle.title(winner)
        won = True


# 1 = square, -1 = circle
def stamp_shape(x: float, y: float, pointer: turtle.Turtle, text: turtle.Turtle, mode: str):
    global turn, board, won
    if won is True:
        return
    if mode == "u" and turn == -1:
        return

    pointer.shape("square" if turn == 1 else "circle")
    xr, yr = None, None
    xmap = {0: 1, 1: 3, 2: 5}
    ymap = {0: 5, 1: 3, 2: 1}

    if 0 < x < 2:
        xr = 0
    elif 2 < x < 4:
        xr = 1
    elif 4 < x < 6:
        xr = 2

    if 0 < y < 2:
        yr = 2
    elif 2 < y < 4:
        yr = 1
    elif 4 < y < 6:
        yr = 0

    # don't count if they hit outside square
    if xr is None or yr is None:
        return write_text("Please hit inside a spot.", text)

    if board[yr][xr] != 0:
        return write_text("Spot already used.", text)
    else:
        board[yr][xr] = turn

    pointer.goto(xmap[xr], ymap[yr])
    pointer.stamp()

    turn *= -1
    write_text(f"It is {'square' if turn == 1 else 'circle'}'s turn", text)

    if winner := check_win(board):
        if winner != "Tie":
            write_text(f"{winner} wins the game.", text)
        else:
            write_text("It is a tie.", text)
        turtle.title(winner)
        won = True
    elif mode == "u":
        write_text("AI is thinking.", text)
        ai_move(board, pointer, text)


def load(pointer: turtle.Turtle, text: turtle.Turtle):
    global board, turn

    if not Path("saved_ttt.txt").is_file():
        return write_text("Couldn't find a saved game.", text)
    with open("saved_ttt.txt") as f:
        board = json.load(f)

    pointer.clearstamps()
    used = [(y, x) for y in range(3) for x in range(3) if board[y][x] != 0]
    xmap = {0: 1, 1: 3, 2: 5}
    ymap = {0: 5, 1: 3, 2: 1}
    am = 0

    for y, x in [_ for _ in used]:
        pointer.shape("square" if board[y][x] == 1 else "circle")
        am += board[y][x] 
        pointer.goto(xmap[x], ymap[y])
        pointer.stamp()
    if am <= 0:
        turn = 1
    else:
        turn = -1
    write_text(f"Loaded game. {'Square' if turn == 1 else 'Circle'}'s turn.", text)
    


def save(board: list, text: turtle.Turtle):
    if check_win(board):
        return write_text("Can't save game that is over.", text)
    with open("saved_ttt.txt", "w") as f:
        f.write(str(board))
    write_text("Saved game state.", text)


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
    write_text("Normal or Unbeatable AI?", text)

    mode = screen.textinput("Mode", "[N]ormal 2v2 or [U]nbeatable AI? Default: Normal")
    if mode == "n":
        write_text(f"It is {'square' if turn == 1 else 'circle'}'s turn.", text)
    elif mode == "u":
        write_text("It is your turn.", text)
    else:
        mode = "n"
        write_text(f"It is {'square' if turn == 1 else 'circle'}'s turn.", text)

    screen.onclick(lambda x, y: stamp_shape(x, y, pointer, text, mode))
    screen.onkey(main, "n")

    screen.onkey(lambda: load(pointer, text), "l")
    screen.onkey(lambda: save(board, text), "s")

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
