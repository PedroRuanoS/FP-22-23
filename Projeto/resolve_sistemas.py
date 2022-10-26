def produto_interno(tup1: tuple, tup2: tuple) -> float:
    res = 0
    for i in range(len(tup1)):
        res += (tup1[i]*tup2[i])
    return float(res)

#print(produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)))

def verifica_convergencia(matriz: tuple, constante: tuple, x: tuple, precisao: tuple) -> bool:
    i = 0
    for t in matriz:
        if abs(produto_interno(t, x) - constante[i]) > precisao:
            return False
        i += 1
    return True

#a1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.00001))
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.001))

def retira_zeros_diagonal(matriz: tuple, constante: tuple) -> tuple:
    list_m = list(matriz)
    list_c = list(constante)
    
    for i in range(len(matriz)):
        if list_m[i][i] == 0:
            for j in range(len(matriz)):
                if list_m[i][j] != 0 and list_m[j][i] != 0 and i != j:
                    list_m[i], list_m[j] = list_m[j], list_m[i]
                    list_c[i], list_c[j] = list_c[j], list_c[i]
                    break
        
    return (tuple(list_m), tuple(list_c)) 

#a2, c2 = ((0, 1, 1), (1, 0, 0), (0, 1, 0)), (1, 2, 3)
#a3 = ((1, 0, 0), (0, 1, 0), (0, 1, 1))
#matrix, cmatrix = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)), (1, 2, 3, 4)
#print(retira_zeros_diagonal(matrix, cmatrix))

def eh_diagonal_dominante(matriz: tuple) -> bool:
    for i in range(len(matriz)):
        linha = 0
        for j in range(len(matriz[i])):
            if j == i:
                diag = abs(matriz[i][j])
            else:
                linha += abs(matriz[i][j])
        if diag < linha:
            return False

    return True

#a4 = ((1, 2, 3, 4, 5),(4, -5, 6, -7, 8), (1, 3, 5, 3, 1),
#(-1, 0, -1, 0, -1), (0, 2, 4, 6, 8))
#print(eh_diagonal_dominante(a4))
#print(eh_diagonal_dominante(((1, 0, 0), (0, 1, 0), (0, 1, 1))))

def resolve_sistema(mat: tuple, cons: tuple, precisao: float) -> tuple:
    if not isinstance(mat, tuple) or not isinstance(cons, tuple) or not isinstance(precisao, (int, float)):
        raise ValueError('resolve_sistema: argumentos invalidos')
    if len(mat) == 0:
        raise ValueError('resolve_sistema: argumentos invalidos')
    for num in cons:
        if not isinstance(num, (int, float)):
            raise ValueError('resolve_sistema: argumentos invalidos')
    for linha in mat:
        if not isinstance(linha, tuple):
            raise ValueError('resolve_sistema: argumentos invalidos')
        if len(linha) != len(mat) or len(linha) != len(cons):
            raise ValueError('resolve_sistema: argumentos invalidos')
        for num in linha:
            if not isinstance(num, (int, float)):
                raise ValueError('resolve_sistema: argumentos invalidos')
       
    matriz, constante = retira_zeros_diagonal(mat, cons)
    if not eh_diagonal_dominante(matriz):
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    x = [0,0,0]
    while not verifica_convergencia(matriz, constante, x, precisao):
        for i in range(len(x)):
            x[i] = x[i] + (constante[i] - produto_interno(matriz[i], x))/matriz[i][i]  
    
    return tuple(x)

#a4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
#print(resolve_sistema(a4, c4, 1e-20))
#a4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
#a5, c5 = ((4, -1, 1), (2, -8, 1), (1, 0, -3)), (2, 4, 1)
#print(resolve_sistema(a5, c5, 1e-20))


