import turtle

def draw_board():
    pointer = turtle.Turtle("square")
    

def check_win():
    ...

# 1=circle, 2=square
def stamp_shape(x, y, pointer):
    # OOP is so much better than globals
    global turn, board
    pointer.shape("square" if turn % 2 == 0 else "circle")
    xr, yr = None, None
    if round(x) in [0, 1, 2]:
        xr = 0
    elif round(x) in [2, 3, 4]:
        xr = 1
    elif round(x) in [4, 5, 6]:
        xr = 2

    if round(y) in [0, 1, 2]:
        yr = 0
    elif round(y) in [2, 3, 4]:
        yr = 1
    elif round(y) in [4, 5, 6]:
        yr = 2

    if board[xr][yr] == 1:
        print("SQUARE ALREADY USED")
        return
    else:
        board[xr][yr] = 1

    pointer.goto(x, y)
    pointer.stamp()
    turn += 1


def main():
    global turn, board
    turn = 0
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(0,0,6,6)
    board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    screen.clear()
    pointer = turtle.Turtle()
    pointer.hideturtle()
    pointer.shapesize(5, 5)
    pointer.penup()
    pointer.pensize(15)
    pointer.speed(0)

    screen.onclick(lambda x, y: stamp_shape(x, y, pointer))
    screen.onkey(main, "n")
    screen.listen()
    screen.mainloop()

if __name__ == "__main__":
    main()
