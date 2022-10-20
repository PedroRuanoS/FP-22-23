
def limpa_text(jose):
    return ' '.join(jose.split())


cu = '''           Computers are incredibly \n\tfast, \n\t\taccurate
 \n\t\t\tand stupid. \n Human beings  \f            are incredibly slow 
inaccurate, and\v           brilliant. \n Together they are         powerful 
beyond imagination.         '''

joana = ' Fundamentos\n\tda Programacao\n'

#print(limpa_text(cu))

a = ['o', 'jose', 'mal']

a.insert(2, 'cheira')

#print(a)

a = ['cu','assado','com','mel']

#for i in a:
#    i.split()
#    i.append(' ')
#    print(i)
'''
h = resto
h.split()
resu = []
for j in h:
    j.split()
    resu.append(j)

'''
def limpa_texto(s: str) -> str:
    """Esta função recebe uma cadeia de carateres {s} qualquer e devolve
    a cadeia de carateres limpa {res} que corresponde à remoção de carateres 
    brancos.""" 
    return ' '.join(s.split())        #split: transforma uma cadeia de caracteres numa lista, ignorando caracteres vazios e os caracteres \t,\n,\v,\f,\r; join: transforma uma lista numa cadeia de caractreres, separando os elementos da lista por ' '.  


test1 = '''   Computers are incredibly \n\tfast, \n\t\taccurate
 \n\t\t\tand stupid. \n Human beings are incredibly slow 
inaccurate, and brilliant. \n Together they are powerful 
beyond imagination. '''

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
        if len(p)<i:
            res.append(p)              #append: adiciona um item à lista {res1}               
            i -= len(p) + 1                
            resto.remove(p)              #remove: remove um item da lista {res2}
        else: 
            break

    return ' '.join(res), ' '.join(resto)

#print(corta_texto('Computers are incredibly fast, accurate and stupid. Human beings are incredibly slow inaccurate, and brilliant. Together they are powerful beyond imagination.', 60))

def insere_espacos(car: str, num: int) -> str:
    n = car.split()
    i = len(n) - 1
    t = num 
    k = 1   

    for c in n:
        t -= len(c)         #{t}: caracteres vazios a adicionar para {n} ficar com a quantidade de caracteres desejada {num}                  
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



def justifica_texto(texto, numero):
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
#NOT COMPLETE

    return res   


#print(justifica_texto(test1, 60))

test1 = '''   Computers are incredibly \n\tfast, \n\t\taccurate
 \n\t\t\tand stupid. \n Human beings are incredibly slow 
inaccurate, and brilliant. \n Together they are powerful 
beyond imagination. '''

def retira_zeros_diagonal(m, c):
    list_m = list(m)
    list_c = list(c)
    
    for i in range(len(m)):
        if list_m[i][i] == 0:
            for j in range(len(m)):
                if list_m[i][j] != 0 and list_m[j][i] != 0 and i != j:
                    list_m[i], list_m[j] = list_m[j], list_m[i]
                    list_c[i], list_c[j] = list_c[j], list_c[i]
                    #k = list_m[i]
                    #l = list_m[j]
                    #o = list_c[i]
                    #n = list_c[j]
                    #list_m.pop(j)
                    #list_m.insert(j, k)
                    #list_m.pop(i)
                    #list_m.insert(i, l)
                    #list_c.pop(j)
                    #list_c.insert(j, o)
                    #list_c.pop(i)
                    #list_c.insert(i, n)
                    break
        
    return (tuple(list_m), tuple(list_c)) 

a2, c2 = ((0, 1, 1), (1, 0, 0), (0, 1, 0)), (1, 2, 3)
a3 = ((1, 0, 0), (0, 1, 0), (0, 1, 1))
matrix = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0))
#print(retira_zeros_diagonal(matrix, c2))
print(retira_zeros_diagonal(a2,c2))