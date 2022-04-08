from typing import List #importante import para que listas ande bien

def nave_estelar_cercana(sensado: List[int], p: int) -> bool:
    
    '''
    requiere: p(punto critico) >= 0 and list elements >= 0
    devuelve: true si hay una distancia en sensado <= a p, false en caso contrario
    '''
    i:int = 0
    res: bool = False
    while (i < len(sensado)):
        if sensado[i] <= p:
            res = True
        i += 1
    return res

listaDeDistancias: List[int] = [1323,4321,2135,5436,23414,6336643,125]
ptoCritico: int = 125
print(nave_estelar_cercana(listaDeDistancias,ptoCritico))


