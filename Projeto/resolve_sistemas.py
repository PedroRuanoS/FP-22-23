def produto_interno(tup1,tup2):
    res = 0
    for i in range(len(tup1)):
        res = res + (tup1[i]*tup2[i])
    return res

print(produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)))