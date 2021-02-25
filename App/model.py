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
    lt.addLast(catalog["Category"],category)
    

# Funciones para creacion de datos

def newCategory(id,name):
    diccionario={ "id": id,"name":name}
    return diccionario

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1,video2):
    return int(video1["views"]) < int(video2["views"])


# Funciones de ordenamiento

def reduceList(catalog,size):
    reduced=lt.subList(catalog["videos"],0,size)
    return reduced

def selectionSort(lista):
    start_time = time.process_time()
    se.sort(lista, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def insertionSort(lista):
    start_time = time.process_time()
    si.sort(lista, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def shellSort(lista):
    start_time = time.process_time()
    sa.sort(lista, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg
def mergeSort(lista):
    start_time = time.process_time()
    ms.sort(lista, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def quicksort(lista):
    start_time = time.process_time()
    qs.sort(lista, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg
