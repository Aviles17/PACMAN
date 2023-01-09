import Graficos
import time
import random
import Mapas
import Opciones_Exe
'''
########################################################################################################################################
Hacer lectura de los parametros de ejecucion del juego
########################################################################################################################################
'''
Modo_Juego,Mapa,Estad = Opciones_Exe.Interprete_Opciones()    
'''
########################################################################################################################################
Establecer piezas de mapa y retribucion de graficos por partes del archivo Graficos.py
########################################################################################################################################
'''    
vidas = 3 #Numero de vidas que tiene el jugadar para completar el laberinto
puntaje = 0 #Puntaje inical del juego
window = Graficos.InicializarVentana()
pen = Graficos.InicializarHUD(vidas,puntaje)
lines, map = Mapas.GenerarMapa(Mapa)
if(Modo_Juego == 's'):
    pacman = Graficos.CrearActorPacman()
    dots = Graficos.InicializarComida()
else:
    Recorrido_Cart, Tiempo_Calc_AI = Mapas.GenerarGrafo(map,Modo_Juego)
    pacman = Graficos.CrearActorPacmanGoto(Recorrido_Cart[0])
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
if(Modo_Juego == 's'):
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
                    
if(Modo_Juego == 'd' or Modo_Juego == 'm'):
    while(True):                
        #IA guiada por Algoritmo de Dijkstra o Manhattan
        Contador = 0
        Start_time = time.time()
        while(pacman.distance(Recorrido_Cart[len(Recorrido_Cart)-1][0],Recorrido_Cart[len(Recorrido_Cart)-1][1]) > 15):
            window.update()
            X1 = Recorrido_Cart[Contador][0]
            X2 = Recorrido_Cart[Contador+1][0]
            Y1 = Recorrido_Cart[Contador][1]
            Y2 = Recorrido_Cart[Contador+1][1]
            if(pacman.distance(X2,Y2) < 15):
                Contador += 1
            if(X1 - X2 < 0):
                MovimientoDer()
            if(X1 - X2 > 0):
                MovimientoIz()
            if(Y1 - Y2 < 0):
                MovimientoArriba()
            if(Y1 - Y2 > 0):
                MovimientoAbajo()
            if(Contador + 1 >= len(Recorrido_Cart)):
                break
            Graficos.movement(pacman)
        pacman.direction = 'stop'
        Finish_time = time.time()
        Graficos.movement(pacman)
        time.sleep(1)
        break
    if(Estad == True):
        print("############################################################################################")
        print("                                          REPORTE                                           ")
        print("############################################################################################")
        print("CANTIDAD DE NODOS VISITADOS :" + str(len(Recorrido_Cart)))
        print("TIEMPO EN RECORRIDO : " + str(Finish_time - Start_time))
        print("TIEMPO EN CALCULAR RECORRIDO : " + str(Tiempo_Calc_AI))
        print("/n")