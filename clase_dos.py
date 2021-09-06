#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:09:06 2021

@author: jesus
"""

# COndicionales

# Tabla de Verdad

# AND
# v and v = v
# v and f = f
# f and v = f
# f avd f = f
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# OR
# v or v = v
# v or f = f
# f or v = f
# f or f = f
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# NEGACION
print(not True)  # False
print(not False)  # True

# Varias condiciones
print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True

# Jerarquía de operaciones
# 1. Paréntesis y Llaves
# 2. Potencias y Raíces
# 3. Mutiplicación y División
# 4. Sumas y Restas

# Jerarquía de operaciones booleanas
# 1. Paréntesis y Llaves
# 2. Tabla de verdad

# Estructura
x = 1
if (x > 0):
    print('1')
else:
    print('2')
print('3')

# HUA que dada la edad de una persona indique si es mayor o menor de edad.
edad = int(input('Ingrese su edad: '))
if (edad > 0):
    if (edad >= 18):
        print('Usted es mayor de edad')
    else:
        print('Usted es menor de edad')
else:
    print('Numero invalido')

# HUA que donde se aprueba una asignatura con 3.0 y la máxima es 5.0.
nota = float(input('Ingrese su nota: '))
if (nota >= 0 and nota <= 5):
    if (nota >= 3):
        print('Usted ha aprobado')
    else:
        print('Usted ha reprobado')
else:
    print('Nota inválida')

# HUA que dado un número n diga si es negativo, positivo o cero.
n = float(input('Ingrese su número: '))
if (n > 0):
    print('Su número es positivo')
elif (n < 0):
    print('Su número es negativo')
else:
    print(f'Su número es {n}')
