import turtle as t

from freegames import line


def grid():
    # Dibujar una cuadrícula de tres en raya
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    t.color("blue")
    t.width(5)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    t.color("red")
    t.width(5)
    t.up()
    t.goto(x + 67, y + 15)
    t.down()
    t.circle(52)


def floor(value):
    # Redondear el valor a la cuadrícula con un tamaño cuadrado de 133
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = [[None, None, None], [None, None, None], [None, None, None]]


def tap(x, y):
    # Dibujar X o O en el cuadrado pulsado
    x = floor(x)
    y = floor(y)
    player = state['player']

    # Validar si una casilla ya se encuentra ocupada
    if board[int((y + 200) // 133)][int((x + 200) // 133)] is None:
        draw = players[player]
        draw(x, y)
        t.update()
        board[int((y + 200) // 133)][int((x + 200) // 133)] = player
        state['player'] = not player


t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
grid()
t.update()
t.onscreenclick(tap)
t.done()
