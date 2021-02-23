"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Seleccionar tipo de datos")
    print("1- Cargar información en el catálogo")
    print("2-  Encontrar buenos videos por categoria y pais")
    print("3- Encontrar video tendencia por pais")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar videos con mas likes ")
    print("6- Seleccionar tamaño de la muestra para trabajar")

catalog = None
reducido= None
"""
Menu principal
"""
while True:
    printMenu()
    tipo=""
    inputs = int(input('Seleccione una opción para continuar '))
    if inputs==0:
        x=int(input("Presione 1 para seleccionar arreglos, o 2 para seleccionar listas encadenadas"))
        if x==1:
            tipo="ARRAY_LIST"
        else:
            tipo="SINGLE_LINKED"
    elif inputs == 1:
        print("Cargando información de los archivos ....")
        catalog=controller.initCatalog(tipo)
        controller.loadData(catalog)

    elif inputs == 2:
        size=int(input("Indique el tamaño de la muestra"))
        if size<lt.size(catalog["videos"]):
            reducido=controller.reduceList(catalog,size)  
            print("Seleccione el tipo de ordenamiento iterativo:")
            print("1- selection Sort")
            print("2- Insertion Sort")
            print("3- Shell Sort")
            size=lt.size(reducido)
            tipo=int(input())
            if tipo==1:
                ordenado=controller.selectionSort(reducido)
            elif tipo==2:
                ordenado=controller.insertionSort(reducido)
            elif tipo==3:
                ordenado=controller.shellSort(reducido)
            print(" Para una muestra de " +str(size) + " El tiempo en que se ordenaron los datos fue de : " + str(ordenado[1]) + " milisegundos")
    elif inputs==6:
        size=int(input("Indique el tamaño de la muestra"))
        if size<lt.size(catalog["videos"]):
            reducido=controller.reduceList(catalog,size)  
        

    else:
        sys.exit(0)
sys.exit(0)
