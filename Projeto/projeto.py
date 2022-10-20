#1

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

