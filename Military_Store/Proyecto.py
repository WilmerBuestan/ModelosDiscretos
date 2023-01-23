import os
from sqlite3 import enable_shared_cache

import fitz
from re import sub

listaClientes = []
listaProductos = []
listaRangos = []
listaUnidades = []
listaFacturas = []
listaDetalles = []

def llenarBlancos(cadena, tam, bandera):
    for x in range(len(cadena), tam,1):
        if (bandera):
            cadena = cadena + " "
        else:
            cadena = " " + cadena
    return cadena

def leerArchivo(tipo):
    if (tipo == 1):
        with open("rangos.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")

                diccionarioRango = dict()
                diccionarioRango = {
                    "codigo" : arreglo[0],
                    "descripcion" : arreglo[1],
                    "abreviatura" : arreglo[2][0:len(arreglo[2]) - 1]
                }
                listaRangos.append(diccionarioRango)
    elif (tipo == 2):
        with open("productos.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")
                diccionarioProducto = dict()
                diccionarioProducto = {
                    "codigo" : arreglo[0],
                    "descripcion" : arreglo[1],
                    "precio": arreglo[2],
                    "stock" : int(arreglo[3][0:len(arreglo[3]) - 1])
                }
                listaProductos.append(diccionarioProducto)
    elif (tipo == 3):
        with open("clientes.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")
                diccionarioCliente = dict()
                diccionarioCliente = {
                    "cedula": arreglo[0],
                    "nombre": arreglo[1],
                    "apellido": arreglo[2],
                    "armaServicio": arreglo[3],
                    "estado": arreglo[4],
                    "rango": arreglo[5],
                    "unidadMilitar": arreglo[6][0:len(arreglo[6]) - 1]
                }
                listaClientes.append(diccionarioCliente)
    elif (tipo == 4):
        with open("unidades.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")
                diccionarioUnidad = dict()
                diccionarioUnidad = {
                    "codigo": arreglo[0],
                    "descripcion": arreglo[1][0:len(arreglo[1]) - 1]
                }
                listaUnidades.append(diccionarioUnidad)
    elif (tipo == 5):
        with open("facturas.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")
                diccionarioFactura = dict()
                diccionarioFactura = {
                    "codigo": arreglo[0],
                    "cedula": arreglo[1],
                    "subtotal": arreglo[2],
                    "iva": arreglo[3],
                    "total": arreglo[4][0:len(arreglo[4]) - 1]
                }
                listaFacturas.append(diccionarioFactura)
        with open("detalles.txt") as archivo:
            for linea in archivo:
                arreglo = linea.split(sep=";")
                diccionarioDetalles = dict()
                diccionarioDetalles = {
                    "codFactura": arreglo[0],
                    "codigo": arreglo[1],
                    "producto": arreglo[2],
                    "precio": arreglo[3],
                    "cantidad": arreglo[4],
                    "total": arreglo[5][0:len(arreglo[5]) - 1]
                }
                listaDetalles.append(diccionarioDetalles)

def escribirArchivo(tipo):
    if (tipo == 1):
        archivo = open("clientes.txt", "w")
        for cliente in listaClientes:
            archivo.write(cliente["cedula"] + ";" + cliente["nombre"] + ";" + cliente["apellido"] + ";" + cliente["armaServicio"] + ";" + cliente["estado"] + ";" + cliente["rango"] + ";" + cliente["unidadMilitar"] + "\n")
    elif (tipo == 2):
        archivo = open("productos.txt", "w")
        for producto in listaProductos:
            archivo.write(producto["codigo"] + ";" + producto["descripcion"] + ";" + producto["precio"] + ";" + str(producto["stock"]) + "\n")
    elif (tipo == 3):
        archivo = open("facturas.txt", "w")
        for factura in listaFacturas:
            archivo.write(factura["codigo"] + ";" + factura["cedula"] + ";" + str(factura["subtotal"]) + ";" + str(factura["iva"]) + ";" + str(factura["total"]) + "\n")
        archivo = open("detalles.txt", "w")
        for detalle in listaDetalles:
            archivo.write(str(detalle["codFactura"]) + ";" + detalle["codigo"] + ";" + detalle["producto"] + ";" + str(detalle["precio"]) + ";" + str(detalle["cantidad"]) + ";" + str(detalle["total"]) + "\n")

def verificarCedula(nro):
    l = len(nro)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
                raise Exception(u'Tercer digito invalido')
        else:
            raise Exception(u'Codigo de provincia incorrecto')
    else:
        raise Exception(u'Longitud incorrecta del numero ingresado')

def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver

def buscarCliente(cedula):
    for cliente in listaClientes:
        if (cliente["cedula"] == cedula):
            return True
    return False

def registroClientes():
    diccionarioCliente = dict();
    diccionarioCliente["cedula"] = input("Ingrese cédula:")

    if verificarCedula(diccionarioCliente["cedula"]):

        if buscarCliente(diccionarioCliente["cedula"]) == False:

            diccionarioCliente["nombre"] = input("Ingrese nombre:")
            diccionarioCliente["apellido"] = input("Ingrese apellido:")

            while True:
                print("*******Tipo*******")
                print("1. Arma")
                print("2. Servicios")
                tipo = int(input("Ingrese tipo:"))

                if tipo == 1 or tipo == 2:
                    diccionarioCliente["armaServicio"] = "Arma" if (tipo == 1) else "Servicio"
                    break
                else:
                    print("*********************************")
                    print("******Opcion no contemplada******")
                    print("*********************************")

            while True:
                print("*******Estado*******")
                print("1. Activo")
                print("2. Pasivo")
                estado = int(input("Ingrese tipo:"))

                if estado == 1 or estado == 2:
                    diccionarioCliente["estado"] = "Activo" if (estado == 1) else "Pasivo"
                    break
                else:
                    print("*********************************")
                    print("******Opcion no contemplada******")
                    print("*********************************")

            while True:
                print("*******Rangos Disponibles*******")
                reporteRangos()
                codRango = int(input("Ingrese codigo rango:"))

                if codRango >= 1 and codRango <= len(listaRangos):
                    diccionarioCliente["rango"] = listaRangos[codRango - 1]["descripcion"] + " " + listaRangos[codRango -1]["abreviatura"]
                    break
                else:
                    print("*********************************")
                    print("******Opcion no contemplada******")
                    print("*********************************")

            while True:
                print("*******Unidades Disponibles*******")
                reporteUnidades()

                codUnidad = int(input("Ingrese codigo unidad:"))
                if codUnidad >= 1 and codUnidad <= len(listaUnidades):
                    diccionarioCliente["unidadMilitar"] = listaUnidades[codUnidad - 1]["descripcion"]
                    break
                else:
                    print("*********************************")
                    print("******Opcion no contemplada******")
                    print("*********************************")

            listaClientes.append(diccionarioCliente)
            escribirArchivo(1)
            print("*********************************")
            print("*******Cliente Registrado********")
            print("*********************************")
        else:
            print("*********************************")
            print("*******Cliente ya existe*********")
            print("*********************************")
    else:
        print("*********************************")
        print("******Cédula no es correcta******")
        print("*********************************")

def registroProductos():
    diccionarioProducto = dict()
    diccionarioProducto["codigo"] = str(len(listaProductos) + 1)
    diccionarioProducto["descripcion"] = input("Ingrese descripción:")
    diccionarioProducto["precio"] = input("Ingrese precio:")
    diccionarioProducto["stock"] = int(input("Ingrese sctock:"))

    listaProductos.append(diccionarioProducto)
    escribirArchivo(2)
    print("*********************************")
    print("******Producto Registrado********")
    print("*********************************")

def registroVentas():
    cedula = input("Ingrese cédula:")
    if verificarCedula(cedula):
        if buscarCliente(cedula) == True:
            codigoFactura = len(listaFacturas) + 1
            listaDetallesFactura = []
            while True:
                print("***********Producto***********")
                reporteProductos()
                codigoProducto = int(input("Ingrese codigo producto:"))
                if (codigoProducto >= 1 and codigoProducto <= len(listaProductos)):
                    cantidad = int(input("Ingrese cantidad:"))

                    if (listaProductos[codigoProducto - 1]["stock"] >= cantidad):

                        diccionarioDetalles = {
                            "codFactura" : str(codigoFactura),
                            "codigo" : str(len(listaDetallesFactura) + 1),
                            "codProd" : listaProductos[codigoProducto - 1]["codigo"],
                            "producto" : listaProductos[codigoProducto - 1]["descripcion"],
                            "precio" : listaProductos[codigoProducto - 1]["precio"],
                            "cantidad" : str(cantidad),
                            "total" :  cantidad * float(listaProductos[codigoProducto - 1]["precio"])
                        }
                        listaDetallesFactura.append(diccionarioDetalles)

                        subttotal = 0
                        iva = 0
                        total = 0
                        for detalle in listaDetallesFactura:
                            print()
                            subttotal = subttotal + float(detalle["total"])

                        iva = (subttotal * 12) / 100
                        total = subttotal + iva

                        print("Subtotal: {:.2f}".format(subttotal))
                        print("IVA: {:.2f}".format(iva))
                        print("Total: {:.2f}".format(total))
                    else:
                        print("Cantidad solicitada supera al stock disponible")

                    continua = input("Desea registrar otro producto s/n:")
                    if (continua == 'n' or continua == 'N'):
                        for detalle in listaDetallesFactura:
                            for producto in listaProductos:
                                if (producto["codigo"] == detalle["codProd"]):
                                    producto["stock"] = producto["stock"] - int(detalle["cantidad"])
                            listaDetalles.append(detalle)
                        escribirArchivo(2)

                        diccionarioFactura = {
                            "codigo": str(codigoFactura),
                            "cedula": cedula,
                            "subtotal" : subttotal,
                            "iva" : iva,
                            "total" : total
                        }

                        listaFacturas.append(diccionarioFactura)
                        escribirArchivo(3)
                        print("*********************************")
                        print("*******Factura Registrada********")
                        print("*******Stock Actualizado*********")
                        print("*********************************")
                        break
                        #Mandar a escribir
                else:
                    print("*********************************")
                    print("******Opcion no contemplada******")
                    print("*********************************")
        else:
            print("*********************************")
            print("********Cliente no existe********")
            print("*********************************")
    else:
        print("*********************************")
        print("******Cédula no es correcta******")
        print("*********************************")

def reporteClientes():
    for cliente in listaClientes:
        print(cliente["cedula"] + "\t" + cliente["nombre"] + "\t" + cliente["apellido"])

def reporteProductos():
    for producto in listaProductos:
        print(producto["codigo"] + "\t" + llenarBlancos(producto["descripcion"],30,True) + "\t" + llenarBlancos(str(producto["precio"]),10,False) + "\t" + llenarBlancos(str(producto["stock"]), 10, False))

def reporteVentas():
    total = 0
    for venta in listaFacturas:
        print(venta["codigo"] + "\t" + venta["cedula"] + "\t" + venta["subtotal"] + "\t" + venta["iva"] + "\t"+ "\t" + venta["total"])
        total = total + float(venta["total"])
    print("\nTotal general ventas: " + str(total))

def reporteRangos():
    for rango in listaRangos:
        print(rango["codigo"] + "\t" + rango["descripcion"] + "\t" + rango["abreviatura"])

def reporteUnidades():
    for unidad in listaUnidades:
        print(unidad["codigo"] + "\t" + unidad["descripcion"])

def generaPDF():
    # Nuevo documento
    doc = fitz.open()
    # Nueva página en el documento. Se insertará tras la última página
    pagina = doc.new_page(pno=-1, width=1240, height=1754)
    # Establecemos la posición sobre la que vamos a dibujar
    posicion = fitz.Point(100, 200)
    # Insertamos un texto en la página
    total = 0
    x = 100
    y = 100
    posicion = fitz.Point(x, y)
    pagina.insert_text(posicion, llenarBlancos("N°",7,True) + "\t" + llenarBlancos("Cedula",20,True) + "\t" + llenarBlancos("Cliente",40,True) + "\t \t \t \t \t \t \t \t" + llenarBlancos("Subtotal",15,True) + "\t" + llenarBlancos("Iva",15,True) + "\t" + llenarBlancos("Total",15,True), fontsize=20)
    y = y + 30
    for venta in listaFacturas:
        posicion = fitz.Point(x, y)
        total = total + float(venta["total"])
        clienteAux = ""
        for cliente in listaClientes:
            if (cliente["cedula"] == venta["cedula"]):
                clienteAux = cliente["nombre"] + " " + cliente["apellido"]
                break

        pagina.insert_text(posicion, llenarBlancos(str(venta["codigo"]),7,True) + "\t" + llenarBlancos(str(venta["cedula"]),20,True) + "\t" + llenarBlancos(str(clienteAux),40,True)  + llenarBlancos(str(venta["subtotal"]),15,False) + llenarBlancos(str(venta["iva"]),15,False) + llenarBlancos(str(venta["total"]),15,False) , fontsize=20)
        y = y + 30
    y = y + 30
    posicion = fitz.Point(x, y)
    pagina.insert_text(posicion,"Total general ventas" + str(round(total,2)), fontsize=20)

    # Guardamos los cambios en el documento
    doc.write()
    # Guardamos el fichero PDF
    doc.save("ventas.pdf", pretty=True)
    os.system("ventas.pdf") #Esta linea se puede quitar, se encarga de abrir el archivo pero corta la ejecucion del programa
    menuprincipal()

def cargarDatos():
    leerArchivo(1)
    leerArchivo(2)
    leerArchivo(3)
    leerArchivo(4)
    leerArchivo(5)

def menuprincipal():
    cargarDatos()
    opcion = 0
    while True:
        print("*******Menu Principal*******")
        print(" Military Store es un programa desarrollado en Python que administra un almacén militar. Con él, se puede llevar un registro detallado de los inventarios de armamento, municiones, equipos tácticos y otros suministros críticos. El programa cuenta con una interfaz intuitiva y fácil de usar, lo que permite a los usuarios ingresar y actualizar información de inventario con facilidad. También incluye funciones de búsqueda y filtrado avanzadas para ayudar a los usuarios a encontrar rápidamente los artículos que necesitan.")

        print("1. Registro Clientes")
        print("2. Registro Productos")
        print("3. Generar Ventas")
        print("4. Reporte Clientes")
        print("5. Reporte Productos")
        print("6. Reporte Ventas")
        print("7. Generar PDF")
        print("8. Salir")
        opcion = int(input("Ingrese opcion:"))
        os.system('cls')

        if (opcion == 1):
            registroClientes()
        elif (opcion == 2):
            registroProductos()
        elif (opcion == 3):
            registroVentas()
        elif (opcion == 4):
            reporteClientes()
        elif (opcion == 5):
            reporteProductos()
        elif (opcion == 6):
            reporteVentas()
        elif (opcion == 7):
            generaPDF()
        elif (opcion == 8):
            print("Fin del Programa")
            break
        else:
            print("Opcion no contemplada")

if __name__ == "__main__":
    menuprincipal()

