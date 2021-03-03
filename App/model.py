"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    catalog={ "videos" : None,
               "Category" : None}

    catalog["videos"] = lt.newList(tipo)
    catalog["Category"]=lt.newList(tipo)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):
    lt.addLast(catalog["videos"],video)

def addCategory(catalog,category):
    category["name"]=category["name"].strip()
    lt.addLast(catalog["Category"],category)
    

# Funciones para creacion de datos

def newCategory(id,name):
    diccionario={ "id": id,"name":name}
    return diccionario

# Funciones de consulta
def getCategoryNumber(nombre,catalog):
    categorias=catalog["Category"]
    size=lt.size(categorias)
    
    for i in range(1,size+1):
        elemento=lt.getElement(categorias,i)
        if elemento["name"]==nombre:
            return int(elemento["id"])
    return -1
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViewsDescendant(video1,video2):
   return int(video1["views"])< int(video2["views"])

def cmpVideosByvViewsAscendant(video1,video2):
    return int(video1["views"])>int(video2["views"])

def cmpVideosByCountry(pais,video):
    return str(video["country"])==str(pais)
def cmpVideosByCategory(numero,video):
    return int(video["category_id"])==int(numero)
# Funciones de ordenamiento




def reduceList(catalog,size):
    reduced=lt.subList(catalog["videos"],0,size)
    return reduced

def selectionSort(lista,ascendente):
    
    start_time = time.process_time()
    if ascendente:
        se.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    else:
        se.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def insertionSort(lista,ascendente):
    start_time = time.process_time()
    if ascendente:
        si.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    else:
        si.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def shellSort(lista,ascendente):
    start_time = time.process_time()
    if ascendente:
        sa.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    else:
        sa.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def mergeSort(lista,ascendente):
    start_time = time.process_time()
    if ascendente:
        ms.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    else:
        ms.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def quicksort(lista,ascendente):
    start_time = time.process_time()
    if ascendente:
        qs.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    else:
        qs.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

# Funciones para reducir datos


def listaPorCategoriaPaises(pais,categoria,tamano,tipo,catalog):
    start_time = time.process_time()
    lista=catalog["videos"]
    size=lt.size(lista)

    if tipo==1:
        ordenada=selectionSort(lista,True)
    elif tipo==2:
        ordenada=insertionSort(lista,True)
    elif tipo==3:
        ordenada=shellSort(lista,True)
    elif tipo==4:
        ordenada=quicksort(lista,True)
    elif tipo==5:
        ordenada=mergeSort(lista,True)
    
    numero=getCategoryNumber(categoria,catalog)
    tamano=int(tamano)
    contador=1
    recorredor=1
    size=lt.size(ordenada[0])
    while (contador<=tamano or recorredor>size):
        video=lt.getElement(ordenada[0],recorredor)
        if cmpVideosByCategory(numero,video) and cmpVideosByCountry(pais,video):
            lt.exchange(ordenada[0],recorredor,contador)
            contador+=1
        recorredor+=1

    if tamano!=1:
        lista_total=lt.subList(ordenada[0],1,contador-1)
    else:
        lista_total=lt.subList(ordenada[0],1,contador)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista_total, elapsed_time_mseg





    