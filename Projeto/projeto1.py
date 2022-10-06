
def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} qualquer e devolve
    a cadeia de carateres limpa que corresponde à remoção de carateres 
    brancos.""" 
    res = ''

    for c in s:
        if c in '\n,\t,\v,\f,\r':       #Caracteres removidos: \n, \t, \v, \f, \r.
            res += ' '
        else: 
            res += c

    return ' '.join(res.split())        #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  


test1 = '''   Computers are incredibly \n\tfast, \n\t\taccurate
 \n\t\t\tand stupid. \n Human beings are incredibly slow 
inaccurate, and brilliant. \n Together they are powerful 
beyond imagination. '''

#print(limpa_texto(test))

def corta_texto(st: str, i: int) -> str:
    """"""
    n = st.split()
    res1 = [] 
    res2 = n

    for p in n:
        if len(p)<i:
            res1.append(p)
            i -= len(p)
            res2.remove(p)
        else: 
            break
    
    return ' '.join(res1), ' '.join(res2)

print(corta_texto(limpa_texto(test1), 100))



