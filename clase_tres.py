#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:27:29 2021

@author: jesus
"""

# Tipos de Colecciones - Clase #3

# LISTAS O VECTORES
# Tipos de dato mutable y ordenado
a = []
a = [1, 2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2, 5, 7], 2.6]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
print(b[2])
print(c[2][1])
print(c[3][1][1])

a.append(99)  # Agregar el elemento al final de la lista
a.remove(3)  # Elimina el elemento que coincida con el valor | primero
a.pop()  # Elimina el último elemento del vector
a.pop(2)  # Elimina un entero por posicion
a.clear()  # Elimina todos lo elementos del vector

4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos de un vector
a = b  # Asignación de b en el mismo espacio de memoria de a
id(a)  # Dirección de memoria de un objeto
a = b.copy()  # Copia los elementos de b en a
a = b[:]  # Forma de copiar utilizada por la comunidad
b = a[0:3]
b = a[2:7]
b = a[:6]
b = a[1:]

b = c[3][1][:2]


# TUPLA
# Tipo de dato INMUTABLE (Su valor no cambia en el tiempo) y ordenado
a = ()
a = (1, 2, 3, 4)
print(a[1])
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2, 5, 7], 2.6])
4 in a


# SET (No es diccionario)
# Tipo de dato mutable pero NO ordenado
a = {1, 2, 3, 4}
a = set()
b = {2, True, 'Hola', 3.4}
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2, 5, 7], 2.6])  # No permite vector en su interior 
4 in a

# DICCIONARIO
# Mutable y NO ordenado
a = {}
a = {'nombre': 'Jesús', 'apellido': 'Hernández'}
a = {1: 'Jesús', 2: 'Hernández'}
a['nombre']

for valor in a:
    print(valor)

for valor in a.values():
    print(valor)

for valor in a.items():
    print(valor)  # Retorna tuplas

for llave, valor in a.items():
    print(f'Llave: {llave}, Valor: {valor}')


# Funciones
def nombre_funcion():
    pass


def saludar():
    print('Hola mundo')


def saludar(nombre):
    print(f'Hola {nombre}')


# Python no prermite la SOBRECARGA de métodos
# Parámetros opcionales
def saludar(nombre='Mundo'):
    print(f'Hola {nombre}')


def saludar(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')

# No puedo tener un parámetro obligatorio después de un
# parámetro opcional
def saludar(nombre="", apellido):  # NO SIRVE
    print(f'Hola {nombre} {apellido}')


# Parámetros ilimitados
def saludar(*nombres):
    print(f'Hola {nombres}')


def saludar(*nombres):
    for nombre in nombres:
        print(f'Hola {nombres}')


def saludar(*nombres, apellido=""):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido: {apellido}')


def saludar(*nombres, apellido):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido: {apellido}')


def saludar(**nombres):  # Esto espera como parametro un {key:value}
    print(nombres)


def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div


resultado = operaciones(4, 5)

suma, res, mul, div = operaciones(4, 5)

suma, _, _, div = operaciones(4, 5)  # Solo suma y división | Descomprimir

# while(condición):
