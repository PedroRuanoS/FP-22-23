#2.1.1
#TAD gerador
def cria_gerador(b, s):
    if (b != 32 and b != 64) or not isinstance(b, int) or not isinstance(s, int) or s < 1 or s > (2**b)-1:
        raise ValueError('cria_gerador: argumentos invalidos')
    return {'bits': b, 'seed': s}

def cria_copia_gerador(g):
    return g.copy()

def obtem_estado(g):
    return g['seed']

def define_estado(g,s):
    g['seed'] = s
    return s

def atualiza_estado(g):
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
    if isinstance(arg, dict) and len(arg) == 2:
        if 'bits' in arg and 'seed' in arg:
            if cria_copia_gerador(arg)['bits'] == 32 or cria_copia_gerador(arg)['bits'] == 64: 
                if isinstance(obtem_estado(arg), int) and (2**cria_copia_gerador(arg)['bits'])-1 >= obtem_estado(arg) >= 0:
                    return True
    return False

def geradores_iguais(g1, g2):
    if eh_gerador(g1) and eh_gerador(g2):
        if cria_copia_gerador(g1)['bits'] == cria_copia_gerador(g2)['bits'] and obtem_estado(g1) == obtem_estado(g2):
            return True
    return False

def gerador_para_str(g):
    return 'xorshift' + str(cria_copia_gerador(g)['bits']) + '(s=' + str(obtem_estado(g)) + ')'

def gera_numero_aleatorio(g,n):
    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n)

def gera_carater_aleatorio(g,c):
    atualiza_estado(g)
    return chr(65 + (obtem_estado(g) % (ord(c) - ord('A') + 1)))

#2.1.2
#TAD coordenada
def cria_coordenada(col, lin):
    if not isinstance(col, str) or not isinstance(lin, int) or len(col) != 1 or not (65 <= ord(col) <= 90) or not (1 <= lin <= 99):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return {'col': col, 'lin': lin}

def obtem_coluna(c):
    return c['col']

def obtem_linha(c):
    return c['lin']

def eh_coordenada(arg):
    if isinstance(arg, dict) and len(arg) == 2:
        if 'col' in arg and 'lin' in arg:
            if isinstance(obtem_coluna(arg), str) and isinstance(obtem_linha(arg), int) and len(obtem_coluna(arg)) == 1 and 65 <= ord(obtem_coluna(arg)) <= 90 and 1 <= obtem_linha(arg) <= 99:
                return True
    return False

def coordenadas_iguais(c1, c2):
    if eh_coordenada(c1) and eh_coordenada(c2) and obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2):
        return True
    return False

def coordenada_para_str(c):
    if obtem_linha(c) < 10:
        return obtem_coluna(c) + '0' + str(obtem_linha(c))
    else:
        return obtem_coluna(c) + str(obtem_linha(c))

def str_para_coordenada(s):
    if s[1] == 0:
        return {'col': s[0], 'lin': int(s[2])}
    else:
        return {'col': s[0], 'lin': int(s[1] + s[2])}

def obtem_coordenadas_vizinhas(c):
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
    return cria_coordenada(gera_carater_aleatorio(g, obtem_coluna(c)), gera_numero_aleatorio(g, obtem_linha(c)))

#2.1.3 
#TAD parcela
def cria_parcela():
    return {'estado': 'tapada', 'mina': False}

def cria_copia_parcela(p):
    return p.copy()

def limpa_parcela(p):
    p['estado'] = 'limpa'
    return p

def marca_parcela(p):
    p['estado'] = 'marcada'
    return p

def desmarca_parcela(p):
    p['estado'] = 'tapada'
    return p

def esconde_mina(p):
    p['mina'] = True
    return p

def eh_parcela(arg):
    if isinstance(arg, dict) and len(arg) == 2:
        if 'estado' in arg and 'mina' in arg:
            if isinstance(cria_copia_parcela(arg)['estado'], str) and isinstance(cria_copia_parcela(arg)['mina'], bool) and (cria_copia_parcela(arg)['estado'] == 'limpa'
            or cria_copia_parcela(arg)['estado'] == 'marcada' or cria_copia_parcela(arg)['estado'] == 'tapada'):
                return True
    return False

def eh_parcela_tapada(p):
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'tapada':
        return True
    return False

def eh_parcela_marcada(p):
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'marcada':
        return True
    return False

def eh_parcela_limpa(p):
    if eh_parcela(p) and cria_copia_parcela(p)['estado'] == 'limpa':
        return True
    return False

def eh_parcela_minada(p):
    if eh_parcela(p) and cria_copia_parcela(p)['mina']:
        return True
    return False

def parcelas_iguais(p1, p2):
    if eh_parcela(p1) and eh_parcela(p2) and cria_copia_parcela(p1)['estado'] == cria_copia_parcela(p2)['estado'] and cria_copia_parcela(p1)['mina'] == cria_copia_parcela(p2)['mina']:
        return True
    return False

def parcela_para_str(p):
    if eh_parcela_tapada(p):
        return '#'
    if eh_parcela_marcada(p):
        return '@'
    if eh_parcela_limpa(p) and not eh_parcela_minada(p):
        return '?'
    if eh_parcela_limpa(p) and eh_parcela_minada(p):
        return 'X'
    
def alterna_bandeira(p):
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
    try:
        cria_coordenada(c,l)
    except ValueError:
        raise ValueError('cria_campo: argumentos invalidos')
    #if not eh_coordenada(cria_coordenada(c,l)):
    #    raise ValueError('cria_campo: argumentos invalidos')
    campo = {}
    for i in range(1, l+1):
        for j in range(65, ord(c)+1):
            campo[coordenada_para_str(cria_coordenada(chr(j), i))] = cria_parcela()
    return campo

def cria_copia_campo(m):
    copia_campo = {}
    for i in m:
        copia_campo[i] = m[i].copy()
    return copia_campo

def obtem_ultima_coluna(m):
    return obtem_coluna(str_para_coordenada(list(m)[-1]))

def obtem_ultima_linha(m):
    return obtem_linha(str_para_coordenada(list(m)[-1]))

def obtem_parcela(m, c):
    return m[coordenada_para_str(c)]

def obtem_coordenadas(m, s):
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
    return coordenada_para_str(c) in m

def obtem_numero_minas_vizinhas(m,c):
    viz = obtem_coordenadas_vizinhas(c)
    counter = 0
    for i in tuple(coordenada_para_str(p) for p in viz):
        if eh_coordenada_do_campo(m, str_para_coordenada(i)):
            if eh_parcela_minada(obtem_parcela(m, str_para_coordenada(i))):
                counter += 1
    return counter

def eh_campo(arg):
    if isinstance(arg, dict) and len(arg) != 0:
        for i in cria_copia_campo(arg):
            if eh_coordenada(str_para_coordenada(i)):
                if eh_parcela(cria_copia_campo(arg)[i]):
                    return True
    return False
        
def campos_iguais(m1,m2):
    if eh_campo(m1) and eh_campo(m2):
        if len(m1) == len(m2):
            for i in m1:
                if i in m2 and obtem_parcela(m1, str_para_coordenada(i)) != obtem_parcela(m2, str_para_coordenada(i)):
                    return False
            return True
    return False

def campo_para_str(m):
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
    if eh_parcela_minada(obtem_parcela(m, c)) or obtem_numero_minas_vizinhas(m, c) >= 1:
        limpa_parcela(obtem_parcela(m, c))
        return m
    limpa_parcela(obtem_parcela(m, c))
    n_analisadas = []
    if obtem_numero_minas_vizinhas(m, c) == 0:
        for i in obtem_coordenadas_vizinhas(c):
            if eh_coordenada_do_campo(m, i):
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
    if len(obtem_coordenadas(m, 'minadas')) == len(obtem_coordenadas(m, 'marcadas')) + len(obtem_coordenadas(m, 'tapadas')):
        return True
    return False

#2.2.2
def turno_jogador(m):
    action = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while not (action == 'L' or action == 'M'):
        action = input('Escolha uma ação, [L]impar ou [M]arcar:')
    coord = input('Escolha uma coordenada:')
    while not eh_coordenada_do_campo(m, str_para_coordenada(coord)):
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
    while len(coord_minas) != 3 or (int(coord_minas[1:]) < 10 and len(coord_minas[1:]) < 2) or not eh_coordenada_do_campo(m, str_para_coordenada(coord_minas)):
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
        bandeiras = len(obtem_coordenadas(m, 'marcadas'))
        print(f'   [Bandeiras {bandeiras}/{n}]')
        print(campo_para_str(m)) 
    print('VITORIA!!!')
    return True

