def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} qualquer e devolve
    a cadeia de carateres limpa (utilizando join e split) que corresponde à remoção de carateres 
    brancos.""" 
    return ' '.join(s.split())        #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  

#print(limpa_texto(test1))

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

print(corta_texto('Computers are incredibly fast, accurate and stupid. Human beings are incredibly slow inaccurate, and brilliant. Together they are powerful beyond imagination.', 60))

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

#print(insere_espacos('Fundamentos da Programacao!!!', 30))

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

#print(justifica_texto(cad, 6))
