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
        print(lis1)
        print(lis2)
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
            dic[menor].pop(0)
        else:
            max_i = lis1.index(max(lis1))
            res += [lis2[max_i]]
            dic[lis2[max_i]].pop(0)
        
    return res

#print(atribui_mandatos({'A':12000, 'B':7500, 'C':5250, 'D':3000}, 7))

def obtem_partidos(territorios: dict) -> list:
    partidos = []
    for territorio in territorios:
        for partido in territorios[territorio]['votos']:
            if partido not in partidos:
                partidos.append(partido)
    
    return sorted(partidos)

#info = {
#'Endor': {'deputados': 7,
#'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},
#'Hoth': {'deputados': 6,
#'votos': {'B':11500, 'A':9000, 'E':5000, 'D':1500}},
#'Tatooine': {'deputados': 3,
#'votos': {'A':3000, 'B':1900}}}

#print(obtem_partidos(info))

#for cu in info['Endor']['votos']:
#    print(cu)

def ordenar(res):
    menor = 0
    for i in range(len(res)):
        if res[i][1] > res[menor][1]:
            res[i], res[menor] = res[menor], res[i]
        elif res[i][1] < res[menor][1]:
            menor = i
        elif res[i][1] == res[menor][1]:
            if res[i][2] > res[menor][2]:
                res[i], res[menor] = res[menor], res[i]
            if res[i][2] < res[menor][2]:
                menor = i 
    
    return res

def obtem_resultado_eleicoes(territorios):

    

    partidos = obtem_partidos(territorios)
    soma = {}
    for i in partidos:
        soma[i] = 0

    mandatos = []
    for territorio in territorios:
        for partido in territorios[territorio]['votos']:
            soma[partido] = soma[partido] + territorios[territorio]['votos'][partido]
        mandato = atribui_mandatos(territorios[territorio]['votos'], territorios[territorio]['deputados'])
        mandatos += mandato

    res = []
    for partido_total in soma:
        counter = 0
        for j in mandatos:
            if j == partido_total:
                counter += 1
        res.append((partido_total, counter, soma[partido_total]))

    res = ordenar(res)
    return res

