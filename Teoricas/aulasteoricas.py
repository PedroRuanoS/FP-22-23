'''
#Aula 11

notas = (15,6,10,12,17)

print(notas[0])

v = (12,10,(15,11,14),18,17)

print(v[2][1])

#v[0] = 11 NÃO DÁ, PQ TUPLO NÃO PODE SER ALTERADO

a = (2,1,3,7,5)

print(a[2:4])
print(a[:3])
print(a[4:])
print(a[:])
print(a[1:8:2])


def substitui(t,p,e):
    return t[:p] + (e,) + t[p+1:]

a = [2,1,3,7,5]
b = substitui(1, 2, 3)
print (a,b)


def soma_elementos(t):
    if type(t) != tuple: 
        raise ValueError('Não é tuplo')
    res = ()
    i = 0
    tamanho = len(t)
    while i< len(t):
        if not isinstance(t[i], (int, float)):
            raise ValueError('Não é número')
        res += (t[i]**2,)
        i += 1
    return res

print(soma_elementos((1,2,3)))

#Aula 12

t = (1, 'a', 3, 4, 6)

for elemento in t:
    print (elemento)

t = (1, 'a', 3, 4, 6)

for elemento in t:
    if elemento == 3:
        break
    print (elemento)

def soma_elementos_for(t):
    soma = 0
    for val in t:
        soma += val
    return soma

tuplo = (1,2,3,7)
print(soma_elementos_for(tuplo))

def soma_elementos_for_range(t):
    soma = 0
    for i in range(len(t)):
        soma += t[i]
    return soma

print(soma_elementos_for_range((2,4,5,6)))

def soma_elementos_for_range(v1,v2):
    res = ()
    for i  in range(len(v1)):
        res += (v1[i]+v2[i],)
    return res

print(soma_elementos_for_range((2,4),(3,6)))
'''

def tabelas():
    for x in range(1,11):
        for y in range(1,11):
            print(x, 'x', )


def simbolos_comum(s1,s2):
    res = ''
    i = 0
    while i < len(s1):
        if s1[i] in s2 and s1[i] not in res:
            res += s1[i]
        i += 1
    return res 

#print(simbolos_comum('olaa', 'adeus'))

def simbolos_comum_for(s1,s2):
    res = ''
    for c in s1:
        if c in s2 and c not in res:
            res += c
    return res

#print(simbolos_comum_for('olaa','adeus'))





















































































































