from typing import List

def filtrar_solo_CAFE(s: str) -> str:
    '''
    requiere: nada
    devuelve: las letras {C,A,F,E} en el mismo orden que aparecen en el argumento

    '''
    i: int = 0
    cafe: str = ""
    #A
    while(i < len(s)):
        #B
        if(s[i] in "CAFE"):
            cafe = cafe + s[i]
        i = i + 1
        #C
    #D
    return cafe



def es_cafetero(n: int) -> bool:
    """
    requiere: n > 0
    devuelve: un booleano que dice si el numero ingresado es cafetero o no
    """
    nroHex: str = hex(n).upper()
    i: int = 0
    res: bool = False
    if("B" in nroHex or "D" in nroHex):
        res = False
    elif (filtrar_solo_CAFE(nroHex) == "CAFE"):
        res = True
    return res
    
def generar_mensaje(res: bool, n: int):
    """
    requiere: el resultado de esCafetero junto al numero analizado
    devuelve: imprime en pantalla el resultado de es_cafetero enunciando si es cafetero o no
    """
    if(res == True):
        return "El " + str(n) + " es cafetero." 
    else:
        return "El " + str(n) + " no es cafetero."






def n_esimo_cafetero(n: int) -> int:
    '''
    requiere: n > 0
    devuelve: el n-esimo numero cafetero que existe empezando por 51966 como el 1-esimo

    '''
    i: int = 0
    # contador de la cantidad de cafeteros
    j: int = 51965
    # numero a analizar para ver si es cafetero o no
    cafe: int = 0
    while(i < n):
        if(es_cafetero(j)):
            i = i + 1
            if(i == n):
                cafe = j
        j = j +1
    return cafe

def cafeteros_entre(n: int, m: int) -> List[int]:
    '''
    requiere: n y m >= 0; n <= m
    devuelve: una lista de los numeros cafeteros comprendidos entre n y m de manera ordenada de mayor a menor
    modifica: agrega los numeros cafeteros encontrados entre n y m a listaCafeteros
    '''
    listaCafeteros: List[int] = []
    i: int = n
    while (i < m):
        if(es_cafetero(i) == True):
           listaCafeteros.append(i)
        i = i + 1
    return listaCafeteros


# Definir también las funciones auxiliares que se consideren necesarias.

