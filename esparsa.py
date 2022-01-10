#__author__"ist1103149 Beatriz Neto"
#__version__ = "0.1"
#__all__ = [’cria_posicao’, ’eh_posicao’, ’posicao_linha’,’posicao_coluna’, ’posicao_igual’, ’posicao_str’, \
#’cria_matriz’, ’eh_matriz’, ’matriz_zero’, ’matriz_copia’, ’matriz_posicao’, ’matriz_valor’, ’matriz_dimensao’, \
#’matriz_densidade’, ’matriz_nulo’, ’matriz_str’, ’matriz_linha’, ’matriz_coluna’, ’matriz_diagonal’ ]

'''O objetivo do projeto é desenvolver um conjunto de rotinas para a manipulação de matrizes esparsas, em Python3.'''
'''Um elemento da matriz é um valor identificado por uma coordenada.
Uma matriz esparsa representa apenas os elementos não nulos.
Representei as posições enquanto tuplos e as matrizes enquanto dicionários, cujas keys são tuplos e os values floats.'''


def cria_posicao(linha: int, coluna: int) -> tuple:
    '''Se os argumentos forem dois inteiros, devolve a posição(tuplo) formada por esse par (linha,coluna).'''
    if type(linha) == int and type(coluna) == int and linha >= 0 and coluna >= 0:
        return linha, coluna
    else:
        raise ValueError("cria_posição: argumentos inválidos")
pos = cria_posicao(1,1)

def eh_posicao(argumento:tuple) -> bool:
    '''Verifica se a representação da posição é compatível, sem gerar erros.'''
    return type(argumento) == tuple and len(argumento) == 2 and all((type(i) == int and i >= 0 for i in argumento))
print(eh_posicao((1,1)))

def posicao_linha(pos:tuple) -> int:
    '''Devolve a linha(inteiro) do argumento posição.'''
    return pos[0]
print(posicao_linha(pos))

def posicao_coluna(pos:tuple) -> int:
    '''Devolve a coluna(inteiro) do argumento posição.'''
    return pos[1]
print(posicao_coluna(pos))

def posicao_igual(pos1:tuple, pos2:tuple) -> bool:
    '''Devolve True se as duas posições referem a mesma coordenada.'''
    if eh_posicao(pos1) and eh_posicao(pos2):
        return pos1 == pos2

def posicao_str(pos:tuple) -> str:
    '''Devolve uma representação textual(string) da posição.'''
    pos = str(pos)
    return pos
print(posicao_str(cria_posicao(1, 2)))

def cria_matriz(arg=0.0)->dict:
    '''Recebe um valor real(int/float), que é o zero da matriz. Devolve uma matriz vazia.'''
    if type(arg) == float or type(arg) == int or arg is None:
        dicionario = {}
        if arg == 0:
            dicionario["zero"] = 0.0
        else:
            dicionario["zero"] = float(arg)
        return dicionario
    else:
        raise ValueError("cria_matriz: argumento inválido")
print(cria_matriz())

'''def _eh_imutavel(argumento)->bool:
    if eh_posicao(argumento):
        return tuple(eh_posicao(argumento))'''

def eh_matriz(arg:dict)->bool:
    '''Recebe um argumento de qualquer tipo. Devolve True se o argumento corresponde a uma matriz.'''
    return type(arg) == dict and ("zero" in arg) and \
    ({key == "zero" or ((eh_posicao(key) and (type(i) == int or type(i) == float for i in arg.values()))) for key in arg.keys()})

def matriz_zero(matriz:dict)->float:
    '''Recebe uma matriz e devolve o seu zero.'''
    return matriz["zero"]

def matriz_copia(matriz:dict)->dict:
    '''Recebe uma matriz e devolve uma cópia da mesma.'''
    dic_copia = {}
    for key, value in matriz.items():
        dic_copia = dic_copia | {key: value}
    return dic_copia

def matriz_posicao(matriz:dict, posicao:tuple, elemento)-> float:
    '''Recebe uma matriz, uma posição e um valor(float/int). Introduz o valor(float) na matriz na posição indicada. \
    Devolve o valor que se encontrava nessa posição anteriormente.'''
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

def matriz_valor(matriz:dict, posicao)->float:
    '''Recebe uma matriz e uma posição. Devolve o valor associado à posição nessa matriz.'''
    if posicao not in matriz or posicao == "zero":
        return matriz_zero(matriz)
    else:
        return matriz[posicao]

def matriz_dimensao(matriz:dict)->tuple:
    '''Recebe uma matriz. Devolve um tuplo que contém a coordenada mínima e a coordenada máxima \
    (ou um tuplo vazio se a matriz não contém elementos).'''
    coluna_max = 0
    linha_max = 0
    maxi = ()
    if len(matriz.keys()) == 1 and "zero" in matriz:
        return ()
    for key in matriz:
        if key != "zero":
            if posicao_coluna(key) > coluna_max: coluna_max = posicao_coluna(key)
            if posicao_linha(key) > linha_max: linha_max = posicao_linha(key)
    coluna_min = coluna_max
    linha_min = linha_max
    for key in matriz:
        if key != "zero":
            if posicao_coluna(key) <= coluna_min: coluna_min = posicao_coluna(key)
            if posicao_linha(key) <= linha_min: linha_min = posicao_linha(key)
    return (linha_min, coluna_min), (linha_max, coluna_max)

def matriz_densidade(matriz:dict)->float:
    '''Recebe uma matriz. \
    Devolve a densidade da matriz (quociente entre o nº de elementos não nulos e dimensão total da matriz).'''
    matdim = matriz_dimensao(matriz)
    nelementos = (matdim[1][1]-matdim[0][1]+1) * (matdim[1][0]-matdim[0][0]+1)
    naonulos = 0
    for key in matriz:
        if key != "zero": naonulos += 1
    return naonulos/nelementos

def matriz_nulo(matriz:dict, novozero:float):
    '''Recebe uma matriz e um float. Define um novo zero(float) para a matriz. Devolve None.'''
    matriz["zero"] = novozero
    for key in list(matriz.keys()):
        if key != "zero" and matriz[key] == novozero:
            del matriz[key]
    return None

def matriz_linha(matriz, nlinha:int)->tuple:
    '''Recebe uma matriz e um inteiro. Devolve um tuplo que contém os elementos da linha passada como \
    argumento(inteiro), mas apenas entre a dimensão mínima e a dimensão máxima!'''
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    if matrizdim == ():
        return ()
    while counter <= posicao_coluna(matrizdim[1])-posicao_coluna(matrizdim[0]):
        lista = lista + [matriz_zero(matriz)]
        if matriz_valor(matriz, (nlinha, counter+(posicao_coluna(matrizdim[0])))) != matriz_zero(matriz):
            lista[counter] = matriz_valor(matriz, (nlinha, counter+posicao_coluna(matrizdim[0])))
        counter = counter + 1
    return tuple(lista)

def matriz_str(matriz, tipoformat:str)->str:
    '''Recebe uma matriz e o formato de representação dos valores (em string). \
    Devolve uma representação textual(string) da matriz sob a forma não esparsa.'''
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

def matriz_coluna(matriz, ncoluna:int)->tuple:
    '''Recebe uma matriz e um inteiro. Devolve um tuplo que contém os elementos da coluna passada como \
    argumento(inteiro), mas apenas entre a dimensão mínima e a dimensão máxima!'''
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

def matriz_diagonal(matriz)->tuple:
    '''Recebe uma matriz. Devolve um tuplo que contém os elementos da sua diagonal completa, \
     mas apenas entre a dimensão mínima e a dimensão máxima! \
     Gera uma exceção ValueError caso as dimensões da matriz não tenham igual amplitude.'''
    matrizdim = matriz_dimensao(matriz)
    lista = []
    counter = 0
    nlinhas = posicao_linha(matrizdim[1])-posicao_linha(matrizdim[0])
    ncolunas = posicao_coluna(matrizdim[1])-posicao_coluna(matrizdim[0])
    if matrizdim == ():
        return ()
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

