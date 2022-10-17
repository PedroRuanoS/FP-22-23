def produto_interno(tup1: tuple, tup2: tuple) -> float:
    res = 0
    for i in range(len(tup1)):
        res += (tup1[i]*tup2[i])
    return float(res)

#print(produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)))

def verifica_convergencia(mat: tuple, cons: tuple, x: tuple, num: tuple) -> bool:
    i = 0
    for t in mat:
        if abs(produto_interno(t, x) - cons[i]) > num:
            return False
        i += 1
    return True

#a1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.00001))
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.001))

def retira_zeros_diagonal(mat: tuple, cons) -> tuple:
    list_m = list(mat)
    list_c = list(cons)
    
    for i in range(len(mat)):
        if list_m[i][i] == 0:
            for j in range(len(mat)):
                if list_m[i][j] != 0 and list_m[j][i] != 0 and i != j:
                    k = list_m[i]
                    l = list_m[j]
                    o = list_c[i]
                    n = list_c[j]
                    list_m.pop(j)
                    list_m.insert(j, k)
                    list_m.pop(i)
                    list_m.insert(i, l)
                    list_c.pop(j)
                    list_c.insert(j, o)
                    list_c.pop(i)
                    list_c.insert(i, n)
                    break
        
    return (tuple(list_m), tuple(list_c)) 

#a2, c2 = ((0, 1, 1), (1, 0, 0), (0, 1, 0)), (1, 2, 3)
#a3 = ((1, 0, 0), (0, 1, 0), (0, 1, 1))
#matrix, cmatrix = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)), (1, 2, 3, 4)
#print(retira_zeros_diagonal(matrix, cmatrix))

def eh_diagonal_dominante(mat: tuple) -> bool:
    for i in range(len(mat)):
        linha = 0
        for j in range(len(mat[i])):
            if j == i:
                diag = abs(mat[i][j])
            else:
                linha += abs(mat[i][j])
        if diag < linha:
            return False

    return True

a4 = ((1, 2, 3, 4, 5),(4, -5, 6, -7, 8), (1, 3, 5, 3, 1),
(-1, 0, -1, 0, -1), (0, 2, 4, 6, 8))
print(eh_diagonal_dominante(a4))
print(eh_diagonal_dominante(((1, 0, 0), (0, 1, 0), (0, 1, 1))))

