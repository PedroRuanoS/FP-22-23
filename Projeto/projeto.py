#1

from email.errors import MultipartConversionError


def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} e devolve
    a cadeia de carateres "limpa", ou seja, são retirados 
    os caracteres \t,\n,\v,\f,\r, dois ou mais espaços seguidos
    e espaços no inicio ou no fim da cadeia (utilizando os métodos join e split).""" 

    return ' '.join(s.split())                 #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  


def corta_texto(st: str, i: int) -> tuple:
    """Esta função recebe uma cadeia de carateres {st} e um inteiro positivo {i} correspondentes
    a um texto limpo e uma largura de coluna respetivamente, e devolve duas subcadeias
    de carateres limpas {res e resto} em que {res} é a subcadeia com a quantidade de caracteres igual
    à largura fornecida e {resto} é a subdeia que contém o resto do texto de entrada"""                 
   
    n = st.split()                      #split: transfoma uma cadeia de caracteres {st} uma lista {n}
    res = [] 
    resto = st.split()                   
    
    for p in n:
        if len(p)<=i:
            res.append(p)              #append: adiciona um item à lista {res1}               
            i -= len(p) + 1                
            resto.remove(p)              #remove: remove um item da lista {res2}
        else: 
            break

    return (' '.join(res), ' '.join(resto))   #...


def insere_espacos(car: str, num: int) -> str:
    n = car.split()
    i = len(n) - 1
    t = num 
    k = 1   

    for c in n:
        t -= len(c)         #{t}: caracteres vazios necessários de adicionar para {n} ficar com a quantidade de caracteres desejada {num}                  
    if len(n) == 1:
        for d in range(t):
            n.append(' ')
    else:  
        while t > 0:
            k += 1
            j = -1
            for e in range(i):
                j += k
                n.insert(j, ' ')
                t -= 1
                if t == 0:
                    break
            
    return ''.join(n)


def justifica_texto(texto: str, numero: int) -> tuple:
    if not isinstance(numero, int) or not isinstance(texto, str) or len(texto) == 0:
        raise ValueError('justifica_texto: argumentos invalidos')
    erro = texto.split()
    for palavra in erro:
        if len(palavra)>numero:
            raise ValueError('justifica_texto: argumentos invalidos')

    text = limpa_texto(texto)
    resto = text
    res = []
    rest = resto.split()

    while len(resto) > numero:
        n = corta_texto(resto, numero)[0]
        o = n.split()
        m = insere_espacos(n, numero)
        res.append(m)
        for i in o:
            rest.remove(i)
        resto = ' '.join(rest)

    t = numero - len(resto)
    if t%2 == 0:
        for j in range(int(t/2)):
            rest.append(' ')
            resto = ' '.join(rest)
    else: 
        for j in range(int((t+1)/2)):
            rest.append(' ')
            resto = (' '.join(rest))[:-1]
            
    res.append(resto)
    return tuple(res)  


#2

def calcula_quocientes(partidos: dict, num: int) -> dict:
    dic = {}
    for partido in partidos:
        div = []
        for i in range(num + 1):
            if i > 0:
                div += [partidos[partido]/i]
        dic[partido] = div
    return dic

def atribui_mandatos(partidos: dict, num: int) -> list:
    res = []
    dic = calcula_quocientes(partidos, num)
    for j in range(num):
        lis1 = []
        lis2 = []
        for partido in dic:
            lis1 += [dic[partido][0]]
            lis2 += [partido]

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

def obtem_partidos(territorios: dict) -> list:
    partidos = []
    for territorio in territorios:
        for partido in territorios[territorio]['votos']:
            if partido not in partidos:
                partidos.append(partido)
    
    return sorted(partidos)

def ordenar(res):
    for i in range(len(res)-1):
        for j in range(len(res)-i-1):
            if res[j][1] < res[j+1][1]:
                res[j], res[j+1] = res[j+1], res[j]
            elif res[j][1] == res[j+1][1]:
                if res[j][2] < res[j+1][2]:
                    res[j], res[j+1] = res[j+1], res[j]
  
    return res

def obtem_resultado_eleicoes(territorios):
    if not isinstance(territorios, dict):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    if len(territorios) < 1:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    for terrorio_e in territorios:
        if not isinstance(territorios[terrorio_e], dict) or not isinstance(terrorio_e, str): 
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if len(territorios[terrorio_e]) != 2:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if 'deputados' not in territorios[terrorio_e] or 'votos' not in territorios[terrorio_e]:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if not isinstance(territorios[terrorio_e]['deputados'], int) or not isinstance(territorios[terrorio_e]['votos'], dict):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if territorios[terrorio_e]['deputados'] < 1 or len(territorios[terrorio_e]['votos']) < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        votos = 0
        for partido_e in territorios[terrorio_e]['votos']:
            if not isinstance(partido_e, str): 
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            if not isinstance(territorios[terrorio_e]['votos'][partido_e], int) or territorios[terrorio_e]['votos'][partido_e] < 0:
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            votos += territorios[terrorio_e]['votos'][partido_e]
        if votos == 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    
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

    return ordenar(res)

#3

def produto_interno(tup1: tuple, tup2: tuple) -> float:
    res = 0
    for i in range(len(tup1)):
        res += (tup1[i]*tup2[i])
    return float(res)

def verifica_convergencia(matriz: tuple, constante: tuple, x: tuple, precisao: tuple) -> bool:
    i = 0
    for t in matriz:
        if abs(produto_interno(t, x) - constante[i]) > precisao:
            return False
        i += 1
    return True

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

def resolve_sistema(mat: tuple, cons: tuple, precisao: float) -> tuple:
    if not isinstance(mat, tuple) or not isinstance(cons, tuple) or not isinstance(precisao, float) or not 0 < precisao < 1:
        raise ValueError('resolve_sistema: argumentos invalidos')
    if len(mat) == 0 or len(cons) == 0:
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
    
    x1 = []
    x2 = []
    for k in range(len(matriz)):
            x1 += [0]
            x2 += [0]
    
    while not verifica_convergencia(matriz, constante, x2, precisao):  
        for j in range(len(x2)):
            x1[j] = x2[j]
        for i in range(len(x2)):
            x2[i] = x1[i] + (constante[i] - produto_interno(matriz[i], x1))/matriz[i][i]  
    
    return tuple(x2)

