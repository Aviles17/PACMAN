'''
##############################################################################################################
1.Contenido : Toda la implementacion de los fantasmas de pacman
2.Proposito: Se tiene este archivo para guardar la posible implementacion de estos, ya que para el analisis 
del proyecto estos no son necesarios
3.Forma del documento : En cada funcion se especificara la ubiacion de donde va cada cosa si se llegara a 
incluir, al igual que su funcion
##############################################################################################################
'''
#------------------------------------------------------------------------------------------------------------------
'''
########################################################################################################################################
Inicailizacion de los enemigos dentro del juego (Opcional para el desarrollo del estudio)
Este fragmento de codigo va en las reglas de inicio del juego
########################################################################################################################################
'''   
enemigos = []
for x in range(10):
    enemigo = turtle.Turtle()
    enemigo.penup()
    enemigo.color('red')
    enemigo.shape('turtle')
    enemigo.speed = 0.55
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    enemigo.setposition(x,y)
    enemigos.append(enemigo)

def MovEnemigos():
    for enemigo in enemigos:
        option = random.randint(0,3)
        if(option == 0):
            y = enemigo.ycor()
            x = enemigo.xcor()
            y = y + enemigo.speed
            if(y > 300):
                enemigo.sety(-298)
            else:
                enemigo.sety(y)
        if(option == 1):
            y = enemigo.ycor()
            x = enemigo.xcor()
            x = x + enemigo.speed
            if(x > 300):
                enemigo.setx(-298)
            else:
                enemigo.setx(x)
        if(option == 2):
            y = enemigo.ycor()
            x = enemigo.xcor()
            y = y - enemigo.speed
            if(y < -300):
                enemigo.sety(298)
            else:
                enemigo.sety(y)
        if(option == 3):
            y = enemigo.ycor()
            x = enemigo.xcor()
            x = x - enemigo.speed
            if(x < -300):
                enemigo.setx(298)
            else:
                enemigo.setx(x)
            

#Colision con el enemigo, este fragmento de codigo va en el bucle while del main
for enemigo in enemigos:
    if pacman.distance(enemigo) < 10:
        vidas -= 1
        pen.clear()
        pen.write('Score: {}  Lives: {}'.format(puntaje,vidas),align='center',font=('Courier',20))
        time.sleep(2)
        pacman.goto(0,0)
            
#Esta llamada de funcion va en el bucle while del main y tiene como proposito actualizar la posicion de los enemigos            
MovEnemigos()


