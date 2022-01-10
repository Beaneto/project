def cria_posicao(linha: int, coluna: int) -> tuple:
    if type(linha) == int and type(coluna) == int and linha >= 0 and coluna >= 0:
        return linha, coluna
    else:
        raise ValueError("cria_posição: argumentos inválidos")
print(cria_posicao(1, 2))

def eh_posicao(argumento:tuple) -> bool:
    return type(argumento) == tuple and len(argumento) == 2 and all((type(i) == int for i in argumento))
print(eh_posicao(cria_posicao(1,2)))

def posicao_linha(pos:tuple) -> int:
    return pos[0]
print(posicao_linha(cria_posicao(1,2)))

def posicao_coluna(pos:tuple) -> int:
    return pos[1]
print(posicao_coluna(cria_posicao(1,2)))

def posicao_igual(pos1:tuple, pos2:tuple) -> bool:
    if eh_posicao(pos1) and eh_posicao(pos2):
        return pos1 == pos2
print(posicao_igual(cria_posicao(1,1),cria_posicao(1,1)))

def posicao_str(pos:tuple) -> str:
    pos = str(pos)
    return pos
print(posicao_str(cria_posicao(1,2)))

def cria_matriz(arg=0.0):
    if type(arg) == float or type(arg) == int or arg is None:
        dicionario = {}
        if arg == 0 or arg is None:
            dicionario["zero"] = 0.0
        else:
            dicionario["zero"] = float(arg)
        return dicionario
print(cria_matriz())

def eh_matriz(arg:dict)->bool:
    return type(arg) == dict and ("zero" in arg) and ({key == "zero" or ((eh_posicao(key) and (type(i) == int or type(i) == float for i in arg.values()))) for key in arg.keys()})
print(eh_matriz(cria_matriz()))

def matriz_zero(matriz:dict)->float:
    if eh_matriz(matriz):
        return matriz["zero"]
print(matriz_zero(cria_matriz(1)))

def matriz_copia(matriz:dict)->dict:
    return matriz.copy()
print (matriz_copia(cria_matriz(1)))

def matriz_posicao(matriz:dict, posicao:tuple, elemento:float)-> float:
    if eh_matriz(matriz) and eh_posicao(posicao):
        if posicao not in matriz:
            if elemento != matriz["zero"]:
                matriz[posicao] = float(elemento)
                return matriz["zero"]
            else:
                return matriz["zero"]
        else:
            antigo = matriz[posicao]
            matriz[posicao] = float(elemento)
            return antigo

def matriz_valor(matriz:dict, posicao:tuple)->float:
    if eh_matriz(matriz):
        if posicao not in matriz or posicao == "zero":
            return mat["zero"]
        else:
            return matriz[posicao]

def matriz_dimensao(matriz:dict)->tuple:
    coluna_max = 0
    linha_max = 0
    maxi = ()
    if len(matriz.keys()) == 1 and "zero" in matriz:
        return ()
    for key in matriz:
        if key != "zero":
            if posicao_coluna(key) > coluna_max:
                coluna_max = posicao_coluna(key)
            if posicao_linha(key) > linha_max:
                linha_max = posicao_linha(key)
        maxi = linha_max, coluna_max
    coluna_min = coluna_max
    linha_min = linha_max
    mini = ()
    for key in matriz:
        if key != "zero":
            if posicao_coluna(key) <= coluna_min:
                coluna_min = posicao_coluna(key)
            if posicao_linha(key) <= linha_min:
                linha_min = posicao_linha(key)
    mini = linha_min, coluna_min
    return mini, maxi

def matriz_densidade(matriz:dict)->float:
    matdim = matriz_dimensao(matriz)
    nelementos = (matdim[1][1]-matdim[0][1]+1) * (matdim[1][0]-matdim[0][0]+1)
    naonulos = 0
    for key in matriz:
        if key != "zero":
            naonulos += 1
    return naonulos/nelementos

def matriz_nulo(matriz:dict, novozero:float):
    matriz["zero"] = novozero
    for key in list(matriz.keys()):
        if key != "zero" and matriz[key] == novozero:
            del matriz[key]
    return

#mat = cria_matriz()
#print(matriz_posicao(mat, cria_posicao(1,2), 12.5))
#print(matriz_posicao(mat, cria_posicao(2,1), 5))
#print(matriz_nulo(mat, 12.5))
#print(matriz_densidade(mat))

def matriz_linha(matriz, nlinha:int)->tuple:
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    while counter <= posicao_coluna(matrizdim[1])-posicao_coluna(matrizdim[0]):
        lista = lista + [matriz_zero(matriz)]
        if matriz_valor(matriz, (nlinha, counter+(posicao_coluna(matrizdim[0])))) != matriz_zero(matriz):
            lista[counter] = matriz_valor(matriz, (nlinha, counter+posicao_coluna(matrizdim[0])))
        counter = counter + 1
    return tuple(lista)

def matriz_str(matriz, tipoformat:str)->str:
    matrizdim = matriz_dimensao(matriz)
    linhaini = posicao_linha(matrizdim[0])
    linhafin = posicao_linha(matrizdim[1])
    linhastr = matrizstr = ''
    for i in range(linhafin - linhaini + 1):
        linha = matriz_linha(matriz, linhaini + i)
        linhastr = ''
        for j in linha:
            linhastr = linhastr + str(tipoformat % j) + ' '
        matrizstr = matrizstr + '\n' + linhastr
    return matrizstr

mat = cria_matriz()
matriz_posicao(mat, cria_posicao(1,2), 12.5)
matriz_posicao(mat, cria_posicao(2, 1), 5)
#matriz_posicao(mat, cria_posicao(2,4), 3)
print(matriz_linha(mat, 1))
print (matriz_str(mat, "%.2f"))

def matriz_linha(matriz, nlinha:int)->tuple:
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    while counter <= posicao_coluna(matrizdim[1])-posicao_coluna(matrizdim[0]):
        lista = lista + [matriz_zero(matriz)]
        if matriz_valor(matriz, (nlinha, counter+(posicao_coluna(matrizdim[0])))) != matriz_zero(matriz):
            lista[counter] = matriz_valor(matriz, (nlinha, counter+posicao_coluna(matrizdim[0])))
        counter = counter + 1
    return tuple(lista)

def matriz_coluna(matriz, ncoluna:int)->tuple:
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    if matrizdim == ():
        return ()
    else:
        while counter <= posicao_linha(matrizdim[1])-posicao_linha(matrizdim[0]):
            lista = lista + [matriz_zero(matriz)]
            if matriz_valor(matriz, (counter+posicao_linha(matrizdim[0]), ncoluna)) != matriz_zero(matriz):
                lista[counter] = matriz_valor(matriz, (counter+posicao_linha(matrizdim[0]), ncoluna))
            counter = counter + 1
        return tuple(lista)

mat = cria_matriz()
#print(matriz_posicao(mat, cria_posicao(0, 1), 2))
#print(matriz_posicao(mat, cria_posicao(1, 2), 5))
#print(matriz_posicao(mat, cria_posicao(2, 3), 6.2))
#print(matriz_posicao(mat, cria_posicao(4, 4), 7))


def matriz_diagonal(matriz)->tuple:
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    nlinhas = posicao_linha(matrizdim[1])-posicao_linha(matrizdim[0])
    ncolunas = posicao_coluna(matrizdim[1])-posicao_coluna(matrizdim[0])
    if ncolunas != nlinhas:
        raise ValueError("matriz_diagonal: matriz não quadrada")
    else:
        while counter <= nlinhas:
            lista = lista + [matriz_zero(matriz)]
            linhaini = posicao_linha(matrizdim[0])
            colunaini = posicao_coluna(matrizdim[0])
            if matriz_valor(matriz, (counter + linhaini, counter + colunaini)) != matriz_zero(matriz):
                lista[counter] = matriz_valor(matriz, (counter + linhaini, counter + colunaini))
            counter = counter + 1
        return tuple(lista)

#print(matriz_diagonal(mat))











