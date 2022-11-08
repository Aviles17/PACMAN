import Graficos
import time
import random
import Mapas

vidas = 3 #Numero de vidas que tiene el jugadar para completar el laberinto
puntaje = 0 #Puntaje inical del juego

window = Graficos.InicializarVentana()
pacman = Graficos.CrearActorPacman()
pen = Graficos.InicializarHUD(vidas,puntaje)
dots = Graficos.InicializarComida()
lines = Mapas.GenerarMapa('E',True)
'''
########################################################################################################################################
Enlazar la actualizacion de coordenadas con la informacion mostrada en pantalla
########################################################################################################################################
'''    
def MovimientoArriba():
    pacman.direction = 'up'
def MovimientoAbajo():
    pacman.direction = 'down'
def MovimientoIz():
    pacman.direction = 'left'
def MovimientoDer():
    pacman.direction = 'right'
'''
########################################################################################################################################
Configurar entrada por eventos (Entrada por buffer del teclado)
########################################################################################################################################
''' 
window.listen()
window.onkeypress(MovimientoArriba,'w')   
window.onkeypress(MovimientoAbajo,'s')
window.onkeypress(MovimientoIz,'a')
window.onkeypress(MovimientoDer,'d')
#Main (Loop para que el juego funcione)
while True:
    window.update()
    #Colisiones con el borde o limites del mapa
    if(pacman.xcor() > 300):
        pacman.goto(-298,pacman.ycor())
        MovimientoDer()
    if(pacman.xcor() < -300):
        pacman.goto(298,pacman.ycor())
        MovimientoIz()
    if(pacman.ycor() < -300):
        pacman.goto(pacman.xcor(),298)
        MovimientoAbajo()
    if(pacman.ycor() > 300):
        pacman.goto(pacman.xcor(),-298)
        MovimientoArriba()
    
    #Revisar vidas y respawn en el caso de ser 0
    if(vidas==0):
        puntaje = 0
        vidas = 3
        pen.clear()
        pen.write('Score: {}  Lives: {}'.format(puntaje,vidas),align='center',font=('Courier',20))
        time.sleep(1)
        pacman.goto(0,0)
        
    #Comida y la colision con pacman
    for dot in dots:
        if pacman.distance(dot) < 10:
            puntaje += 1
            pen.clear()
            pen.write('Score: {}  Lives: {}'.format(puntaje,vidas),align='center',font=('Courier',20))
            x = random.randint(-245,230)
            y = random.randint(-190,250)
            dot.goto(x,y)
            
    #Colision con los limites del mapa
    for l in lines:
        if pacman.distance(l) < 15:
            #Diferentes acercamientos, diferente comportamiento de colision
            if(pacman.direction == 'right'):
                pacman.direction = 'ColDer'
            if(pacman.direction == 'left'):
                pacman.direction = 'ColIz'
            if(pacman.direction == 'up'):
                pacman.direction = 'ColUp'
            if(pacman.direction == 'down'):
                pacman.direction = 'ColDown'
    
    Graficos.movement(pacman)