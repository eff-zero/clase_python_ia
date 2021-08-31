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

a = 'hola'
b = a * 5

# CAPTURAR POR PANTALLA
nombre = input('Digite su nombre: ')
print('Hola', nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)

# EJERCICIOS
# 1. Haga un algoritmo que sume dos números e imprima su resultado
n1 = input('Numero #1 ')
n2 = input('Numero #2 ')
suma = float(n1) + float(n2)
print('La suma de', n1, '+', n2, 'es: ', suma)

n1 = float(input('Number 1 '))
n2 = float(input('Number 2 '))
print(f'La suma de {n1} + {n2} es {n1+n2}')

# 2. Haga un algoritmo que lea un numero y lo eleve al cuadrado
n = float(input('Ingrese su numero: '))
r = n ** 2
print(f'El cuadrado de {n} es {r}')

# 3. Haga un algoritmo que tome el valor de un producto
#    Le aplique el 20%, imprimar valor inicial
#    valor con descuento y valor final

vproducto = float(input('Ingrese el valor del producto $'))
descuento = vproducto * 0.20
vfinal = vproducto - descuento
print(f'El valor inicial del producto es ${vproducto:,}')
print(f'El valor del descuento es ${descuento:,}')
print(f'El valor final del producto es ${vfinal:,}')
