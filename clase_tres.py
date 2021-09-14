#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:27:29 2021

@author: jesus
"""

# Tipos de Colecciones - Clase #3

# Listas o vectores
# Tipos de dato mutable y ordenado

a = [5, 6, 1, 2, 5, 9, 8, 3, 0]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]]

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
