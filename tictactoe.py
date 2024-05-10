"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import turtle as t

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    t.color("blue")
    t.width(5)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Draw O player."""
    t.color("red")
    t.width(5)
    t.up()
    t.goto(x + 67, y + 15)
    t.down()
    t.circle(52)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = [[None, None, None], [None, None, None], [None, None, None]]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
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
