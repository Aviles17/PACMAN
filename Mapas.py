'''
########################################################################################################################################
Ester archivo tiene como proposito el probar generacion de mapa, no influye en la ejecucion de Pacman.py
########################################################################################################################################
'''
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
map = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
lines = []
InicialX = -270
InicialY = 280
for i in range(20):
    for j in range(20):
        if(map[i][j] == 1): #Generar lineas horizontales
            Limit = turtle.Turtle()
            Limit.speed(0)
            Limit.shape("square")
            Limit.color('blue')
            Limit.penup()
            Limit.goto(InicialX + 28*(j),InicialY)
            Limit.pendown()
            Limit.shapesize(stretch_len= 2.3, stretch_wid= 0.5)
            lines.append(Limit)
        if(map[i][j] == 2): #Generar lineas verticales
            Limit = turtle.Turtle()
            Limit.speed(0)
            Limit.shape("square")
            Limit.color('blue')
            Limit.penup()
            Limit.goto(InicialX + 28*(j),InicialY)
            Limit.pendown()
            Limit.shapesize(stretch_len= 0.5, stretch_wid= 2.3)
            lines.append(Limit)    
    InicialY -= 28 #Pasar a la siguiente linea 
        
while True:
    window.update()

