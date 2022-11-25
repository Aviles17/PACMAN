import turtle
import numpy as np
import Algoritmos
import sys
import time
def GenerarMapa(opcion):
    if(opcion == 'B'):
        #Mapa Basico (Cuadrado)
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
    if(opcion == 'C'):
        #Mapa Complejo (En progreso)
        map = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,2],
                        [2,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,2],
                        [2,0,2,0,0,0,1,1,1,0,0,1,1,2,0,2,0,1,1,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,1,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,0,2],
                        [2,0,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,0,2],
                        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
    if(opcion == 'E'):
        map = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,1,1,1,1,1,1,1,1,1,1,0,0,0,2],
                        [2,0,0,2,0,2,0,0,2,0,0,0,2,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,2,0,0,0,2,0,0,0,0,0,0,2],
                        [2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,1,0,0,0,2,0,0,0,0,0,1,1,1,1,1,1,1,1,2],
                        [2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                        [2,1,0,0,0,2,1,1,1,1,1,1,0,0,2,0,0,0,0,2],
                        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2],
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
    return lines, map
'''
########################################################################################################################################
Rutina para generar el grafo dirigido
########################################################################################################################################
'''
def GenerarGrafo(map,Modo_Juego):
    Mat_Grafo = np.empty((20,20),int)
    for i in range(20):
        for j in range(20):
            Mat_Grafo[i][j] = 0
    Nodo = 0 # Inicializar el contador de nodos
    for i in range(20):
        for j in range(20):
            if(map[i][j] == 0):
                if(map[i-1][j] != 0 or map[i+1][j] != 0):
                    if(map[i][j-1] != 0 or map[i][j+1] != 0):
                        Mat_Grafo[i][j] = Nodo
                        Nodo += 1
            else:
                Mat_Grafo[i][j] = -1
                
    Mat_Grafo = Auxiliar_Grafo(Mat_Grafo,Nodo) 
    Mat_Grafo, Num_Nodos = ReEnumerarEstruct(Mat_Grafo)
    Relaciones = GenerarMatrizRelaciones(Mat_Grafo,Num_Nodos)
    Ori,Dest = pedirOriDes(Num_Nodos)
    if(Modo_Juego == 'd'):
        Recorrido_Dij, Time = Algoritmos.Dijkstra_Algorithm(Relaciones,Ori,Dest)
        Recorrido_Cart = Algoritmos.Transformacion_Cartesiana(Recorrido_Dij,Mat_Grafo)
    if(Modo_Juego == 'm'):
        Recorrido_Manhattan, Time = Algoritmos.Manhattan_Euristic_Algorithm(Relaciones,Mat_Grafo,Ori,Dest)
        Recorrido_Cart = Algoritmos.Transformacion_Cartesiana(Recorrido_Manhattan,Mat_Grafo)
    return Recorrido_Cart, Time
'''
########################################################################################################################################
Rutina para auxiliar la funcion del grafo para asi completar los nodos 
########################################################################################################################################
'''
def Auxiliar_Grafo(Matriz_Map, Nodo):
    
    for i in range(20):
        for j in range(20):
            #Se encontro un nodo
            if(Matriz_Map[i][j] != 0 and Matriz_Map[i][j] != -1):
                #Evaluar los alrededores verticales hacia la Derecha
                if(Matriz_Map[i][j-1] == -1):
                    Contador = j
                    while(Matriz_Map[i][Contador] != -1):
                        if(Matriz_Map[i][Contador+1] == -1):
                            Matriz_Map[i][Contador] = Nodo
                            Nodo += 1
                            
                        Contador += 1
                #Evaluar los alrededores verticales hacia la Izquierda
                if(Matriz_Map[i][j+1] == -1):
                    Contador = j
                    while(Matriz_Map[i][Contador] != -1):
                        if(Matriz_Map[i][Contador-1] == -1):
                            Matriz_Map[i][Contador] = Nodo
                            Nodo += 1
                            
                        Contador -= 1  
                #Evaluar los alrededores horizontales hacia arriba
                if(Matriz_Map[i-1][j] == -1):
                    Contador = i
                    while(Matriz_Map[Contador][j] != -1):
                        if(Matriz_Map[Contador+1][j] == -1):
                            Matriz_Map[Contador][j] = Nodo
                            Nodo += 1
                            
                        Contador += 1  
                #Evaluar los alrededores horizontales hacia abajo
                if(Matriz_Map[i+1][j] == -1):
                    Contador = i
                    while(Matriz_Map[Contador][j] != -1):
                        if(Matriz_Map[Contador-1][j] == -1):
                            Matriz_Map[Contador][j] = Nodo
                            Nodo += 1
                            
                        Contador -= 1 
    return Matriz_Map 


def ReEnumerarEstruct(Matriz_Map):
    Incializar_Num = 1
    for i in range(20):
        for j in range(20):
            if(Matriz_Map[i][j] != -1 and Matriz_Map[i][j] != 0):
                Matriz_Map[i][j] = Incializar_Num
                Incializar_Num += 1	
    return Matriz_Map, Incializar_Num


def GenerarMatrizRelaciones(Matriz_Map, NumNodos):
    #Inicializar matriz de relaciones
    Relaciones = np.empty((NumNodos,NumNodos),int)
    for i in range(NumNodos):
        for j in range(NumNodos):
            Relaciones[i][j] = 0
    #Comprobacion por si se genera mal la matriz del mapa
    if(NumNodos >= 100):
        print("REINICIAR PROGRAMA, OCURRIO UN ERROR EN LA GENERACION")
        print("No existen " + str(NumNodos) + " nodos")
        sys.exit()
    #Recorrer matriz de mapa para encontrar nodos de forma horizontal
    for i in range(20):
        Ori_Encontrado = False
        Contador = 0
        Nodo_1 = 0
        Nodo_2 = 0
        for j in range(20):
            if(Matriz_Map[i][j] > 0 and Ori_Encontrado == False):
                Nodo_1 = Matriz_Map[i][j]
                Ori_Encontrado = True
                Contador = 0 #Reiniciar contador para poder ver las cargas entre nodos
            if(Matriz_Map[i][j] > 0 and Ori_Encontrado == True and Matriz_Map[i][j] != Nodo_1):
                Nodo_2 = Matriz_Map[i][j]
                Relaciones[Nodo_1-1][Nodo_2-1] = Contador
                Relaciones[Nodo_2-1][Nodo_1-1] = Contador
                Nodo_1 = Nodo_2
            if(Matriz_Map[i][j] == -1):
                Nodo_1 = 0
                Nodo_2 = 0
                Ori_Encontrado == False
            Contador += 1
    #Recorrer la matriz de mapa para encontrar nodos de forma vertical
    for i in range(20):
        Ori_Encontrado = False
        Contador = 0
        Nodo_1 = 0
        Nodo_2 = 0
        for j in range(20):
            if(Matriz_Map[j][i] > 0 and Ori_Encontrado == False):
                Nodo_1 = Matriz_Map[j][i]
                Ori_Encontrado = True
                Contador = 0 #Reiniciar contador para poder ver las cargas entre nodos
            if(Matriz_Map[j][i] > 0 and Ori_Encontrado == True and Matriz_Map[j][i]!= Nodo_1):
                Nodo_2 = Matriz_Map[j][i]
                Relaciones[Nodo_1-1][Nodo_2-1] = Contador
                Relaciones[Nodo_2-1][Nodo_1-1] = Contador
                Nodo_1 = Nodo_2
            if(Matriz_Map[j][i] == -1):
                Nodo_1 = 0
                Nodo_2 = 0
                Ori_Encontrado == False
            Contador += 1
    return Relaciones        
                
'''
########################################################################################################################################
Rutina para pedir nodos a los cuales se les aplicara algoritmos
########################################################################################################################################
'''
def pedirOriDes(NumNodos):
    Ori = 0
    Dest = 0
    while(Ori <= 0 or Ori > NumNodos):
        print("Indique el nodo del cual iniciar el recorrido, existen 1 al " + str(NumNodos) + " nodos posibles :\n")
        Ori = input("Ingrese un numero entre esos valores :\n")
        Ori = int(Ori)
        if(Ori <= 0 or Ori > NumNodos):
            time.sleep(0.5)
            print("El nodo seleccionado no esta en rango")
    print("\n")
    while(Dest <= 0 or Dest > NumNodos):
        print("Indique el nodo con el cual quiere finalizar el recorrido, existen 1 al " + str(NumNodos) + " nodos posibles :\n")
        Dest = input("Ingrese un numero entre esos valores :\n")
        Dest = int(Dest)
        if(Dest <= 0 or Dest > NumNodos):
            time.sleep(0.5)
            print("El nodo seleccionado no esta en rango")
    time.sleep(1)
    return Ori,Dest
        

    
