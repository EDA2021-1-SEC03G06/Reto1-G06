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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(tipo):
    catalog=model.newCatalog(tipo)
    return catalog

    

# Funciones para la carga de datos
def loadData(catalog):
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    
    file_name=cf.data_dir + "videos-small.csv"
    input_file=csv.DictReader(open(file_name,encoding="utf-8"))
    for video in input_file:
        model.addVideo(catalog,video)

    

def loadCategories(catalog):
    file_name=cf.data_dir + "category-id.csv"
    input_file=csv.DictReader(open(file_name,encoding="utf-8"),delimiter="\t")
    for categoria in input_file:
        model.addCategory(catalog, categoria)

# Funciones de ordenamiento


def selectionSort(lista,ascendente):
    return model.selectionSort(lista,ascendente)
def insertionSort(lista,ascendente):
    return model.insertionSort(lista,ascendente)
def shellSort(lista,ascendente):
    return model.shellSort(lista,ascendente)
def mergeSort(lista,ascendente):
    return model.shellSort(lista,ascendente)
def quickSort(lista,ascendente):
    return model.shellSort(lista,ascendente)

# Funciones de consulta sobre el catálogo
# Funciones para reducir datos
def reduceList(catalog,size):
    return model.reduceList(catalog,size)
def PaisesCategoria(pais,categoria,tamano,tipo,catalog):
    return model.listaPorCategoriaPaises(pais,categoria,tamano,tipo,catalog)

#funcion para seleccionar ordenamientos

def seleccionarOrdenamiento(tipo,lista,ascendente):
    return model.seleccionarOrdenamiento(tipo,lista,ascendente)