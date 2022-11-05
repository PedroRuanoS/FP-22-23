#TAD gerador
def cria_gerador(b, s):
    if (b != 32 and b != 64) or not isinstance(s, int) or s < 0 or s > b:
        raise ValueError('cria_gerador: argumentos invalidos')
    return {'bits': b, 'seed': s}

def copia_gerador(g):
    return g.copy()

def obtem_estado(g):
    return g['seed']

def define_estado(g,s):
    g['seed'] = s
    return s

def atualiza_estado(g):
    s = obtem_estado(g)
    if copia_gerador(g)['bits'] == 32:
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
        define_estado(g,s)
    if copia_gerador(g)['bits'] == 64:
        s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
        s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
        s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
        define_estado(g,s)
    return obtem_estado(g)

def eh_gerador(arg):
    if isinstance(arg, dict) and len(arg) == 2:
        if 'bits' in arg and 'seed' in arg:
            if (copia_gerador(arg)['bits'] == 32 or copia_gerador(arg)['bits'] == 64) and isinstance(obtem_estado(arg), int) and \
                copia_gerador(arg)['bits'] > obtem_estado(arg) >= 0:
                return True
    return False

def geradores_iguais(g1, g2):
    if eh_gerador(g1) and eh_gerador(g2):
        if copia_gerador(g1)['bits'] == copia_gerador(g2)['bits'] and obtem_estado(g1) == obtem_estado(g2):
            return True
    return False

def gerador_para_str(g):
    return 'xorshift' + str(copia_gerador(g)['bits']) + '(s=' + str(obtem_estado(g)) + ')'

def gera_numero_aleatorio(g,n):
    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n)

def gera_carater_aleatorio(g,c):
    atualiza_estado(g)
    return chr(65 + (obtem_estado(g) % (ord(c) - ord('A') + 1)))

#TAD coordenada
def cria_coordenada(col, lin):
    if not isinstance(col, str) or not isinstance(lin, int) or not 65 <= ord(col) <= 90 or not 1 <= lin <= 99:
        raise ValueError('cria_coordenada: argumentos invalidos')
    return {'col': col, 'lin': lin}

def obtem_coluna(c):
    return c['col']

def obtem_linha(c):
    return c['lin']

def eh_coordenada(arg):
    if isinstance(arg, dict) and len(arg) == 2:
        if 'col' in arg and 'lin' in arg:
            if isinstance(obtem_coluna(arg), str) and isinstance(obtem_linha(arg), int) and 65 <= ord(obtem_coluna(arg)) <= 90 and 1 <= obtem_linha(arg) <= 99:
                return True
    return False

def coordenadas_iguais(c1, c2):
    if obtem_coluna(c1) == obtem_coluna(c2) and obtem_linha(c1) == obtem_linha(c2):
        return True
    return False

def coordenada_para_str(c):
    if obtem_linha(c) < 10:
        return obtem_coluna(c) + '0' + str(obtem_linha(c))
    else:
        return obtem_coluna(c) + str(obtem_linha(c))

def string_para_coordenada(s):
    if s[1] == 0:
        return {'col': s[0], 'lin': int(s[2])}
    else:
        return {'col': s[0], 'lin': int(s[1] + s[2])}

c1 = cria_coordenada('B', 1)
c2 = cria_coordenada('N', 20)
#print(coordenadas_iguais(c1, c2))
#print(coordenada_para_str(c1))
#print(string_para_coordenada('A04'))
#print(string_para_coordenada('E23'))

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
            
def obtem_coordenada_aleatoria():
    pass

c3 = cria_coordenada('M', 44)
t = obtem_coordenadas_vizinhas(c3)
#print(tuple(coordenada_para_str(p) for p in t))
