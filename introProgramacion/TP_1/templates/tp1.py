from re import A
from cafetero import filtrar_solo_CAFE, es_cafetero, n_esimo_cafetero, generar_mensaje, cafeteros_entre

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario.
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios 
    adelante y atrás según la siguiente codificación:
        A -> Filtrar solo CAFE;
        B -> Determinar si un número es cafetero;
        C -> Devolver n-ésimo número cafetero;
        D -> Devolver cafeteros entre dos números;
        X -> Finalizar;
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Filtrar solo CAFE [s]')
    print('B. Es cafetero [n]')
    print('C. N-ésimo cafetero [n]')
    print('D. Cafeteros entre [n,m]')
    print('X. Finalizar')
    
    # input permite al usuario ingresar su opción, strip le saca caracteres 
    # de fin de línea, upper la pasa a mayúsculas.
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()
    
    # Se analiza la opción elegida
    
    if opcion_seleccionada == 'A':
        s:str = input('Ingrese s: ')
        print("String filtrado: " + filtrar_solo_CAFE(s) + ".")
    
    elif opcion_seleccionada == 'B':
        n:int = int(input('Ingrese n: '))
        res: bool = es_cafetero(n)
        print(generar_mensaje(res,n))
    
    elif opcion_seleccionada == 'C':
        n:int = int(input('Ingrese n: '))
        print("El " + str(n) +"-esimo cafetero es: " + str(n_esimo_cafetero(n)) + ".")
    
    elif opcion_seleccionada == 'D':
        n:int = int(input('Ingrese n: '))
        m:int = int(input('Ingrese m: '))
        print(cafeteros_entre(n,m))
    
    elif opcion_seleccionada == 'X':
        finalizar = True
    
    else:
        print('Opción inválida.')

    
    if opcion_seleccionada != 'X':
        input('Presione ENTER para continuar.')
