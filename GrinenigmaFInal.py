'''
Universidad de las Fuerzas Armadas ESPE
Enunciado: Proyecto primer parcial - Grinenigma 
Fecha de creación: 30/11/2022
Fecha de modificación: 06/12/2022
Github: https://github.com/WilmerBuestan/ModelosDiscretos/tree/main
Descripcion del Juego:
El juego del Grinenigma es un juego de logica proposicional diseñado para 
el empleo de razonamiento matematico y de esta manera logra completar el desafio

Autor:
Wilmer Buestan

Verisión:
VER.1.2
'''

import os
os.system("cls")
def dibujar_grenigrama():
    '''
    Es una funcion la cual nos imprime el dibujo del grenigrama vacio
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
    Si tiene valor de retorno, retorna el dibujo del grenigrama
    para que el usuario se familiarice
    
    '''


    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")
    print("▓    ▓             ▓    ▓  ")
    print("▓    ▓1            ▓    ▓2 ")
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")
    print("      \           /        ")
    print("       \         /         ")
    print("        \       /          ")
    print("         ▓▓▓▓▓▓▓           ")
    print("         ▓     ▓3          ")
    print("         ▓     ▓           ")
    print("         ▓▓▓▓▓▓▓           ")
    print("        /       \          ")
    print("       /         \         ")
    print("      /           \        ")
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")
    print("▓    ▓-------------▓    ▓  ")
    print("▓    ▓4            ▓    ▓5 ")
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")

def imprimir_resultados(numeros):
    '''
          
    Funcion que imprime el dibujo del grinenigrama con los datos que ingreso el usuario e imprime los resultados de las sumas

    Parametros
    ----------
    numeros : lista
        Variable de la cual se imprime los numeros ingresados por el usuario
    '''
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")
    print("▓",numeros[0]," ▓             ▓",numeros[1]," ▓  ")
    print("▓    ▓cuadro1      ▓    ▓cuadro2 ")
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")
    print("      \           /        ")
    print("       \         /         ")
    print("        \       /          ")
    print("         ▓▓▓▓▓▓▓           ")
    print("         ▓",numeros[2],"  ▓           ")
    print("         ▓     ▓cuadro3    ")
    print("         ▓▓▓▓▓▓▓           ")
    print("        /       \          ")
    print("       /         \         ")
    print("      /           \        ")
    print("▓▓▓▓▓▓-------------▓▓▓▓▓▓  ")
    print("▓",numeros[3]," ▓             ▓",numeros[4]," ▓  ")
    print("▓    ▓cuadro4      ▓    ▓cuadro5 ")
    print("▓▓▓▓▓▓             ▓▓▓▓▓▓  ")

    #Sumamos el cuadrado 1,3,5
    suma_cuadrado_1_3_5=numeros[0]+numeros[2]+numeros[4]
    #imprimimos la suma de los cuadrados 1,3,5
    print("La suma del cuadrado 1, cuadrado 3 y el cuadrado 5 es:" ,suma_cuadrado_1_3_5)
    #Sumamos el cuadrado 2,3,4
    suma_cuadrado_2_3_4=numeros[1]+numeros[2]+numeros[3]
    #imprimimos la suma de los cuadrados 2,3,3
    print("La suma del cuadrado 2, cuadrado 3 y el cuadrado 4 es:" ,suma_cuadrado_2_3_4)
    #Sumamos el cuadrado 4,5
    suma_cuadrado_4_5=numeros[3]+numeros[4]
    #imprimimos la suma de los cuadrados 4,5
    print("La suma del cuadrado 4 y el cuadrado 5 es:" ,suma_cuadrado_4_5)

    #si todas las sumas resultaron en 11 entonces se imprimira un mensaje de reconocimiento , caso contrario se imprimira que no todos los cuadrados no suman 11'''
    if(suma_cuadrado_1_3_5==11 and suma_cuadrado_2_3_4==11 and suma_cuadrado_4_5==11):
        print("TODOS LOS NUMEROS SUMAN 11, FELICIDADES!!!")
    else:
        print("No todas las uniones suman 11 o ninguno suma 11")

def ingresar_numero():
    '''
    Funcion donde se valida si es que el numero ingresado por el jugador es entero, si lo que se ingresó no es un numero
    entero entonces el jugador tendra que volver a ingresar un numero

    Retorna
    -------
    Retorna la variable num_cuadrado como un numero entero
    '''
    while True:
        try:
            num_cuadrado=int(input("Que numero desea agregar en el cuadro : "))#se ingresa un dato
            break
        except ValueError:
            print("No ha ingresado un numero entero.")
    return num_cuadrado

def llenar_cuadros_con_numeros():
    '''
    Funcion que llena los cinco cuadros con los numeros que haya ingresado el usuario
    Retorna:
    ------------
    No tiene valores de retorno   
    '''

    #declaramos numeros como lista para guardar los 5 numeros que se hayan ingresado en los cuadrados
    numeros=[]

    #Ingresamos un numero al primer cuadrado
    print("-------------------------------------------------------")
    print("Cuadro superior izquierda(cuadro 1)")
    cuadro1=ingresar_numero()
    #'Mientras el ciclo repetitivo sea verdadero entonces
    while True:
        if(cuadro1==1 or cuadro1==2 or cuadro1==4 or cuadro1==5 or cuadro1==6):
            numeros.append(cuadro1)
            break
        else:
            print("Solo se puede ingresar 1,2,4,5,6")
            cuadro1=ingresar_numero()
    #Ingresamos un numero al segundo cuadrado
    print("-------------------------------------------------------")
    print("Cuadro superior derecha(cuadro 2)")
    cuadro2=ingresar_numero()
    '''Mientras el ciclo repetitivo sea verdadero entonces'''
    while True:
        if(cuadro2!=cuadro1 and(cuadro2==1 or cuadro2==2 or cuadro2==4 or cuadro2==5 or cuadro2==6)):
            numeros.append(cuadro2)
            break
        else:
            print("Solo se puede ingresar 1,2,4,5,6 y no se puede repetir el mismo numero en otro cuadro:")
            cuadro2=ingresar_numero()
    
    #Ingresamos un numero al tercer cuadrado
    print("-------------------------------------------------------")
    print("Cuadro de en medio(cuadro 3)")
    cuadro3=ingresar_numero()
    #Mientras el ciclo repetitivo sea verdadero entonces'''
    while True:
        if((cuadro3!=cuadro1 and cuadro3!=cuadro2) and(cuadro3==1 or cuadro3==2 or cuadro3==4 or cuadro3==5 or cuadro3==6)):
            numeros.append(cuadro3)
            break
        else:
            print("Solo se puede ingresar 1,2,4,5,6 y no se puede repetir el mismo numero en otro cuadro:")
            cuadro3=ingresar_numero()

    #Ingresamos un numero al cuarto cuadrado
    print("-------------------------------------------------------")
    print("Cuadro inferior izquierda(cuadro 4)")
    cuadro4=ingresar_numero()
    #Mientras el ciclo repetitivo sea verdadero entonces
    while True:
        if((cuadro4!=cuadro1 and cuadro4!=cuadro2 and cuadro4!=cuadro3) and(cuadro4==1 or cuadro4==2 or cuadro4==4 or cuadro4==5 or cuadro4==6)):
            numeros.append(cuadro4)
            break
        else:
            print("Solo se puede ingresar 1,2,4,5,6 y no se puede repetir el mismo numero en otro cuadro:")
            cuadro4=ingresar_numero()

    #Ingresamos un numero al quinto cuadrado
    print("-------------------------------------------------------")
    print("Cuadro inferior derecha(cuadro 5)")
    cuadro5=ingresar_numero()
    #Mientras el ciclo repetitivo sea verdadero entonces
    while True:
        if((cuadro5!=cuadro1 and cuadro5!=cuadro2 and cuadro5!=cuadro3 and cuadro5!=cuadro4) and(cuadro5==1 or cuadro5==2 or cuadro5==4 or cuadro5==5 or cuadro5==6)):
            numeros.append(cuadro5)
            break
        else:
            print("Solo se puede ingresar 1,2,4,5,6 y no se puede repetir el mismo numero en otro cuadro:")
            cuadro5=ingresar_numero()

    imprimir_resultados(numeros)

if __name__ == '__main__':
    print("JUEGO DEL GRINENIGMA")
    print('Bienvenido al juego del Grinenigma que es un juego de logica proposicional diseñado para el empleo de razonamiento matematico y de esta manera logra completar el desafio')
    print(' ')
    print("INDICACIONES:")
    print("1. Debera colocar los siguientes numeros: 1,4,5,2,6 en el siguiente grafico para que todas las lineas sumen 11")
    print("2. Los cuadros tienen un numero para que se guien en donde poner el numero")
    print("")
    dibujar_grenigrama()
    print("")
    os.system("pause")
    os.system("cls")
    llenar_cuadros_con_numeros()