def calcula_quocientes(partidos: dict, num: int) -> dict:
    dic = {}
    for partido in partidos:
        div = []
        for i in range(num + 1):
            if i > 0:
                div += [partidos[partido]/i]
        dic[partido] = div
    return dic

#print(calcula_quocientes({'A':12000, 'B':7500, 'C':5250, 'D':3000}, 7))

def atribui_mandatos(partidos: dict, num: int) -> list:
    res = []
    dic = calcula_quocientes(partidos, num)
    for j in range(num):
        lis1 = []
        lis2 = []
        for partido in dic:
            lis1 += [dic[partido][0]]
            lis2 += [partido]
        max_i = lis1.index(max(lis1))

        maior = max(lis1)
        maiores = []
        for k in range(len(lis1)):
            if lis1[k] == maior:
                maiores += [lis2[k]]
    
        if len(maiores) > 1:
            menor = maiores[0]
            for partido in maiores:
                if partidos[partido] < partidos[menor]:
                    menor = partido 
            res += [menor]
            #se houverem dois elementos iguais na lis1 !!!!!!!!!!!!!!!!!!
        else:
            res += [lis2[max_i]]
            dic[lis2[max_i]].pop(0)
        
    return res

print(atribui_mandatos({'A':12000, 'B':7500, 'C':5250, 'D':3000}, 7))

