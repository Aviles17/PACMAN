import sys
'''
########################################################################################################################################
Leer las opciones dentro de la ejecucion del Pacman
########################################################################################################################################
'''
def Interprete_Opciones():
    List_arguments = sys.argv
    if(len(List_arguments) != 7):
        print("Cantidad de argumentos invalida, repita ejecucion")
        sys.exit()
    Comp1 = False
    Comp2 = False
    Comp3 = False
    for index in range(len(List_arguments)):
        if(List_arguments[index] == '-g'):
            Modo_Juego = List_arguments[index+1]
            Comp1 = True
        if(List_arguments[index] == '-m'):
            Mapa = List_arguments[index+1]
            Comp2 = True
        if(List_arguments[index] == '-e'):
            Estad = True
            Comp3 = True
    if(Comp1 == False or Comp2 == False or Comp3 == False):
        print("Cantidad de argumentos digitados no existen dentro del sistema")
        sys.exit()
    else:
        return Modo_Juego,Mapa,Estad
        
            