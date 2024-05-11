"""
Este es un códgo modificado para emular
el videojuego memoria. Las modificaciones
con respecto al código fueron dos:
1. Contar las veces de taps durante el juago.
2. Identificar cuando se han volteado todos los
   cuadrados.
"""

from random import shuffle
import turtle
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable para contar los taps


def square(x, y):
    """Dibujar un rectángulo gris con borde negro en (x, y)."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """Convertir coordenadas (x, y) al índice de mosaicos."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convertir índice a coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualizar marca y ocultar según lo escogido."""
    global tap_count
    tap_count += 1  # Incrementar el contador de taps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def all_uncovered():
    """Verificar si todos los cuadros están destapados."""
    for count in range(64):
        if hide[count]:
            return False
    return True


def draw():
    """Dibujar imagen, cuadros y número de taps."""
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps
    turtle.goto(-180, 180)  # Posición para mostrar el número de taps
    turtle.color('black')
    turtle.write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

    if all_uncovered():
        turtle.goto(-120, -200)
        turtle.write("¡Felicidades, terminaste!", font=('Arial', 16, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)


shuffle(tiles)
turtle.setup(420, 420, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
