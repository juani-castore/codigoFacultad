# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:58:34 2022

@author: juani
"""
import math

def calcularFactorial(n: int) -> int:
    ''' Requiere: n > 0
        Devuelve: el factorial de n
    '''
    return math.factorial(n)

print(calcularFactorial(5))