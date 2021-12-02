import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.setworldcoordinates(0, 0, 400, 400)

pointer = turtle.Turtle()
pointer.up()
pointer.hideturtle()
pointer.speed(0)


def draw_rect(x, y, length, height):
    pointer.up()
    pointer.goto(x, y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x + length, y)
    pointer.goto(x + length, y + height)
    pointer.goto(x, y + height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()


def draw_brick_wall_offset(rows, cols, brick_width, brick_height, mortar_width):
    width = brick_width + mortar_width
    height = brick_height + mortar_width
    for y in range(rows):
        for x in range(cols):
            if y % 2:
                if x == 0:
                    draw_rect(
                        x * width,
                        y * height,
                        (brick_width - mortar_width) / 2,
                        brick_height,
                    )
                if x == cols - 1:
                    draw_rect(
                        x * width + width / 2,
                        y * height,
                        (brick_width - mortar_width) / 2,
                        brick_height,
                    )
                else:
                    draw_rect(x * width + width / 2, y * height, brick_width, brick_height)
            else:
                draw_rect(x * width, y * height, brick_width, brick_height)


def draw_brick_wall_special(rows, cols, brick_height, mortar_width):
    brick_width = 2 * brick_height
    for y in range(cols):
        for x in range(rows):
            if x % 2 == 0:
                draw_rect(x * (brick_width + mortar_width), y * (brick_height + mortar_width), brick_width, brick_height)
            else:
                if y % 2 == 0:
                    draw_rect(
                        x * (brick_width + mortar_width),
                        y * (brick_height + mortar_width),
                        brick_height - mortar_width / 2,
                        brick_width + mortar_width,
                    )
                    draw_rect(
                        x * (brick_width + mortar_width) + (brick_width + mortar_width) / 2,
                        y * (brick_height + mortar_width),
                        brick_height - mortar_width / 2,
                        brick_width + mortar_width,
                    )


def draw_brick_wall(rows, cols, brick_width, brick_height, mortar_width):
    for y in range(cols):
        for x in range(rows):
            draw_rect(x * (brick_width + mortar_width), y * (brick_height + mortar_width), brick_width, brick_height)


draw_brick_wall(10, 5, 50, 25, 5)
# draw_brick_wall_offset(10, 5, 50, 25, 5)
# draw_brick_wall_special(10, 10, 25, 5)
turtle.done()
