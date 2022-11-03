def cria_gerador(b, s):
    if (b != 32 and b != 64) or not isinstance(s, int) or s < 0 or s > b:
        raise ValueError('cria_gerador: argumentos invalidos')
    return {'bits': b, 'seed': s}

def copia_gerador(g):
    return g

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
            if copia_gerador(arg)['bits'] == 32 or copia_gerador(arg)['bits'] == 64 and isinstance(obtem_estado(arg), int) and copia_gerador(arg)['bits'] > obtem_estado(arg) >= 0:
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

#g1 = cria_gerador(32, 1)
#[atualiza_estado(g1) for n in range(3)]
#print(gera_numero_aleatorio(g1, 25))
#g2 = cria_gerador(64, 1)
#[atualiza_estado(g2) for n in range(5)]
#print(gera_carater_aleatorio(g2, 'Z'))
