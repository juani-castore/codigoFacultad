# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:46:05 2022

@author: juani

guia 2, ejercicio 3

"""

import math

print("ej a")

def intSqr(n: int) -> int:
    ''' Requiere: n > 0
        Devuelve: el resultado entero de calcular la raiz cuadrada de n
    '''
    print(n)
    print(n**0.5)
    return int(n**0.5)

print(intSqr(2))
print(intSqr(5))
print(intSqr(7))
print(intSqr(123))
print(intSqr(11))


print("ej b")

def calcularFactorial(n: int) -> int:
    ''' Requiere: n > 0
        Devuelve: el factorial de n
    '''
    return math.factorial(n)

print(calcularFactorial(5))

print("ej c")

def calcularCombinatorio(n: int, k: int) -> int:
    ''' Requiere: n y k >= 0, con k <= n 
        Devuelve: el combinatorio (n k)
    '''
    combinatorio: int = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return combinatorio

print(calcularCombinatorio(4, 2))


#print("ej d")
#    ''' Requiere: n >= 0 
#        Devuelve: un string con los valores de (n i) para todo 0 ≤ i ≤ n, separados por comas
 #   '''
  #  string: str = []
   # a : int = 4
    #for i: int in range(a)
     #   combinatorio : int = calcularCombinatorio(a, i)
   # -----------------------------------------------------------------------
    
    
def stringDeAsteriscos :
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

