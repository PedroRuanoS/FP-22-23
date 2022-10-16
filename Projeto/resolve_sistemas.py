def produto_interno(tup1,tup2):
    res = 0
    for i in range(len(tup1)):
        res += (tup1[i]*tup2[i])
    return res

#print(produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)))

def verifica_convergencia(m, c, x, num):
    i = 0
    for t in m:
        if abs(produto_interno(t, x) - c[i]) > num:
            return False
        i += 1
    return True

#a1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.00001))
#print(verifica_convergencia(a1, c1, (0.1001, 1), 0.001))
