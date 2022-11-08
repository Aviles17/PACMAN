import turtle
import random
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
        y = y + 1 #Generar un movimiento en la coordenada
        pacman.sety(y)
    if pacman.direction == 'down':
        y = pacman.ycor() 
        y = y - 1 #Generar un movimiento en la coorden
        pacman.sety(y)
    if pacman.direction == 'left': 
        x = pacman.xcor() #Obtener la coordenada 'x' de pacman
        x = x - 1
        pacman.setx(x)
    if pacman.direction == 'right':
        x = pacman.xcor()
        x = x + 1
        pacman.setx(x)
    #Ajustes de movimiento ligeros para colisiones
    if pacman.direction == 'ColDer':
        x = pacman.xcor()
        y = pacman.ycor()
        x = x - 0.5
        pacman.setx(x)
    if pacman.direction == 'ColIz':
        x = pacman.xcor()
        y = pacman.ycor()
        x = x + 0.5
        pacman.setx(x)
    if pacman.direction == 'ColUp':
        x = pacman.xcor()
        y = pacman.ycor()
        y = y - 0.5
        pacman.sety(y)
    if pacman.direction == 'ColDown':
        x = pacman.xcor()
        y = pacman.ycor()
        y = y + 0.5
        pacman.sety(y)
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
def InicializarHUD(vidas,puntaje):

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("grey")
    pen.penup()
    pen.goto(0,-293)
    pen.pendown()
    pen.write('Score: {}  Lives: {}'.format(puntaje,vidas),align='center',font=('Courier',20))
    pen.hideturtle()
    return pen
