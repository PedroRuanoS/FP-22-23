b = {'bits': 3, 'seed': 4}

#print(b['bits'])

#c1 = cria_coordenada('B', 1)
#c2 = cria_coordenada('N', 20)
#print(coordenadas_iguais(c1, c2))
#print(coordenada_para_str(c1))
#print(string_para_coordenada('A04'))
#print(string_para_coordenada('E23'))
#c = cria_coordenada('M', 44)
#t = obtem_coordenadas_vizinhas(c1)
#print(tuple(coordenada_para_str(p) for p in t))
#c3 = cria_coordenada('Z', 99)
#g1 = cria_gerador(32, 1)
#c4 = obtem_coordenada_aleatoria(c3, g1)
#print(c4)
#print(coordenada_para_str(c4))

#p1 = cria_parcela()
#p2 = cria_copia_parcela(p1)
#print(parcela_para_str(p1))
#print(parcela_para_str(limpa_parcela(p1))) 
#print(parcelas_iguais(p1, p2))
#print(parcela_para_str(esconde_mina(p2)))
#print(alterna_bandeira(p2))
#print(parcela_para_str(p2))
#print(alterna_bandeira(p1))
#print(eh_parcela_minada(p2))

#m = cria_campo('E',5)
#for l in 'ABC':esconde_mina(obtem_parcela(m, cria_coordenada(l,1)))
#for l in 'BC':esconde_mina(obtem_parcela(m, cria_coordenada(l,2)))
#for l in 'DE':limpa_parcela(obtem_parcela(m, cria_coordenada(l,1)))
#for l in 'AD':limpa_parcela(obtem_parcela(m, cria_coordenada(l,2)))
#for l in 'ABCDE':limpa_parcela(obtem_parcela(m, cria_coordenada(l,3)))
#alterna_bandeira(obtem_parcela(m, cria_coordenada('D',4)))
#print(campo_para_str(m))

cu = {'c': 123, 'c1': 123}

del cu['c'], cu['c1']

#print(cu)


#m = cria_campo('E',5)
#g = cria_gerador(32, 1)
#c = cria_coordenada('D', 4)
#m1 = coloca_minas(m, c, g, 2)
#print(tuple(coordenada_para_str(p) for p in obtem_coordenadas(m1, 'minadas')))

def obtem_numero_limpas_vizinhas(m, j):
    pass

#def limpa_campo(m, c):
#    copia_m = cria_copia_campo(m)
#    if not eh_parcela_minada(obtem_parcela(m,c)):
#        limpa_parcela(obtem_parcela(m, c))
#        while not campos_iguais(copia_m, m):
#            copia_m = cria_copia_campo(m)
#            for j in m:
#                if obtem_numero_minas_vizinhas(m, string_para_coordenada(j)) == 0 and obtem_numero_limpas_vizinhas(m, string_para_coordenada(j)) < len(obtem_coordenadas_vizinhas(string_para_coordenada(j))):
#                    for i in obtem_coordenadas_vizinhas(string_para_coordenada(j)):
#                        if eh_coordenada_do_campo(m, i):
#                            limpa_parcela(obtem_parcela(m, i))
#    else:
#        return m

#lista_v = [1,2,3]
#lista_c = lista_v.copy()
#lista_v.remove(1)
#print(lista_c)

#m = cria_campo('Z', 10)
#g = cria_gerador(32, 2)
#c = cria_coordenada('M', 5)
#m = coloca_minas(m, c, g, 16)
#limpa_campo(m, c)
#print(campo_para_str(m))

#m = cria_campo('E',5)
#g = cria_gerador(32, 1)
#c = cria_coordenada('D', 4)
#m = coloca_minas(m, c, g, 2)
#print(campo_para_str(limpa_campo(m, c)))

#m = cria_campo('F',6)
#print(jogo_ganho(m))
#g = cria_gerador(32, 2)
#c = cria_coordenada('D', 4)
#m = coloca_minas(m, c, g, 1)
#print(campo_para_str(limpa_campo(m, c)))
#print(jogo_ganho(m))

#m = cria_campo('M',5)
#g = cria_gerador(32, 2)
#c = cria_coordenada('G', 3)
#m = coloca_minas(m, c, g, 5)
#print(turno_jogador(m))

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
    if not isinstance(col, str) or not isinstance(lin, int) or len(col) != 1 or not 65 <= ord(col) <= 90 or not 1 <= lin <= 99:
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
    if not eh_coordenada(cria_coordenada(c,l)):
        raise ValueError('cria_campo: argumentos invalidos')
    campo = {}
    for i in range(1, l+1):
        for j in range (65, ord(c)+1):
            campo[coordenada_para_str(cria_coordenada(chr(j), i))] = cria_parcela()
    return campo

def cria_copia_campo(m):
    copia_campo = {}
    for i in m:
        copia_campo[i] = m[i]
    return copia_campo


def obtem_ultima_coluna(m):
    return obtem_coluna(str_para_coordenada(list(m)[-1]))

def obtem_ultima_linha(m):
    return obtem_linha(str_para_coordenada(list(m)[-1]))

def obtem_parcela(m, c):
    return m[coordenada_para_str(c)]

def obtem_coordenadas(m, s):
    res = []
    for i in m:
        if m[i]['estado'] == s[:-1]:
            res.append(str_para_coordenada(i))
        elif s == 'minadas' and m[i]['mina']:
            res.append(str_para_coordenada(i))
    return tuple(res)

def eh_coordenada_do_campo(m,c):
    return coordenada_para_str(c) in m

def obtem_numero_minas_vizinhas(m,c):
    viz = obtem_coordenadas_vizinhas(c)
    counter = 0
    for i in tuple(coordenada_para_str(p) for p in viz):
        if eh_coordenada_do_campo(m, str_para_coordenada(i)):
            if  m[i]['mina']:
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
        for i in m1:
            if i in m2 and obtem_parcela(m1, str_para_coordenada(i)) == obtem_parcela(m2, str_para_coordenada(i)):
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
    tup = ()
    for g in m:
        if eh_parcela_minada(obtem_parcela(m, str_para_coordenada(g))):
            tup += (g,)
    return tup

#print(coloca_minas(cria_campo('R', 14), cria_coordenada('A', 1), cria_gerador(64, 555), 40))

#print(turno_jogador(coloca_minas(cria_campo('R',7),cria_coordenada('G',4),cria_gerador(64,9),5)))
def colhao(n):
    try:
        int(n)
    except ValueError:
        return False

#print(colhao('a'))

print(abs(64- ord('C')))

#try:
    #    cria_gerador(d, s)
    #    cria_campo(c, l)
    #except ValueError: 
    #    raise ValueError('minas: argumentos invalidos') #se não for possível criar um gerador ou um campo com os dados recebidos

#minas('M', 5, 5, 64, 80)
#minas('N', 6, 6, 32, 100)
#minas('B', 3, 5, 64, 80)
#minas('E', 5, 100, 32, 100)
#minas('B', 2, 1, 32, 100)

def numero_minas_campo(m, c):
    '''numero_minas_campo: campo x coordenada -> int
    Esta função recebe um campo m e uma coordenada c e devolve um inteiro que corresponde à 
    quantidade de parcelas onde se pode esconder uma mina no campo - função auxiliar à função
    minas'''
    counter = 1
    for i in obtem_coordenadas_vizinhas(c):
        if eh_coordenada_do_campo(m, i):
            counter += 1
    return len(m) - counter

minas('M', 5, 5, 64, 80)
#len(coord_minas) != 3 or str_para_int_aux(coord_minas[1:]) or (int(coord_minas[1:]) < 10 and len(coord_minas[1:]) < 2)

def str_para_int_aux(n):
    '''str_para_aux: universal -> booleano
    Esta função verifica se não é possível tornar o argumento n em inteiro (devolvendo 
    True se não for) - função auxiliar às funções turno_jogador e minas'''
    try:
        int(n)
    except ValueError:
        return True