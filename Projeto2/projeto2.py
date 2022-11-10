#2.1.1
#TAD gerador
def cria_gerador(b, s):
    '''cria gerador : int x int 7 -> gerador
    Esta função recebe um inteiro b (bits) do gerador e um inteiro s (seed/estado inicial),
    e devolve o gerador (no formato TAD gerador) correspondente, verifica também a validade dos argumentos. '''
    if (b != 32 and b != 64) or not isinstance(b, int) or not isinstance(s, int) or s < 1 or s > (2**b)-1:
        raise ValueError('cria_gerador: argumentos invalidos')
    return {'bits': b, 'seed': s}  #estrutura do gerador é representada por um dicionário

def cria_copia_gerador(g):
    '''cria_copia_gerador: gerador -> gerador
    Esta função recebe um gerador g e devolve uma cópia do mesmo'''
    return g.copy()

def obtem_estado(g):
    '''obtem_estado: gerador -> int
    Esta função recebe um gerador e devolve o estado atual do gerador g'''
    return g['seed']

def define_estado(g,s):
    '''define_estado: gerador x int -> int
    Esta função recebe um gerador g define um novo valor do seu estado s,
    e devolve s'''
    g['seed'] = s
    return s

def atualiza_estado(g):
    '''atualiza_estado: gerador -> int
    Esta função recebe um gerador g e atualiza o estado do mesmo de acordo com o algoritmo
    xorshift de geraação de números pseudoaleatórios, devolvendo-o'''
    s = obtem_estado(g)
    if cria_copia_gerador(g)['bits'] == 32:
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
        define_estado(g,s)
    if cria_copia_gerador(g)['bits'] == 64:
        s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
        s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
        s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
        define_estado(g,s)
    return obtem_estado(g)

def eh_gerador(arg):
    '''eh_gerador: universal -> booleano
    Esta função verifica se o argumento arg é um TAD gerador (devolvendo True se sim, e False
    caso contrário)'''
    if isinstance(arg, dict) and len(arg) == 2:
        if 'bits' in arg and 'seed' in arg:
            if cria_copia_gerador(arg)['bits'] == 32 or cria_copia_gerador(arg)['bits'] == 64: 
                if isinstance(obtem_estado(arg), int) and (2**cria_copia_gerador(arg)['bits'])-1 >= obtem_estado(arg) >= 0:
                    return True
    return False

def geradores_iguais(g1, g2):
    '''geradores_iguais: gerador x gerador 7 -> booleano
    Esta função verifica se g1 e g2 são geradores e, se sim, se iguais (devolvendo True se sim, e 
    False caso contrário)'''
    if eh_gerador(g1) and eh_gerador(g2):
        if cria_copia_gerador(g1)['bits'] == cria_copia_gerador(g2)['bits'] and obtem_estado(g1) == obtem_estado(g2):
            return True
    return False

def gerador_para_str(g):
    '''gerador_para_str: gerador -> str
    Esta função recebe um gerador g e devolve uma cadeia de caracteres que representa
    o mesmo (da acordo com os exemplos da ficha do enunciado)'''
    return 'xorshift' + str(cria_copia_gerador(g)['bits']) + '(s=' + str(obtem_estado(g)) + ')'

def gera_numero_aleatorio(g,n):
    '''gera_numero_aleatorio: gerador x int -> int
    Esta função recebe um gerador g e um inteiro n e devolve um número aleatório 
    (depois de atualizar o estado) que está entre desde 1 até n'''
    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n)

def gera_carater_aleatorio(g,c):
    '''gera_caracter_aleatorio: gerador x str -> str
    Esta função recebe um gerador g e um caracter c e devolve um caracter aleatorio 
    (depois de atualizar o estado) que está entre 'A' e c (de acordo com o abecedário)'''
    atualiza_estado(g)
    return chr(65 + (obtem_estado(g) % (ord(c) - ord('A') + 1)))

#2.1.2
#TAD coordenada
def cria_coordenada(col, lin):
    '''cria_coordenada: str x int -> coordenada
    Esta função recebe um caracter col (coluna) e um numero lin (linha) e devolve a coordenada
    (no formato TAD coordenada) correspondente, verifica também a validade dos argumentos'''
    if not isinstance(col, str) or not isinstance(lin, int) or len(col) != 1 or not (65 <= ord(col) <= 90) or not (1 <= lin <= 99):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return {'col': col, 'lin': lin}  #estrutura da coordenada é representada por um dicionário

def obtem_coluna(c):
    '''obtem_coluna: coordenada -> str
    Esta função recebe uma coordenada c e devolve o valor da sua coluna'''
    return c['col']

def obtem_linha(c):
    '''obtem_linha: coordenada -> int
    Esta função recebe uma coordenada c e devolve o valor da sua linha'''
    return c['lin']

def eh_coordenada(arg):
    '''eh_coordenada: universal -> booleano
    Esta função verifica se o argumento arg é um TAD coordenada (devolvendo True se sim, e False
    caso contrário) '''
    if isinstance(arg, dict) and len(arg) == 2:
        if 'col' in arg and 'lin' in arg:
            if isinstance(obtem_coluna(arg), str) and isinstance(obtem_linha(arg), int) and len(obtem_coluna(arg)) == 1 and 65 <= ord(obtem_coluna(arg)) <= 90 and 1 <= obtem_linha(arg) <= 99:
                return True
    return False

def coordenadas_iguais(c1, c2):
    '''coordenadas_iguais: coordenada x coordenada -> booleano
    Esta função verifica se os argumentos c1 e c2 são coordenadas e, se sim, se são iguais 
    (devolvendo True se sim, e False caso contrário)'''
    if eh_coordenada(c1) and eh_coordenada(c2) and obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2):
        return True
    return False

def coordenada_para_str(c):
    '''coordenada_para_str: coordenada -> str
    Esta função recebe uma coordenada c e devolve uma cadeia de caracteres que representa
    a mesma (da acordo com os exemplos da ficha do enunciado)'''
    if obtem_linha(c) < 10:
        return obtem_coluna(c) + '0' + str(obtem_linha(c))
    else:
        return obtem_coluna(c) + str(obtem_linha(c))

def str_para_coordenada(s):
    '''str_para_coordenada: str -> coordenada
    Esta função recebe a cadeia de caracteres s e devolve a coordenada no formato TAD 
    coordenada'''
    if s[1] == 0:
        return {'col': s[0], 'lin': int(s[2])}
    else:
        return {'col': s[0], 'lin': int(s[1] + s[2])}

def obtem_coordenadas_vizinhas(c):
    '''obtem_coordenadas_vizinhas: coordenada -> tuplo
    Esta função recebe uma coordenada c e devolve um tuplo com todas as coordenadas
    vizinhas à mesma, o tuplo está ordenado (começando pela coordenada da diagonal acima à
    esquerda e seguindo os ponteiros do relógio)'''
    if obtem_coluna(c) == 'A':
        if obtem_linha(c) == 1: #3
            return (cria_coordenada('B', 1), cria_coordenada('B', 2), cria_coordenada('A', 2))
        elif obtem_linha(c) == 99: #3
            return (cria_coordenada('A', 98), cria_coordenada('B', 98), cria_coordenada('B', 99))
        else: #5
            return (cria_coordenada('A', obtem_linha(c)-1), cria_coordenada('B', obtem_linha(c)-1), cria_coordenada('B', obtem_linha(c)), 
            cria_coordenada('B', obtem_linha(c)+1), cria_coordenada('A', obtem_linha(c)+1)) 
    elif obtem_coluna(c) == 'Z':
        if obtem_linha(c) == 1: #3
            return (cria_coordenada('Z', 2), cria_coordenada('Y', 2), cria_coordenada('Y', 1))
        elif obtem_linha(c) == 99: #3
            return (cria_coordenada('Y', 98), cria_coordenada('Z', 98), cria_coordenada('Y', 99))
        else: #5
            return (cria_coordenada('Y', obtem_linha(c)-1), cria_coordenada('Z', obtem_linha(c)-1),
            cria_coordenada('Z', obtem_linha(c)+1), cria_coordenada('Y', obtem_linha(c)+1), cria_coordenada('Y', obtem_linha(c))) 
    elif obtem_linha(c) == 1: #5
            return (cria_coordenada(chr(ord(obtem_coluna(c))+1), 1), cria_coordenada(chr(ord(obtem_coluna(c))+1), 2),
            cria_coordenada(obtem_coluna(c), 2), cria_coordenada(chr(ord(obtem_coluna(c))-1), 2), cria_coordenada(chr(ord(obtem_coluna(c))-1), 1))
    elif obtem_linha(c) == 99: #5 
            return (cria_coordenada(chr(ord(obtem_coluna(c))-1), 98), cria_coordenada(obtem_coluna(c), 98),
            cria_coordenada(chr(ord(obtem_coluna(c))+1), 98), cria_coordenada(chr(ord(obtem_coluna(c))+1), 99), cria_coordenada(chr(ord(obtem_coluna(c))-1), 99))
    else: #8
            return (cria_coordenada(chr(ord(obtem_coluna(c))-1), obtem_linha(c)-1), cria_coordenada(obtem_coluna(c), obtem_linha(c)-1), cria_coordenada(chr(ord(obtem_coluna(c))+1), obtem_linha(c)-1), 
            cria_coordenada(chr(ord(obtem_coluna(c))+1), obtem_linha(c)), cria_coordenada(chr(ord(obtem_coluna(c))+1), obtem_linha(c)+1), cria_coordenada(obtem_coluna(c), obtem_linha(c)+1), 
            cria_coordenada(chr(ord(obtem_coluna(c))-1), obtem_linha(c)+1), cria_coordenada(chr(ord(obtem_coluna(c))-1), obtem_linha(c)))
            
def obtem_coordenada_aleatoria(c,g):
    '''obtem_coordenada_aleatoria: coordenada x gerador -> coordenada
    Esta função recebe uma coordenada c (contém a maior coluna e maior linha possíveis) 
    e um gerador g, e devolve uma coordenada gerada aleatoriamente (utilizando as funções
    de alto nível associadas ao TAD anterior)'''
    return cria_coordenada(gera_carater_aleatorio(g, obtem_coluna(c)), gera_numero_aleatorio(g, obtem_linha(c)))

#2.1.3 
#TAD parcela
def cria_parcela():
    '''cria_parcela: {} -> parcela
    Esta função devolve uma parcela tapada sem mina escondida (no formato TAD parcela)'''
    return {'estado': 'tapada', 'mina': False}  #estrutura da parcela é representada por um dicionário

def cria_copia_parcela(p):
    '''cria_copia_parcela: parcela -> parcela
    Esta função recebe uma parcela p e devolve uma cópia da mesma'''
    return p.copy()

def limpa_parcela(p):
    '''limpa_parcela: parcela -> parcela
    Esta função recebe uma parcela p modifica destrutivamente a mesma, alterando o seu estado 
    para limpa, e devolve a própria parcela'''
    p['estado'] = 'limpa'
    return p

def marca_parcela(p):
    '''marca_parcela: parcela -> parcela
    Esta função recebe uma parcela p modifica destrutivamente a mesma, alterando o seu estado 
    para marcada, e devolve a própria parcela'''
    p['estado'] = 'marcada'
    return p

def desmarca_parcela(p):
    '''desmarca_parcela: parcela -> parcela
    Esta função recebe uma parcela p modifica destrutivamente a mesma, alterando o seu estado 
    para tapada, e devolve a própria parcela'''
    p['estado'] = 'tapada'
    return p

def esconde_mina(p):
    '''esconde_mina: parcela -> parcela
    Esta função recebe uma parcela p modifica destrutivamente a mesma, escondendo uma mina na mesma, 
    e devolve a própria parcela'''
    p['mina'] = True
    return p

def eh_parcela(arg):
    '''eh_parcela: unversal -> booleano
    Esta função verifica se o argumento arg é um TAD parcela (devolve True se sim, e False
    caso contrário'''
    if isinstance(arg, dict) and len(arg) == 2:
        if 'estado' in arg and 'mina' in arg:
            if isinstance(cria_copia_parcela(arg)['estado'], str) and isinstance(cria_copia_parcela(arg)['mina'], bool) and (cria_copia_parcela(arg)['estado'] == 'limpa'
            or cria_copia_parcela(arg)['estado'] == 'marcada' or cria_copia_parcela(arg)['estado'] == 'tapada'):
                return True
    return False

def eh_parcela_tapada(p):
    '''eh_parcela_tapada: parcela -> booleano
    Esta função recebe uma parcela p e devolve True no caso desta estar tapada,
    e devolve False caso contrário'''
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'tapada':
        return True
    return False

def eh_parcela_marcada(p):
    '''eh_parcela_marcada: parcela -> booleano
    Esta função recebe uma parcela p e devolve True no caso desta estar marcada,
    e devolve False caso contrário'''
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'marcada':
        return True
    return False

def eh_parcela_limpa(p):
    '''eh_parcela_limpa: parcela -> booleano
    Esta função recebe uma parcela p e devolve True no caso desta estar limpa,
    e devolve False caso contrário'''
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'limpa':
        return True
    return False

def eh_parcela_minada(p):
    '''eh_parcela_minada: parcela -> booleano
    Esta função recebe uma parcela p e devolve True no caso desta estar minada,
    e devolve False caso contrário'''
    if eh_parcela(p) and cria_copia_parcela(p)['mina']:
        return True
    return False

def parcelas_iguais(p1, p2):
    '''parcelas_iguais: parcela x parcela: booleano
    Esta função recebe duas parcelas p1 e p2 e devolve True se ambas forem parcelas e se
    forem iguais'''
    if eh_parcela(p1) and eh_parcela(p2) and cria_copia_parcela(p1)['estado'] == cria_copia_parcela(p2)['estado'] and cria_copia_parcela(p1)['mina'] == cria_copia_parcela(p2)['mina']:
        return True
    return False

def parcela_para_str(p):
    '''parcela_para_str: parcela -> str
    Esta função recebe uma parcela p e devolve a representação do seu estado na forma de
    cadeia de caracteres'''
    if eh_parcela_tapada(p):
        return '#'
    if eh_parcela_marcada(p):
        return '@'
    if eh_parcela_limpa(p) and not eh_parcela_minada(p):
        return '?'
    if eh_parcela_limpa(p) and eh_parcela_minada(p):
        return 'X'
    
def alterna_bandeira(p):
    '''alterna_bandeira: parcela -> booleano
    Esta função recebe uma parcela p e modifica a mesma destrutivamente (desmarca se estiver
    marcada e marca se estiver tapada - devolve True, em qualquer outro caso - devolve False)
    '''
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    else:
        return False

#2.1.4    
#TAD campo
def cria_campo(c, l):
    '''cria_campo: str x int -> campo
    Esta função recebe uma cadeia de caracteres c (ultima coluna) e um inteiro l (ultima linha), 
    e devolve um campo (no formato TAD campo) do tamanho obtido a partir da ultima coluna e linha
    (constituido por parcelas tapadas sem minas), esta função também verifica a validade dos seus 
    argumentos'''
    try:
        cria_coordenada(c,l)
    except ValueError:
        raise ValueError('cria_campo: argumentos invalidos')
    campo = {}
    for i in range(1, l+1):
        for j in range(65, ord(c)+1):
            campo[coordenada_para_str(cria_coordenada(chr(j), i))] = cria_parcela()
    return campo  #a estrutura do campo é representada por um dicionário

def cria_copia_campo(m):
    '''cria_copia_campo: campo -> campo
    Esta função recebe um campo m e devolve uma cópia do mesmo'''
    copia_campo = {}
    for i in m:
        copia_campo[i] = m[i].copy()
    return copia_campo

def obtem_ultima_coluna(m):
    '''obtem_ultima_coluna: campo -> str
    Esta função recebe um campo m e devolve a cadeia de caracteres correspondente à ultima
    coluna do mesmo'''
    return obtem_coluna(str_para_coordenada(list(m)[-1]))

def obtem_ultima_linha(m):
    '''obtem_ultima_linha: campo -> int
    Esta função recebe um campo m e devolve o inteiro correspondente à ultima linha do mesmo'''
    return obtem_linha(str_para_coordenada(list(m)[-1]))

def obtem_parcela(m, c):
    '''obtem_parcela: campo x coordenada -> parcela
    Esta função recebe um campo m e uma coordenada c e devolve a parcela de m que se encontra
    em c'''
    return m[coordenada_para_str(c)]

def obtem_coordenadas(m, s):
    '''obtem_coordenadas: campo x str -> tuplo
    Esta função recebe um campo m e uma cadeia de caracteres s e devolve um tuplo formado
    pelas coordenadas de m cujo estado é "s" (as coordenadas dentro do tuplo estão por ordem
    ascendente de esquerda `a direita e de cima a baixo)'''
    res = []
    if s == 'limpas':
        for i in m:
            if eh_parcela_limpa(obtem_parcela(m, str_para_coordenada(i))):
                res.append(str_para_coordenada(i))
    if s == 'tapadas':
        for i in m:
            if eh_parcela_tapada(obtem_parcela(m, str_para_coordenada(i))):
                res.append(str_para_coordenada(i))
    if s == 'marcadas':
        for i in m:
            if eh_parcela_marcada(obtem_parcela(m, str_para_coordenada(i))):
                res.append(str_para_coordenada(i))
    if s == 'minadas':
        for i in m:
            if eh_parcela_minada(obtem_parcela(m, str_para_coordenada(i))):
                res.append(str_para_coordenada(i))
    return tuple(res)

def eh_coordenada_do_campo(m,c):
    '''eh_coordenada_do_campo: campo x coordenada -> booleano
    Esta função recebe um campo m e uma coordenada c e devolve True se esta estiver dentro do campo
    (devolve False caso contrário)'''
    return coordenada_para_str(c) in m

def obtem_numero_minas_vizinhas(m,c):
    '''obtem_numero_minas_vizinhas: campo x coordenada -> int
    Esta função recebe um campo m e uma coordenada c e devolve a quantidade de parcelas vizinhas que
    têm uma mina escondida'''
    viz = obtem_coordenadas_vizinhas(c)
    counter = 0
    for i in tuple(coordenada_para_str(p) for p in viz):
        if eh_coordenada_do_campo(m, str_para_coordenada(i)):
            if eh_parcela_minada(obtem_parcela(m, str_para_coordenada(i))):
                counter += 1
    return counter

def eh_campo(arg):
    '''eh_campo: universal -> booleano
    Esta função verifica se o argumento arg é um campo (devolve True se sim, False caso contrário)'''
    if isinstance(arg, dict) and len(arg) != 0:
        for i in cria_copia_campo(arg):
            if not eh_coordenada(str_para_coordenada(i)) or not eh_parcela(cria_copia_campo(arg)[i]):
                return False
        return True
    return False    
    
def campos_iguais(m1,m2):
    '''campos_iguais: campo x campo -> booleano
    Esta função recebe dois campos m1 e m2, e se ambos forem campos e forem iguais, devolve True
    (devolve False caso contrário)'''
    if eh_campo(m1) and eh_campo(m2):
        if len(m1) == len(m2):
            for i in m1:
                if i in m2 and obtem_parcela(m1, str_para_coordenada(i)) != obtem_parcela(m2, str_para_coordenada(i)):
                    return False
            return True
    return False

def campo_para_str(m):
    '''campo_para_str: campo -> str
    Esta função recebe um campo m e devolve uma cadeia de caracteres que representa o mesmo
    (da acordo com os exemplos da ficha do enunciado)'''
    string1 = '   '
    string2 = '  +'
    string3 = ''
    lis1 = []
    for i in range(65, ord(obtem_ultima_coluna(m))+1):
        lis1 += [chr(i)]
        string1 += chr(i)
        string2 += '-'
    
    string1 += '\n'
    string2 += '+\n' 

    for j in range(1, obtem_ultima_linha(m)+1):
        if j < 10:
            string3 += '0' + str(j)
        else:
            string3 += str(j) 
        string3 += '|'
        for k in lis1:
            if parcela_para_str(obtem_parcela(m, cria_coordenada(k,j))) == '?':
                if obtem_numero_minas_vizinhas(m, cria_coordenada(k,j)) > 0:
                    string3 += str(obtem_numero_minas_vizinhas(m, cria_coordenada(k,j)))
                else:
                    string3 += ' '
            else:
                string3 += parcela_para_str(obtem_parcela(m, cria_coordenada(k,j)))
        string3 += '|\n'

    return string1 + string2 + string3 + string2[:-1]

def coloca_minas(m, c, g, n):
    '''coloca_minas: campo x coordenada x gerador x int -> campo
    Esta função recebe um campo m, uma coordenada c, um gerador g e um inteiro n, modifica 
    destrutivamente m, colocando minas em n coordenadas aleatórias (não coincidentes com c
    nem com as suas coordenadas vizinhas) sem sobreposição das mesmas, e devolve o campo 
    alterado'''
    coord_proib = [coordenada_para_str(c)] 
    for i in obtem_coordenadas_vizinhas(c):
        if eh_coordenada_do_campo(m, i):
            coord_proib.append(coordenada_para_str(i))
    while n > 0:
        ulti_c = cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m))
        mina_c = obtem_coordenada_aleatoria(ulti_c, g)
        if coordenada_para_str(mina_c) not in coord_proib:
            esconde_mina(obtem_parcela(m, mina_c))
            coord_proib.append(coordenada_para_str(mina_c))
            n -= 1
    return m

def limpa_campo(m, c):
    '''limpa_campo: campo x coordenada -> campo
    Esta função recebe um campo m e uma coordenada c, modifica destrutivamente m, limpando 
    a parcela da coordenada c (limpa parcelas vizinhas, no casp de não terem minas na sua 
    vizinhança)'''
    if eh_parcela_limpa(obtem_parcela(m,c)):
        return m
    else:
        if eh_parcela_minada(obtem_parcela(m, c)) or obtem_numero_minas_vizinhas(m, c) >= 1:
            limpa_parcela(obtem_parcela(m, c))
            return m
        limpa_parcela(obtem_parcela(m, c))
        n_analisadas = []
        if obtem_numero_minas_vizinhas(m, c) == 0:
            for i in obtem_coordenadas_vizinhas(c):
                if eh_coordenada_do_campo(m, i) and not eh_parcela_limpa(obtem_parcela(m, i)) and not eh_parcela_marcada(obtem_parcela(m, i)):
                    limpa_parcela(obtem_parcela(m, i))
                    n_analisadas.append(i)
        while len(n_analisadas) > 0:
            n_analisadas_l = n_analisadas.copy()
            for j in n_analisadas_l:
                n_analisadas.remove(j)
                if obtem_numero_minas_vizinhas(m, j) == 0:
                    for k in obtem_coordenadas_vizinhas(j):
                        if eh_coordenada_do_campo(m, k) and not eh_parcela_limpa(obtem_parcela(m, k)) and not eh_parcela_marcada(obtem_parcela(m, k)):
                            limpa_parcela(obtem_parcela(m, k))
                            n_analisadas.append(k)
        return m

#2.2.1
def jogo_ganho(m):
    '''jogo_ganho: campo -> booleano
    Esta função recebe um campo m e devolve True se todas as parcelas de m que não têm 
    minas estiverem limpas'''
    if len(obtem_coordenadas(m, 'minadas')) == len(obtem_coordenadas(m, 'marcadas')) + len(obtem_coordenadas(m, 'tapadas')):
        return True
    return False

#2.2.2
def str_para_int_aux(n):
    '''str_para_aux: universal -> booleano
    Esta função verifica se não é possível tornar o argumento n em inteiro (devolvendo 
    True se não for) - função auxiliar às funções turno_jogador e minas'''
    try:
        int(n)
    except ValueError:
        return True

def turno_jogador(m):
    '''turno_jogador: campo -> bool
    Esta função recebe um campo m e permite ao jogador escolher uma ação (Limpar ou Marcar)
    e uma coordenada para aplicar esta ação, se o jogaodor escolher limpar uma parcela
    que contém uma mina, a função limpa a parcela e devolve False, caso contrário,
    se o jogador limpar uma parcela não minada, o mesmo limpa a parcela (e vizinhas - de 
    acordo com a função limpa_campo), devolvendo True, e se o jogador marcar uma parcela,
    a função alterna a bandeira da parcela (de acordo com a função alterna_bandeira), 
    devolvendo True'''
    action = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while not (action == 'L' or action == 'M'):
        action = input('Escolha uma ação, [L]impar ou [M]arcar:')
    coord = input('Escolha uma coordenada:')
    while len(coord) != 3 or str_para_int_aux(coord[1:]) or (int(coord[1:]) < 10 and len(coord[1:]) < 2) or not eh_coordenada_do_campo(m, str_para_coordenada(coord)):
        coord = input('Escolha uma coordenada:')
    if action == 'L':
        if eh_parcela_minada(obtem_parcela(m, str_para_coordenada(coord))):
            limpa_campo(m, str_para_coordenada(coord))
            return False
        else:
            limpa_campo(m, str_para_coordenada(coord))
            return True
    elif action == 'M':
        alterna_bandeira(obtem_parcela(m, str_para_coordenada(coord)))
        return True

#2.2.3
def minas(c, l, n, d, s):
    '''minas: str x int x int x int x int -> booleano
    Esta função permite jogar o jogo das minas. A mesma recebe a ultima coluna c e a
    ultima linha l de um campo, um numero de parcelas minadas n, uma dimensao d e uma
    seed s se um gerador, e devolve True se o jogador conseguir ganhar o jogo (False
    caso contrário). Começando por verificar a validade dos argumentos, a função pede 
    ao jogador uma coordenada para começar o jogo e, a partir daí, planta n minas no
    campo (de acordo coma função coloca_minas) depois, enquanto o jogo não está ganho
    (de acordo com a função jogo_ganho), pede ao jogador ações e coordenadas (de acordo
    coma função turno_jogaodor). No caso de ganhar, o jogador recebe a mensagem "VITORIA!!!",
    no caso de perder (a função turno_jogador devolver Falso), o jogador recebe a mensagem
    "BOOOOOOOM!!!"'''
    try:
        cria_gerador(d, s)
        cria_campo(c, l)
    except ValueError:
        raise ValueError('minas: argumentos invalidos')
    if not isinstance(n, int) or n < 1 or n > len(cria_campo(c, l)):
        raise ValueError('minas: argumentos invalidos')
    if (l < 3 and (64 - ord(c)) < 2) or (l < 3 and (64 - ord(c)) < 2):
        raise ValueError('minas: argumentos invalidos')
    g = cria_gerador(d, s)
    m = cria_campo(c, l)
    bandeiras = 0
    print(f'   [Bandeiras {bandeiras}/{n}]')
    print(campo_para_str(m))
    coord_minas = input('Escolha uma coordenada:')
    while len(coord_minas) != 3 or str_para_int_aux(coord_minas[1:]) or (int(coord_minas[1:]) < 10 and len(coord_minas[1:]) < 2) or not eh_coordenada_do_campo(m, str_para_coordenada(coord_minas)):
        coord_minas = input('Escolha uma coordenada:')
    coloca_minas(m, str_para_coordenada(coord_minas), g, n)
    limpa_campo(m, str_para_coordenada(coord_minas))
    print(f'   [Bandeiras {bandeiras}/{n}]')
    print(campo_para_str(m))
    while not jogo_ganho(m):
        if not turno_jogador(m):
            bandeiras = len(obtem_coordenadas(m, 'marcadas'))
            print(f'   [Bandeiras {bandeiras}/{n}]')
            print(campo_para_str(m))
            print('BOOOOOOOM!!!')
            return False
        else:
            bandeiras = len(obtem_coordenadas(m, 'marcadas'))
            print(f'   [Bandeiras {bandeiras}/{n}]')
            print(campo_para_str(m)) 
    print('VITORIA!!!')
    return True

#minas('N', 6, 6, 32, 100)