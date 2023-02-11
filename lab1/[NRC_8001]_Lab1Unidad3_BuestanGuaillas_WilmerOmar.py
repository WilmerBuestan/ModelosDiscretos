

def Regulador_carreteras():
    '''
    Funcion que sirve para controlar el estado de las carreteras, abriendolas y cerrandolas
    Parametros:
        No hay parametros
    Retorna: 
        Costo
    '''
        #pongo en cero el estadoa ctual de las carreteras osea todas abiertas inicialmente 
    via_estado_actual = {'Putumayo': '0',
                         'Cariamanga': '0',
                         'Milagro': '0',
                         'Azogues': '0'}

    
    #pedimos el estado actual de las carreteras donde 0 es abierto y 1 cerrado
    print("Bienvenido al ingreso del estado dela via, por favor ingresa\nel 0 para abierto y el 1 para cerrado a continuacion: \n")
    via_estado_actual["Putumayo"]=int(input("Proporcinar el estado de la via Putumayo: "))
    via_estado_actual["Cariamanga"]=int(input("Ingrese el estado de la via Cariamanga: "))
    via_estado_actual["Milagro"]=int(input("Ingrese el estado de la via Milagro: "))
    via_estado_actual["Azogues"]=int(input("Ingrese el estado de la via Azogues: "))
        # ubico el costo en cero para inicar la funcion
    costo=0

    #ponemos el estado inicial de la via y dependiendo de la eleccion se le pedira las vias a las cual dirigirse.
    estado_inicial=input("Para iniciar su viaje por favor ingrese las abrevituras indicadas a continuacion: \nPut: Putumayo \nCar: Cariamanga\nMil: Milagro\nAzo: Azogues\nIngresa la abreviatura: ")
    #si escogemos putumayo
    if(estado_inicial=='Put' ):      
        estado_objetivo=input("Ingrese la via que quiere llegar \nCar:Cariamanga\nMil:Milagro\nAzo:Azogues\nElija una opcion:")
    #si escogemos cariamanga
    if(estado_inicial=='Car'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \nPut:Putumayo\nMil:Milagro\nAzo:Azogues\nElija una opcion:")
    
    #si escogemos Milagro
    if(estado_inicial=='Mil'):      
        estado_objetivo=input("Ingrese la via que quiere llegar \nPut:Putumayo\nCar:Cariamanga\nAzo:Azogues\nElija una opcion:")
    #si escogemos Azogues
    if(estado_inicial=='Azo' ):      
        estado_objetivo=input("Ingrese la via que quiere llegar \nPut:Putumayo\nCar:Cariamanga\nMil:Milagro\nElija una opcion:")
    # si putumayo esta como estado inicial
    if(estado_inicial=='Put' ):
        # si el objetivo es cariamanga
        if(estado_objetivo=='Car' ):
            #las dos cerradas suma 200 el costo
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Putumayo Y Cariamanga ya no estan cerradas")
                costo=costo+200
                #una sola suma sola putumayo 100
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                #igual cariamanga esta sola suma 100
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Cariamanga"]==0):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                # si las dos estan abiertas suma 0
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Cariamanga"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
        #En el caso que el objetivo sea milagro
        if(estado_objetivo=='Mil' ):
            # Las dos cerradas suman 200
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Milagro"]==1):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+200
                #solo milagro cerrada suma 100
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Milagro"]==1):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                #solo putumayo cerrada suma 100
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Milagro"]==0):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                #si las dos estan abiertas suma cero
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Milagro"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si el estado objetivo es putumayo azogues
        if(estado_objetivo=='Azo'):
            # si las dos estan cerradas 200
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Azogues"]==1):
                print("Carretera Putumayo Y Azogues ya no estan cerradas")
                costo=costo+200
                #si pututmayo esta abierta y azogues cerrada suma 100
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Azogues"]==1):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                #si putumayo esta cerrado y azogues abierto suma 100
            if(via_estado_actual["Putumayo"]==1 and via_estado_actual["Azogues"]==0):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                # su las dos estan abiertas suma 0
            if(via_estado_actual["Putumayo"]==0 and via_estado_actual["Azogues"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si ahora el estado inicial es cariamanga
    if(estado_inicial=='Car'):
        # estado objetivo es putumayo
        if(estado_objetivo=='Put' ):
            # si las dos estan cerradas suma 200
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Putumayo"]==1):
                print("Carretera Cariamanga Y Putumayo ya no estan cerradas")
                costo=costo+200
                # si cariamanga esta abierto y putumayo cerro suma 100
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Putumayo"]==1):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                # si cariamanga esta cerrada y putumayo abierto suma 100
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Putumayo"]==0):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                #si las dos estan abiertas suma cero
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Putumayo"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si el objetivo ahora es Milagro
        if(estado_objetivo=='Mil' ):
            #si las dos estan cerradas el costo es de 200
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Milagro"]==1):
                print("Carretera Cariamanga Y Milagro ya no estan cerradas")
                costo=costo+200
                # si cariamanga esta abierto y milagro cerrado suma 100
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Milagro"]==1):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                #si cariamanga esta cerrada y milagro abierto suma 100
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Milagro"]==0):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                #si las dos estan abiertas suma cero
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Milagro"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                #si ahora el estado objetivo es azogues
        if(estado_objetivo=='Azo'):
            #las dos cerradas suman 200
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Azogues"]==1):
                print("Carretera Cariamanga Y Azogues ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Azogues"]==1):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Cariamanga"]==1 and via_estado_actual["Azogues"]==0):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                #las dos abiertas suman cero
            if(via_estado_actual["Cariamanga"]==0 and via_estado_actual["Azogues"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
    # estado inicial ahora es Milagro
    if(estado_inicial=='Mil'):
        #estado objetivo es Putumayo
        if(estado_objetivo=='Put' ):
            # las dos cerradas suman 200
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Putumayo"]==1):
                print("Carretera Milagro Y Putumayo ya no esta cerrada")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Putumayo"]==1):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Putumayo"]==0):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                # las dos abiertas suman cero
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Putumayo"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si el estado objetivo es ahora Cariamanga
        if(estado_objetivo=='Car' ):
            #si las dos estan cerradas suman 200
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Milagro Y Cariamanga ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Cariamanga"]==0):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                # si las dos estan abiertas suman cero
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Cariamanga"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si el estado objetivo es Azogues
        if(estado_objetivo=='Azo'):
            # si las dos estan cerradas suman 200
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Azogues"]==1):
                print("Carretera Milagro Y Azogues ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Azogues"]==1):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Milagro"]==1 and via_estado_actual["Azogues"]==0):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                # si las dos estan abiertas suman cero
            if(via_estado_actual["Milagro"]==0 and via_estado_actual["Azogues"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
    #estado inicial Azogues
    if(estado_inicial=='Azo' ):
        # estado objetivo putumayo
        if(estado_objetivo=='Put' ):
            #si las dos estan cerradas suman 200
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Putumayo"]==1):
                print("Carretera Azogues Y Putumayo ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Putumayo"]==1):
                print("Carretera Putumayo ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Putumayo"]==0):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                # si las dos estan abiertan suman cero
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Putumayo"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
                # si el objetivo ahora es Cariamanga
        if(estado_objetivo=='Car' ):
            #si las dos estan cerradas suman 200
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Azogues Y Cariamanga ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Cariamanga"]==1):
                print("Carretera Cariamanga ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Cariamanga"]==0):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                #si las dos estan abiertas suman 0
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Cariamanga"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
        # ahora el objetivo es Milagro
        if(estado_objetivo=='Mil' ):
            #Si las dos estan cerradas suman 200
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Milagro"]==1):
                print("Carretera Azogues Y Milagro ya no estan cerradas")
                costo=costo+200
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Milagro"]==1):
                print("Carretera Milagro ya no esta cerrada")
                costo=costo+100
                # solo una abierta suma 100
            if(via_estado_actual["Azogues"]==1 and via_estado_actual["Milagro"]==0):
                print("Carretera Azogues ya no esta cerrada")
                costo=costo+100
                #si las dos estan abiertas suman cero
            if(via_estado_actual["Azogues"]==0 and via_estado_actual["Milagro"]==0):
                print("Las carreteras se encuentran abiertas")
                costo=costo+0
    # imprimimos el precio de lo que nos costaria abrir la via que necesitamos si estuviera cerrada
    print("El precio que se pagó para abrir las carreteras es de: ",costo,"USD")
if __name__ == '__main__':
    Regulador_carreteras()


    