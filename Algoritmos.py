import numpy as np
from scipy.spatial.distance import cityblock

def Dijkstra_Algorithm(Matriz_Rela,Ori,Dest):
    Recorrido = [Ori]
    Costo_Total = 0
    Canti_Nodos = len(Matriz_Rela[0])
    while(Ori != Dest):
        Minimo = 100000000
        Nodo = 0
        #Comprobar conexiones dentro que tiene el nodo Origen
        Count_Rela = 0
        for i in range(Canti_Nodos):
            if(Matriz_Rela[Ori-1][i] != 0):
                Count_Rela += 1
        #Si hay mas de 1 conexion buscar la que tenga menor carga y que no se haya visitado
        if(Count_Rela > 1):
            for i in range(Canti_Nodos):
                Valor_Temp = Matriz_Rela[Ori-1][i]
                if(Valor_Temp < Minimo and Valor_Temp != 0):
                    Init = False
                #Comprobar si el nodo ya ha sido visitado
                    for n in Recorrido:
                        if(n == i + 1):
                            Init = True
                            
                    if(Init == False):
                        Minimo = Valor_Temp
                        Nodo = i + 1
        #Si tiene 1 obligar al programa a elegir esa ruta aunque se repita
        else:
            for i in range(Canti_Nodos):
                if(Matriz_Rela[Ori-1][i] != 0):
                    Minimo = Matriz_Rela[Ori][i]
                    Nodo = i + 1
        #Actualziar recorrido y variables para proxima iteracion
        if(Nodo != 0 and Minimo != 100000000):
            Recorrido.append(Nodo)
            Costo_Total += Minimo
            Ori = Nodo
        else:
            break
    print(Costo_Total)        
    return Recorrido

def Transformacion_Cartesiana(Recorrido, Mapa,Base_Reguladora = 28):
    #Crear diccionario con las diferentes coordenadas para cada nodo
    Coordenadas_Nodo = {}
    InicialX = -270
    InicialY = 280
    for i in range(20):
        for j in range(20):
            if(Mapa[i][j] > 0):
                Coordx = InicialX + Base_Reguladora*j
                Coordy = InicialY - Base_Reguladora*i
                Coordenadas_Nodo[Mapa[i][j]] = (Coordx,Coordy)
    #Usar diccionario con claves posicionales para traducir el recorrido
    for n in range(len(Recorrido)):
        nodo_b = Recorrido[n]
        for key in Coordenadas_Nodo.keys():
            if(nodo_b == key):
                Recorrido[n] = Coordenadas_Nodo[key]
    
    return Recorrido
    
            
    
def Manhattan_Euristic_Algorithm(Matriz_Rela,Mapa,Ori,Dest,Base_Reguladora = 28):
    #Guardar por nodo sus coordenadas cartesianas
    Coordenadas_Nodo = {}
    InicialX = -270
    InicialY = 280
    for i in range(20):
        for j in range(20):
            if(Mapa[i][j] > 0):
                Coordx = InicialX + Base_Reguladora*j
                Coordy = InicialY - Base_Reguladora*i
                Coordenadas_Nodo[Mapa[i][j]] = (Coordx,Coordy)
    Coordenadas_Nodo[len(Coordenadas_Nodo)]  = (0,0)          
    #Implementar el algoritmo de Dijkstra pero con Euristica (Usando la distancia Manhattan)
    Recorrido = [Ori]
    Costo_Total = 0
    Canti_Nodos = len(Matriz_Rela[0])
    while(Ori != Dest):
        Minimo = 100000000
        Nodo = 0
        #Comprobar conexiones dentro que tiene el nodo Origen
        Count_Rela = 0
        for i in range(Canti_Nodos):
            if(Matriz_Rela[Ori-1][i] != 0):
                Count_Rela += 1
        #Si hay mas de 1 conexion buscar la que tenga menor carga y que no se haya visitado
        if(Count_Rela > 1):
            for i in range(Canti_Nodos):
                Valor_Temp = Matriz_Rela[Ori-1][i]
                if(Valor_Temp != 0):
                    #Calcular valor de la heuristica
                    if(i+1 < len(Coordenadas_Nodo)-1):
                        Punto_1 = [Coordenadas_Nodo[i+1][0],Coordenadas_Nodo[i+1][1]]
                        Punto_2 = [Coordenadas_Nodo[Dest][0], Coordenadas_Nodo[Dest][1]]
                        Heuristica = cityblock(Punto_1,Punto_2)
                        Valor_Temp += Heuristica
                        if(Valor_Temp < Minimo ):
                            Init = False
                        #Comprobar si el nodo ya ha sido visitado
                        for n in Recorrido:
                            if(n == i + 1):
                                Init = True
                            
                        if(Init == False):
                            Minimo = Valor_Temp
                            Nodo = i + 1
        #Si tiene 1 obligar al programa a elegir esa ruta aunque se repita
        else:
            for i in range(Canti_Nodos):
                if(Matriz_Rela[Ori-1][i] != 0):
                    Minimo = Matriz_Rela[Ori][i]
                    Nodo = i + 1
        #Actualziar recorrido y variables para proxima iteracion
        if(Nodo != 0 and Minimo != 100000000):
            Recorrido.append(Nodo)
            Costo_Total += Minimo
            Ori = Nodo
        else:
            break
        
    return Recorrido
    
    
    