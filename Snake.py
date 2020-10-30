#Este codigo tiene el poroposito de generar  un juego de snake mediante vectores
#Se importan funciones de libreria turtle, freegames, y random
from turtle import *
from random import randrange
from random import randint
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#La fucnion moveFood tiene el porposito de mover la comida del juego un valor
#a la vez a una direccion aleatoria, cada vez que se mueve la serpeinte.
def moveFood(food):
    XoY = randint (1, 2) #Se genera un numero aleatoria de 1 o 2

    #Si el numero es 1 se mueve una direccion en x aleatoria
    if XoY == 1:
        moveX = randrange (-1, 2, 2) * 10
        if inside(food):
            food.x += moveX
        else:
            food.x += moveX * -1

    #Si el numero es 2 se mueve una direccion en y aleatoria
    if XoY == 2:
        moveY = randrange (-1, 2, 2) * 10
        if inside(food):
            food.y += moveY
        else:
            food.y += moveY * -1

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)
    #Se mueve la comida cada vez que se mueve la serpeinte con moveFood
    ontimer(moveFood(food), 600)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
