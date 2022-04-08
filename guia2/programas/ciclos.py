def hola(texto):
    i = 0
    while(texto[i] == "*") and i < len(texto):
        i = i + 1
    return i

print(hola("**76239yigufhdiwuhgiwuorhg**"))
