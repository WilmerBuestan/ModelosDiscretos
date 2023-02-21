# Diccionario para asociar nombres de estaciones con números
nombres_estaciones = {'Estacion Shangrila': 0, 'Estacion Tigre': 1, 'Estacion Machinaza': 2,
                      'Estacion Coangos': 3, 'Estacion Cenepa': 4, 'Estacion Zafiro': 5,
                      'Estacion Jaguar': 6, 'Estacion RECON': 7}


# Función para calcular las calorias quemadas al recorrer desde una estación de inicio hasta una estación meta
def calorias_recorridos(meta, inicio):
    # Declaración de variables globales
    global grafo, calorias_quemadas
    # Inicialización de una lista para guardar las respuestas
    answer = []
    # Inicialización de una lista para usarse como una cola
    queue = []
    # Inicialización de la lista answer con valores muy grandes
    for i in range(len(meta)):
        answer.append(10**8)
    # Inicialización de la cola con el punto de iniciouer
    queue.append([0, inicio])
    # Inicialización de un diccionario para marcar las estaciones visitadas
    visited = {}
    # Inicialización de un contador para llevar la cuenta de estaciones meta visitadas
    count = 0
    # Mientras haya elementos en la cola
    while (len(queue) > 0):
        # Ordenar la cola
        queue = sorted(queue)
        # Obtener el último elemento de la cola
        p = queue[-1]
        # Eliminar el último elemento de la cola
        del queue[-1]
        # Cambiar el signo del primer elemento de p (representa el costo) para poder ordenar la cola
        p[0] *= -1
        # Si la estación es una meta
        if (p[1] in meta):
            # Encontrar el índice de la meta en la lista de metas
            index = meta.index(p[1])
            # Si aún no se ha encon menor que el costo previamente encontrado para esta meta
            if (answer[index] > p[0]):
                answer[index] = p[0]
            # Eliminar el último elemento de la cola
            #del queue[-1]
            # Ordenar la cola
            queue = sorted(queue)
            # Si se han visitado todas las metas
            if (count == len(meta)):
                # Devolver la respuesta
                return answer
        # Si la estación no ha sido visitada previamente
        if (p[1] not in visited):
            # Imprimir la estación y las calorías quemadas hasta ese punto
            print("Estacion:", p[1], "Calorias:", p[0])
            # Recorrer los vecinos de la estación
            for i in range(len(grafo[p[1]])):
                # Agregar el vecino a la cola con el costo actualizado
                queue.append( [(p[0] + calorias_quemadas[(p[1], grafo[p[1]][i])])* -1, grafo[p[1]][i]])
        visited[p[1]] = 1
    return answer

if __name__ == '__main__':
    # Se inicializa el grafo y las calorias quemadas como diccionarios vacios

    grafo, calorias_quemadas = [[] for i in range(8)], {}
    
    # Se establecen las relaciones entre las estaciones del grafo
    grafo[0].append(1)
    grafo[0].append(3)
    grafo[3].append(1)
    grafo[3].append(6)
    grafo[3].append(4)
    grafo[1].append(6)
    grafo[4].append(2)
    grafo[4].append(5)
    grafo[2].append(1)
    grafo[5].append(2)
    grafo[5].append(6)
    grafo[6].append(4)
    grafo[3].append(7)
    grafo[7].append(5)
    
    # Se establecen las calorias quemadas para cada relacion del grafo
    calorias_quemadas[(0, 1)] = 30
    calorias_quemadas[(0, 3)] = 85
    calorias_quemadas[(1, 6)] = 145
    calorias_quemadas[(3, 1)] = 100
    calorias_quemadas[(3, 6)] = 120
    calorias_quemadas[(3, 4)] = 320
    calorias_quemadas[(2, 1)] = 60
    calorias_quemadas[(4, 2)] = 49
    calorias_quemadas[(4, 5)] = 298
    calorias_quemadas[(5, 2)] = 220
    calorias_quemadas[(5, 6)] = 40
    calorias_quemadas[(6, 4)] = 420
    calorias_quemadas[(3, 7)] = 70
    calorias_quemadas[(7, 5)] = 90
    
    # Se le pide al usuario ingresar la estacion inicial y la meta a llegar
    meta = []
    print("\t*****************************************************************************")
    print("\tBienvenidos al programa de simulacion de Calorias por Recorridos de las ESCIE")
    print("\t*****************************************************************************")
    print("Para la especificacion de las estaciones tendremos numeradas de 0 al 7,siendo la estacion 0 la\ninicial y la 7 la final.Ingresaremos el nombre de la estacion del programa, no el numero:")
    print("\n")
    print("Estacion Shangrila: 0, Estacion Tigre: 1, Estacion Machinaza: 2,\nEstacion Coangos: 3, Estacion Cenepa: 4, Estacion Zafiro: 5, Estacion Jaguar: 6, Estacion RECON: 7")
    inicio_nombre = input("\nIngrese el nombre de la estacion inicial: ")
    inicio = nombres_estaciones[inicio_nombre]
    meta_nombre = input("Ingrese el nombre de la meta a llegar: ")
    meta = [nombres_estaciones[meta_nombre]]
    
    # Se llama a la funcion calorias_recorridos para obtener el consumo minimo de calorias

    answer = calorias_recorridos(meta, inicio)
    # Se imprime el resultado
    print("El consumo minimo de calorias desde la ", inicio_nombre, "hasta ", meta_nombre, "es: ",answer[0]," Kilocalorias")
