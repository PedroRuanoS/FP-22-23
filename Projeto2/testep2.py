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