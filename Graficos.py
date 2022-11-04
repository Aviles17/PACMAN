import turtle
import random
import time
from freegames import line
import numpy as np

'''
########################################################################################################################################
Rutina de codigo para inicializar una pantalla en negro con turtle
########################################################################################################################################
'''
def InicializarVentana():
    window = turtle.Screen()
    window.tracer(0)
    window.title("Pacman AI Implementation")
    window.bgcolor('black')
    window.setup(600,600)
    return window
'''
########################################################################################################################################
Rutina de codigo para inicializar el laberinto en pantalla
########################################################################################################################################
'''
def InicializarMapa():
      
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
                #Limit.hideturtle()
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
                #Limit.hideturtle()
                lines.append(Limit)
        InicialY -= 56
    return lines

'''
########################################################################################################################################
Rutina de codigo para inicializar una pantalla con un circulo amarillo (Pacman)
########################################################################################################################################
'''
def CrearActorPacman():
    pacman = turtle.Turtle()
    pacman.speed(0)
    pacman.penup() 
    pacman.color("yellow")
    pacman.shape('circle')
    pacman.direction = 'stop'
    return pacman
'''
########################################################################################################################################
Funcion de codigo para actualizar las coordenadas de Pacman
########################################################################################################################################
'''
def movement(pacman): #Funcion para el movimiento de pacman
    if pacman.direction == 'up':
        y = pacman.ycor() #Obtener la coordenada 'y' de pacman
        y = y + 0.55 #Generar un movimiento en la coordenada
        pacman.sety(y)
    if pacman.direction == 'down':
        y = pacman.ycor() 
        y = y - 0.55 #Generar un movimiento en la coorden
        pacman.sety(y)
    if pacman.direction == 'left': 
        x = pacman.xcor() #Obtener la coordenada 'x' de pacman
        x = x - 0.55
        pacman.setx(x)
    if pacman.direction == 'right':
        x = pacman.xcor()
        x = x + 0.55
        pacman.setx(x)
    if pacman.direction == 'Halt':
        x = pacman.xcor()
        y = pacman.ycor()
        pacman.setx(x)
        pacman.sety(y)
        time.sleep(0.01)
        
        
'''
########################################################################################################################################
Enlazar la actualizacion de coordenadas con la informacion mostrada en pantalla
########################################################################################################################################
'''    
def MovimientoArriba(pacman):
    pacman.direction = 'up'
def MovimientoAbajo(pacman):
    pacman.direction = 'down'
def MovimientoIz(pacman):
    pacman.direction = 'left'
def MovimientoDer(pacman):
    pacman.direction = 'right'
'''
########################################################################################################################################
Configurar entrada por eventos (Entrada por buffer del teclado)
########################################################################################################################################
''' 
def ControlCommands(window):
    window.listen()
    window.onkeypress(MovimientoArriba,'w')   
    window.onkeypress(MovimientoAbajo,'s')
    window.onkeypress(MovimientoIz,'a')
    window.onkeypress(MovimientoDer,'d')
'''
########################################################################################################################################
Inicailizacion de las pepitas dentro del mapa de pacman
########################################################################################################################################
''' 
def InicializarComida():
    dots = []
    for i in range(40):
        dot = turtle.Turtle()
        dot.speed(0)
        dot.penup()
        dot.color('white')
        dot.shape('circle')
        dot.shapesize(stretch_len= 0.4, stretch_wid= 0.4) 
        x = random.randint(-245,230)
        y = random.randint(-190,250)
        dot.setposition(x,y)
        dots.append(dot)
    return dots
        
'''
########################################################################################################################################
Inicailizacion del puntaje y vidas del jugador
########################################################################################################################################
''' 
def InicializarHUD():
    vidas = 3 #Numero de vidas que tiene el jugadar para completar el laberinto
    puntaje = 0 #Puntaje inical del juego

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("grey")
    pen.penup()
    pen.goto(0,-275)
    pen.pendown()
    pen.write('Score: {}  Lives: {}'.format(puntaje,vidas),align='center',font=('Courier',20))
    pen.hideturtle()
    return pen
