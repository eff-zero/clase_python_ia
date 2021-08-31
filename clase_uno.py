#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:55:29 2021

@author: jesus
"""

print('Hello World')

# VARIABLES
a = 3
print(type(a))
a = 'Hola'
print(type(a))
a = 3.5
print(type(a))


# OPERACIONES
# Suma
a = 9
b = 2
c = 9 + 2
print(c)

# Resta
a = 9
b = 2
c = 9 - 2
print(c)

# Multiplicacion
a = 9
b = 2
c = 9 * 2
print(c)

# Division
a = 9
b = 2
c = a / b
print(c)

a = 9
b = 2
c = a // b
print(c)

# Potencia
a = 9
b = 2
c = a ** 2
print(c)

# Raiz
a = 27
c = a ** (1/3)
print(c)

# import math
# raiz = 16
# raizc = math.sqrt(raiz)


# TIPOS DE DATOS 
# String str
a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Jesus"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False


# CONVERSIONES ENTRE TIPOS DE DATOS
# Convertir de x a entero
a = '3'
y = int(a)
print(type(y))

# Convertir de x a string
a = '3'
y = str(a)
print(type(y))

# Concatenaciones
a = 'Hola'
b = 'Mundo'
c = a + ' ' + b
