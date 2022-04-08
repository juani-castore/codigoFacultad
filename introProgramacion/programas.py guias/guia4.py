ORIGINYEAR : int = 1980

def IsLeapYear ( y : int ) -> bool :
    ''' Requiere : y >0
    Devuelve : True si el año y es bisiesto ; False si no. '''
    return ( y %4==0) and ( y %100 >0 or y %400==0)

def CalculateCurrentYear ( days :int) -> int :
    ''' Requiere : days >= 0 , la cantidad de días transcurridos
    desde el 1 de enero de ORIGINYEAR .
    Devuelve : El año actual (ej: 2007) . '''
    year : int = ORIGINYEAR
    while days > 365:
        if IsLeapYear ( year ) :
            if days > 366:
                days = days - 366
                year = year + 1
        else :
            days = days - 365
            year = year + 1
    return year

print(CalculateCurrentYear())