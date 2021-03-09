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
def cmpVideosById(video1,video2):
    return video1["video_id"]<video2["video_id"]
# Funciones de ordenamiento

def reduceList(catalog,size):
    reduced=lt.subList(catalog["videos"],0,size)
    return reduced

def selectionSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        se.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        se.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        se.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def insertionSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        si.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        si.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        si.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def shellSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        sa.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        sa.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        sa.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

def mergeSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        ms.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        ms.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        ms.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg


def quickSort(lista,numero):
    numero=int(numero)
    start_time = time.process_time()
    if numero==1:
        qs.sort(lista, cmpVideosByvViewsAscendant)
        stop_time = time.process_time()
    elif numero==2:
        qs.sort(lista,cmpVideosByViewsDescendant)
        stop_time = time.process_time()
    else:
        qs.sort(lista,cmpVideosById)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista,elapsed_time_mseg

# Funciones para reducir datos


def listaPorCategoriaPaises(pais,categoria,tamano,tipo,catalog):
    start_time = time.process_time()
    lista=catalog["videos"]
    size=lt.size(lista)

    numero=getCategoryNumber(categoria,catalog)
    tamano=int(tamano)
    contador=1

    for i in range(1,size+1):
        video=lt.getElement(lista,i)
        if cmpVideosByCategory(numero,video) and cmpVideosByCountry(pais,video):
            lt.exchange(lista,i,contador)
            contador+=1

    if tamano!=1:
        lista_total=lt.subList(lista,1,contador-1)
    else:
        lista_total=lt.subList(lista,1,contador)
    
    ordenada=seleccionarOrdenamiento(tipo,lista_total,1)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return ordenada[0], elapsed_time_mseg

#funciones de seleccion de ordenamientos

def encontrarVideoTendenciaPais(pais,catalog):
    start_time = time.process_time()
    videos=catalog["videos"]
    size=lt.size(videos)
    contador=1
    for i in range(1,size+1):               #seleccionamos los videos que son de un pais y los colocamos al inicio de la lista
        video=lt.getElement(videos,i)
        if cmpVideosByCountry(pais,video):
            lt.exchange(videos,i,contador)
            contador+=1
    
    lista_paises=lt.subList(videos,1,contador) #reducimos la lista total de videos a los videos que son del pais deseado
    lista_ordenada=mergeSort(lista_paises,3)[0] #ordenamos los paises segun su id

    mayor=lt.getElement(lista_ordenada,1)
    cantidad_mayor=0
    size=lt.size(lista_ordenada)
    print(size)
    
    for i in range(1,size+1):                    #se compara cual es el video que mas dias ha durado en tendencia
        comparador=lt.getElement(lista_ordenada,i)
        bandera=True
        numeral=i
        cantidad=0
        while bandera and numeral<=size:
            comparado=lt.getElement(lista_ordenada,numeral)
            if comparador["video_id"]==comparado["video_id"]:
                cantidad+=1
            else:
                bandera=False
            if cantidad>cantidad_mayor:
                cantidad_mayor=cantidad
                mayor=lt.getElement(lista_ordenada,numeral)
            numeral+=1

def encontrarVideoTendenciaCategoria(nombre,catalog):
    start_time = time.process_time()
    videos = catalog["videos"]
    size=lt.size(videos)
    contador=1
    numero = getCategoryNumber(nombre,catalog)
    for i in range(1,size+1):               #seleccionamos los videos que son de una categoria y los colocamos al inicio de la lista
        video=lt.getElement(videos,i)
        if cmpVideosByCategory(numero,video):
            lt.exchange(videos,i,contador)
            contador+=1
    
    lista_categoria=lt.subList(videos,1,contador) #reducimos la lista total de videos a los videos que son de la categoria deseada
    lista_ordenada=mergeSort(lista_categoria,3)[0] #ordenamos las categorias segun su id

    mayor=lt.getElement(lista_ordenada,1)
    cantidad_mayor=0
    size=lt.size(lista_ordenada)
    print(size)
    
    for i in range(1,size+1):                    #se compara cual es el video que mas dias ha durado en tendencia
        comparador=lt.getElement(lista_ordenada,i)
        bandera=True
        numeral=i
        cantidad=0
        while bandera and numeral<=size:
            comparado=lt.getElement(lista_ordenada,numeral)
            if comparador["video_id"]==comparado["video_id"]:
                cantidad+=1
            else:
                bandera=False
            if cantidad>cantidad_mayor:
                cantidad_mayor=cantidad
                mayor=lt.getElement(lista_ordenada,numeral)
            numeral+=1
        
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return mayor,cantidad_mayor,elapsed_time_mseg
          
            
            
        
        


    
def seleccionarOrdenamiento(tipo,lista,ascendente):
    tipo=int(tipo)
    ascendente=int(ascendente)
    if tipo==1:
        ordenada=selectionSort(lista,ascendente)
    if tipo==2:
        ordenada=insertionSort(lista,ascendente)
    if tipo==3:
        ordenada=shellSort(lista,ascendente)
    if tipo==4:
        ordenada=quickSort(lista,ascendente)
    if tipo==5:
        ordenada=mergeSort(lista,ascendente)
    return ordenada

    