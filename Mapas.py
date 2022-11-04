
import turtle
from freegames import line
import numpy as np

'''
########################################################################################################################################
Rutina de codigo para inicializar una pantalla en negro con turtle
########################################################################################################################################
'''
window = turtle.Screen()
window.tracer(0)
window.title("Pacman AI Implementation")
window.bgcolor('black')
window.setup(600,600)
'''
########################################################################################################################################
Rutina de codigo para inicializar el laberinto en pantalla
########################################################################################################################################
'''
map = np.array([[1,1,1,1,1,1,1,1,1,1],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [2,0,0,0,0,0,0,0,0,2],
               [1,1,1,1,1,1,1,1,1,1]])
lines = []
InicialX = -260
InicialY = 280
for i in range(10):
    for j in range(10):
        if(map[i][j] == 1): #Se dibuja una linea horizontal
            p1 = (InicialX,InicialY)
            p2 = (InicialX + 56*(j),InicialY)
            Limit = turtle.Turtle()
            Limit.speed(0)
            Limit.penup()
            Limit.color('blue')
            Limit.goto(p1)
            Limit.pendown()
            Limit.goto(p2)
            Limit.hideturtle()
            lines.append(Limit)
        if(map[i][j] == 2): #Se dibuja una linea horizontal
            x = (InicialX+ 56*(j),InicialY + 56*(i))
            y = (InicialX+ 56*(j),InicialY - 56*(i))
            Limit = turtle.Turtle()
            Limit.speed(0)
            Limit.penup()
            Limit.color('blue')
            Limit.goto(x)
            Limit.pendown()
            Limit.goto(y)
            Limit.hideturtle()
            lines.append(Limit)
    InicialY -= 56
