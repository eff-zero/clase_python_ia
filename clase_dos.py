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
