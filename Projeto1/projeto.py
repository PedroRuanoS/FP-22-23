#1

#1.2.1
def limpa_texto(texto: str) -> str:
    """Esta função recebe uma cadeia de carateres e devolve a cadeia de carateres 
    "limpa", ou seja, são retirados os caracteres \t,\n,\v,\f,\r, dois ou mais espaços 
    seguidos e espaços no inicio ou no fim da cadeia.""" 

    return ' '.join(texto.split())                 #split: Transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r. join: Transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.

#1.2.2
def corta_texto(texto: str, numero: int) -> tuple:
    """Esta função recebe um texto limpo (cadeia de caracteres) e uma largura de coluna 
    (inteiro) e devolve duas subcadeias de carateres limpas em que a primeira é a subcadeia 
    com a quantidade de caracteres igual à largura fornecida e a segunda é a subdeia que 
    contém o resto do texto de entrada"""                 
   
    n = texto.split()                      #transfoma uma cadeia de caracteres numa lista 
    res = [] 
    resto = texto.split()                  #transfoma uma cadeia de caracteres numa lista  
    
    for p in n:                         
        if len(p) <= numero:                  
            res.append(p)              #adiciona um item à lista {res1} e remove-o da lista {resto} até um item ter uma largura maior que {i}        
            numero -= len(p) + 1                
            resto.remove(p)              
        else: 
            break

    return (' '.join(res), ' '.join(resto))   #junta as cadeias de caracteres num tuplo

#1.2.3
def insere_espacos(texto: str, numero: int) -> str:
    '''Esta função recebe um texto limpo (cadeia de caracteres) uma largura de coluna
    (inteiro) e insere ' ' entre as palavras, devolvendo uma cadeia de caracteres com 
    a largura igual ao numero recebido inicialmente'''
    n = texto.split()
    i = len(n) - 1             #{i}: quantidade de sitios onde se tem de adicionar espaços

    for c in n:
        numero -= len(c)         #retira a num a quantidade de caracteres (não vazios) de {car} para se ver quantos ' ' vão ser necessários de colocar                  
    if len(n) == 1:           #no caso de {car} só conter uma palavra 
        for d in range(numero):
            n.append(' ')      
    else:                     #no caso de {car} conter uma ou mais palavras
        k = 1   
        while numero > 0:       
            k += 1
            j = -1
            for e in range(i):
                j += k
                n.insert(j, ' ')    #insire ' ' à direita da coordenada {j} (que começa como 0, e aumenta exponencialmente, a partir de {k}) 
                numero -= 1            
                if numero == 0:        #para o ciclo (for) se já não houver espaços a adicionar (para depois o ciclo (while) também parar)
                    break
            
    return ''.join(n)

#1.2.4
def justifica_texto(texto: str, numero: int) -> tuple:
    '''Esta função recebe uma cadeia de caracteres não vazia e um inteiro positivo,
    verifica a validade dos seus argumentos e devolve um tuplo com cadeias de caracteres
    com comprimento igual ao numero recebido (a partir da inserção de espaços e corte no
    texto recebido)'''
    if not isinstance(numero, int) or not isinstance(texto, str) or len(texto) == 0: #verifica se os tipos de variável estão certos
        raise ValueError('justifica_texto: argumentos invalidos')
    erro = texto.split()
    for palavra in erro:                
        if len(palavra) > numero:        #verifica se o tamanho da palavra é maior que o tamanho de linha recebido
            raise ValueError('justifica_texto: argumentos invalidos')

    text = limpa_texto(texto)       
    resto = text                    
    res = []
    rest = resto.split()            #{rest}: separamos os elementos de {resto} (que começa igual a {text}) ignorando caracteres brancos

    while len(resto) > numero:      #enquanto a largura de {resto} (que vai ser alterado) é maior do que o tamanho da linha recebido
        n = corta_texto(resto, numero)[0]   #pega no primeiro elemento do tuplo recebido pela função corta_texto
        o = n.split()                      
        m = insere_espacos(n, numero)       
        res.append(m)                       
        for i in o:                         
            rest.remove(i)                  #remove do {resto} a parte que foi cortada do texto
        resto = ' '.join(rest)              

    t = numero - len(resto)                 
    if t%2 == 0:                            #se {t} for par
        for j in range(int(t/2)):           
            rest.append(' ')                #adiciona a {rest} metade dos ' ' necessários de adicionar
            resto = ' '.join(rest)          #o método join adiciona a outra metade
    else:                                   
        for j in range(int((t+1)/2)):       
            rest.append(' ')                #adiciona a {rest} metade (arrendondada às unidades) dos ' ' necessários de adicionar
            resto = (' '.join(rest))[:-1]   #o método de join adiciona a outra métade (porém, vem um espaço a mais) por isso {resto} é tudo menos o último elemento da string
            
    res.append(resto)                       
    return tuple(res)  

#2

#2.2.1
def calcula_quocientes(partidos: dict, num: int) -> dict:
    '''Esta função recebe um dicionário com os partidos e os seus votos e o numero de deputados
    e devolve um dicionário tantos quocientes (calculados com o método de Hondt) quanto 
    é o valor do numero de deputados, ordenados por ordem descrescente'''
    dic = {}
    for partido in partidos:
        div = []
        for i in range(num + 1):    #{i} cresce até num + 1 visto que no primeiro loop este é 0
            if i > 0:               
                div += [partidos[partido]/i]        
        dic[partido] = div
    
    return dic

#2.2.2
def atribui_mandatos(partidos: dict, num: int) -> list:
    '''Esta função recebe um dicionário com os partidos e os seus votos e o numero de 
    deputados e devolve uma lista (cuja largura é igual ao numero de deputados) com 
    os partidos os quais foi atribuido cada mandato'''
    res = []
    dic = calcula_quocientes(partidos, num)
    for j in range(num):
        lis1 = []
        lis2 = []
        for partido in dic:                   
            lis1 += [dic[partido][0]]       #lista com o número de votos de cada partido
            lis2 += [partido]               #lista com o nome dos partidos

        maiores = []
        for k in range(len(lis1)):
            if lis1[k] == max(lis1):
                maiores += [lis2[k]]       #lista com o(os) nome(s) do(s) partido(s) com mais votos
    
        if len(maiores) > 1:                #se houver dois ou mais partidos com o maior número de votos (número igual)
            menor = maiores[0]
            for partido in maiores:         
                if partidos[partido] < partidos[menor]:     #acede ao dicionario recebido pela função e vê qual dos partidos tinha menos votos no inicio
                    menor = partido
            res += [menor]                     #atribui o mandato
            dic[menor].pop(0)                  #retira de {dic} o quociente atual do partido cujo mandato foi atribuido
        else:
            max_i = lis1.index(max(lis1))      
            res += [lis2[max_i]]               #atribui o mandato ao elemento da {lis1} com o mesmo indice do maior elemento da {lis2}
            dic[lis2[max_i]].pop(0)
        
    return res

#2.2.3
def obtem_partidos(territorios: dict) -> list:
    '''Esta função recebe um dicionário com os circulos eleitorais de um territorio 
    e devolve uma lista com todos os partidos que participaram nas eleições
    (por ordem alfabética)'''
    partidos = []
    for territorio in territorios:
        for partido in territorios[territorio]['votos']:    #acede à secção de 'votos' de cada terra do dicionario 
            if partido not in partidos:
                partidos.append(partido)                    #adiciona à lista o nome do partido se o nome do mesmo ainda não estiver na mesma 
    
    return sorted(partidos)

def ordenar(res):  
    '''Esta função recebe uma lista com tuplos, em que cada tuplo tem tamanho 3
    (nome do partido, numero total de deputados, numero total de votos) e devolve
    a lista ordenada por ordem decrescente de acordo com os deputados obtidos
    (no caso de numero de deputados igual, é de acordo com o número de votos)'''     
    for i1 in range(len(res)-1):
        for i2 in range(len(res)-i1-1):
            if res[i2][1] < res[i2+1][1]:
                res[i2], res[i2+1] = res[i2+1], res[i2]
            elif res[i2][1] == res[i2+1][1]:
                if res[i2][2] < res[i2+1][2]:
                    res[i2], res[i2+1] = res[i2+1], res[i2]
  
    return res

#2.2.4
def obtem_resultado_eleicoes(territorios):
    '''Esta função recebe um dicionário com os circulos eleitorais de um territorio
    e devolve uma lista ordenada (com o mesmo tamanho do numero de partidos) - 
    ordem da lista explicada na função {ordenar}'''
    if not isinstance(territorios, dict) or len(territorios) < 1:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido') #verifica se o tipo de dados de entrada está certo
    for terrorio_e in territorios:
        if not isinstance(territorios[terrorio_e], dict) or not isinstance(terrorio_e, str) or len(territorios[terrorio_e]) != 2 or 'deputados' not in territorios[terrorio_e] or 'votos' not in territorios[terrorio_e] or not isinstance(territorios[terrorio_e]['deputados'], int) or not isinstance(territorios[terrorio_e]['votos'], dict) or territorios[terrorio_e]['deputados'] < 1 or len(territorios[terrorio_e]['votos']) < 1: 
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')    #verifica se o tipo de dados de cada circulo está certo e se os valores estão certos
        votos = 0
        for partido_e in territorios[terrorio_e]['votos']:
            if not isinstance(partido_e, str) or not isinstance(territorios[terrorio_e]['votos'][partido_e], int) or territorios[terrorio_e]['votos'][partido_e] < 0: 
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')    #verifica se o tipo de dados de cada partido está certo e se os valores estão certos
            votos += territorios[terrorio_e]['votos'][partido_e]
        if votos == 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')    #verifica se dentro de um certo circulo os partidos não têm todos 0 votos
    
    partidos = obtem_partidos(territorios)
    soma = {}
    for i in partidos:  #cria dicionario com os nomes dos partidos como chaves e com zero mandatos cada um
        soma[i] = 0

    mandatos = []
    for territorio in territorios:
        for partido in territorios[territorio]['votos']:
            soma[partido] = soma[partido] + territorios[territorio]['votos'][partido]
        mandato = atribui_mandatos(territorios[territorio]['votos'], territorios[territorio]['deputados'])  #acede a cada circulo e atribui mandatos (a partir da função atribui_mandatos) de acordo com a quantidade de votos e mandatos
        mandatos += mandato            #junta os mandatos atribuidos em todos os circulos numa só lista

    res = []
    for partido_total in soma:  #acede a cada partido
        counter = 0
        for j in mandatos:  #acede à lista com o nome dos partidos cujos mandatos foram atribuidos
            if j == partido_total:
                counter += 1    #quantidade de deputados que o partido obteve no território inteiro
        res.append((partido_total, counter, soma[partido_total]))

    return ordenar(res) 

#3

#3.2.1
def produto_interno(tup1: tuple, tup2: tuple) -> float:
    '''Esta função recebe dois vetores (tuplos) com o mesmo tamanho e devolve o produto interno
    entre os mesmos'''
    res = 0
    for i in range(len(tup1)):
        res += (tup1[i]*tup2[i])

    return float(res)

#3.2.2
def verifica_convergencia(matriz: tuple, constante: tuple, x: tuple, precisao: tuple) -> bool:
    '''Esta função recebe três tuplos (matriz, vetor das constantes e solução atual) 
    com o mesmo tamanho e um numero real positivo e devolve um valor lógico (verdadeiro 
    se o módulo do produto interno entre uma linha da matriz e a solução atual for
    menor do que a precisao e falso caso contrário)'''
    i = 0
    for linha in matriz:
        if abs(produto_interno(linha, x) - constante[i]) >= precisao:
            return False
        i += 1

    return True

#3.2.3
def retira_zeros_diagonal(matriz: tuple, constante: tuple) -> tuple:
    '''Esta função recebe um tuplo com tuplos (matriz) e um tuplo (vetor das constantes)
    com o mesmo tamanho e devolve a matriz com as linhas reordenadas, de forma a deixar
    de ter zeros na diagonal, e o vetor das constantes (também reordenado, de acordo
    com a matriz)'''
    list_m = list(matriz)
    list_c = list(constante)
    
    for i in range(len(matriz)):
        if list_m[i][i] == 0:                   #se o elemento dessa linha que está na diagonal for 0 
            for j in range(len(matriz)):
                if list_m[i][j] != 0 and list_m[j][i] != 0 and i != j:   #verifica se há condições para se trocar de linhas
                    list_m[i], list_m[j] = list_m[j], list_m[i]
                    list_c[i], list_c[j] = list_c[j], list_c[i]
                    break
        
    return (tuple(list_m), tuple(list_c)) 

#3.2.4
def eh_diagonal_dominante(matriz: tuple) -> bool:
    '''Esta função recebe um tuplo com tuplos (matriz) e devolve um valor lógico
    (verdadeiro se o módulo do valor da diagonal for menor que o módulo da soma 
    dos outros elementos da mesma linha, falso caso contrário)'''
    for i in range(len(matriz)):
        linha = 0
        for j in range(len(matriz[i])):
            if j == i:
                diag = abs(matriz[i][j])    #módulo do valor da diagonal
            else:
                linha += abs(matriz[i][j]) #módulo da soma dos elementos da linha (sem ser da diagonal)
        if diag < linha:           
            return False            #a diagonal não é dominante

    return True

#3.2.5
def resolve_sistema(mat: tuple, cons: tuple, precisao: float) -> tuple:
    '''Esta função recebe um tuplo com tuplos (matriz), um tuplo (vetor das constantes)
    e um real (precisao), verifica a validade dos argumentos e devolve um tuplo (solução
    do sistema de equações - depois de aplicado o método de Jacobi)'''
    if not isinstance(mat, tuple) or not isinstance(cons, tuple) or not isinstance(precisao, float) or not 0 < precisao < 1 or len(mat) == 0 or len(cons) == 0: 
        raise ValueError('resolve_sistema: argumentos invalidos')               #verifica se o tipo das variáveis está correto e se o tamanho das variáveis está correto
    for num in cons:
        if not isinstance(num, (int, float)):                                   #verifica se o tipo da variável está correto dentro da constante
            raise ValueError('resolve_sistema: argumentos invalidos')
    for linha in mat:
        if not isinstance(linha, tuple) or len(linha) != len(mat) or len(linha) != len(cons):
            raise ValueError('resolve_sistema: argumentos invalidos')           #verifica se o tipo das variáveis está correto e se o tamanho das variáveis está correto dentro da matriz
        for num in linha:
            if not isinstance(num, (int, float)):                               #verifica se o tipo da variável está correto dentro da linha da matriz
                raise ValueError('resolve_sistema: argumentos invalidos') 
    matriz, constante = retira_zeros_diagonal(mat, cons)

    if not eh_diagonal_dominante(matriz):
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    
    x1 = []
    x2 = []
    for k in range(len(matriz)):  #cria dois vetores nulos com o mesmo tamanho das colunas (e linhas) da matriz
            x1 += [0]
            x2 += [0]
    
    while not verifica_convergencia(matriz, constante, x2, precisao):  #enquanto o módulo da entro produto interno e o vetor das constantes for maior que a precisão
        for j in range(len(x2)):
            x1[j] = x2[j]                 #iguala os vetores
        for i in range(len(x2)):
            x2[i] = x1[i] + (constante[i] - produto_interno(matriz[i], x1))/matriz[i][i]  #atualiza o elemento do vetor x2 para ser verificada a convergencia
    
    return tuple(x2)

