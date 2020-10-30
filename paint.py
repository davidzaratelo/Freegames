"""Paint, for drawing shapes.
Exercises
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector
#funcion que traza una línea de determinada longitud dados un punto inicial
#y uno final
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
'''funcion que traza un cuadrado de determinada longitud de lado 
    dados un punto inicial y uno final a traves de un for en donde
    cada iteracion traza una linea y después gira 90 grados
'''
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()
''' Funcion que traza un circulo (enorme generalmente) a través de trazar 360 veces una linea
    y por cada iteración girar 1 grado a la izquierda
'''
def circle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(360):
        forward(end.x - start.x)
        left(1)

    end_fill()
'''Funcion que traza un rectángulo de largo determinado por un punto final y uno inicial
    y el ancho determinado por la mitad del largo
'''
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #for, que determina si el ancho o el largo se va a dibujar segun la iteracion
    for count in range(4):
        if (count % 2 == 0):
            forward(end.x - start.x)
        else:
            forward((end.x / 2) - (start.x / 2))
        left(90)

    end_fill()
'''funcion que traza un triángulo equilátero de longitud determianda por un punto final y uno inicial
    a través de un for que traza una linea y gira 120 a la izquierda (60°) después de trazar
'''
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: width(10), 'w')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()