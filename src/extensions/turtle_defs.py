import turtle as t

type num = int | float

# Screen


def CLEAR() -> None:
    t.clearscreen()


def GET_SCREEN_WIDTH() -> int:
    width, _ = t.screensize()
    return width


def GET_SCREEN_HEIGHT() -> int:
    _, height = t.screensize()
    return height


def SET_SCREEN_SIZE(width: int, height: int) -> None:
    t.screensize(width, height)


# Pen, Colors


def PEN_UP() -> None:
    t.penup()


def PEN_DOWN() -> None:
    t.pendown()


def SET_STROKE_COLOR(color: str) -> None:
    t.color(color)


def SET_FILL_COLOR(color: str) -> None:
    t.fillcolor(color)


def BEGIN_FILL() -> None:
    t.begin_fill()


def END_FILL() -> None:
    t.end_fill()


def BEGIN_POLYGON() -> None:
    t.begin_poly()


def END_POLYGON() -> None:
    t.end_poly()


# Movement


def HOME() -> None:
    t.home()


def GO_FORWARD(steps: num) -> None:
    t.forward(steps)


def TURN_LEFT(degrees: num) -> None:
    t.left(degrees)


def TURN_RIGHT(degrees: num) -> None:
    t.right(degrees)


def CURRENT_X() -> num:
    x, _ = t.position()
    return x


def CURRENT_Y() -> num:
    _, y = t.position()
    return y


def SET_X(x: num) -> None:
    t.setx(x)


def SET_Y(y: num) -> None:
    t.sety(y)


# Control


def WAIT() -> None:
    t.mainloop()


def SET_SPEED(level: int) -> None:
    t.speed(level)


def HIDE_TURTLE() -> None:
    t.hideturtle()


def SHOW_TURTLE() -> None:
    t.showturtle()


# Execute

t.title("Turtle Graphics")
