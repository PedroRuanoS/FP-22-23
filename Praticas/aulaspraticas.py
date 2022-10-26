'''
#                                                                                   CAPíTULO 2

#16

num = eval(input('Escreva um inteiro\n_> '))
res = num

while num != 0:
    digito = num % 10
    res = res*10 + digito 
    num = num//10 

print(res)

#17

notas = eval(input('Insira as notas, separadas por virgulas: '))

total = 0 
pos = 0

for nota in notas:
    total = total + 1 
    if nota >= 10:
        pos = pos + 1 

per = (pos/total*100)

print(pos, 'alunos tiveram nota positiva, ou seja,', per, '% dos alunos tiveram positiva')


#18

num = int(input('Escreva um inteiro: '))
zeros = 0

while num != 0:
    digito = num%10
    num = num//10
    if digito == 0 and num%10 == 0:
        zeros += 1
    
print('O numero tem', zeros, 'zeros seguidos') 
   

#19

din = eval(input('Insira uma quantidade de dinheiro: ')) * 100//1

for notas in [5000,2000,1000,500,200,100,50,20,10,5,2,1]:
    print(din//notas, 'notas de', notas/100)
    din = din%notas

#20

x=1 
num = 0

while x<=9:
    num = num*10 + x
    print(num, 'x 8 +', x, '=', num*8+x)
    x += 1


#12


x = eval(input("valor de x: "))
n = eval(input("valor de n: "))
i = 1
res = 1
termo = 1

while n!=0:
    termo = termo * (x / i)
    res += termo
    i += 1
    n -= 1

print('O valor da soma é', res)
   

#10 

num = int(input(''))
res = 0 
digito = 0
e = 0
while num != 0:
    digito = num%10
    if digito%2!=0:
        res = res + digito*(10**e)
        e += 1
    num = num//10

print(res)

#11

num = int(input(''))
res = 0 
digito = 0

while num != 0:
    digito = num%10
    res = res*10 + digito
    num = num//10

print(res)
#etc.

#14

num = int(input(''))
res = 0 
digito = 0

while num != 0:
    digito = num%10
    res = res + digito
    num = num//10

print (res)


#9

digito = eval(input('Escreva um dígito (-1 para terminar): '))
res=0

while digito > 0:
    res = res*10 + digito
    digito = eval(input('Escreva um dígito (-1 para terminar): '))

print('O número é:', res)

#8

seg = int(input('Segundos (negativo para terminar): '))

while seg > 0:
    dia = seg/(3600*24)
    print('O número de dias correspondente é', dia)
    seg = int(input('Segundos (negativo para terminar): '))

#7

#6

#5

#4

#REVER HOJE OS OUTROS PARA CIMA PARA NAO ESQUECER, SEGUNDA FAZER OUTRA VEZ

#EXERCICIO TESTE 1º TURNO (1)

num = int(input('Número inteiro: '))
res = 0
while num != 0:
    digito = num%10
    if digito%2 == 0:
        res += (digito**2)
    num //= 10
print(res)


#EXERCICIO TESTE 1º TURNO (2)
def eh_primo(x):
    if x==2 or x==3:
        return True
    if x%2==0 or x<2:
        return False
    for n in range(3,int(x**0.5)+1,2):   
        if x%n==0:
            return False   
    return True

num = int(input('Número inteiro: '))
primo = 0 

while num != 0:
    while eh_primo(primo) == False:
        primo += 1
    if eh_primo(primo + 2) == True:
        print(primo,primo + 2)
        num -= 1
        primo += 1
    else:
        primo += 1

#18

num = int(input('Escreva um inteiro? '))
counter = 0

while num != 0:
    digito = num%10
    num //= 10
    if digito == 0 and num%10 == 0:
        counter += 1

print('O numero tem', counter, 'zeros seguidos')

#17
num = int(input('Quantos alunos existem? '))
total = 0
pos = 0

while num != 0:
    nota = int(input('Nota: '))
    total += 1
    if nota>=10:
        pos += 1
    num -= 1

print(pos, 'alunos tiveram nota positiva, ou seja,', (pos/total)*100, '%.')

#16

num = int(input('Escreva um número inteiro: '))
res = num

while num != 0:
    digito = num%10
    res = res*10 + digito
    num //= 10

print(res)

#15

digito = int(input('Escreva um algorismo (-1 para terminar): '))
num = 0

while digito > 0:
    num = num*10 + digito
    digito = int(input('Escreva um algorismo (-1 para terminar): '))

print(num)

#14 e 9

num = int(input('Escreva um inteiro: '))
res = 0

while num != 0:
    digito = num%10
    res += digito
    num //= 10

print(res)

#13

num = int(input('Número: '))
digi = 1

while digi < 11:
    print(num, 'x', digi, '=', num*digi)
    digi += 1

#12

x = int(input(''))
n = int(input(''))
termo = 1
i = 1
a = 1

while i<=n:
    termo *= (x/i)
    a += termo
    i += 1

print(a)

#11

num = int(input('Escreva um inteiro: '))
res = 0
while num!=0:
   digito = num%10
   res = res*10 + digito
   num //= 10

print(res) 

#10

num = int(input('Escreva um inteiro: '))
res = 0
i = 0

while num!=0:
    digito = num%10
    if digito%2!=0:
        res = res + digito*(10**i)
        i += 1
    num //= 10

print(res)
'''

#                                                                 CAPÍTULO 3


#1 



def cinco(arg):
    return arg == 5
#print(cinco(4))
#print(cinco(5))


#2

def horas_dias(horas):
    return horas/24
#print(horas_dias(123))

#3

def area_circulo(raio):
    return (raio**2)*3.14
#print(area_circulo(3))

#4

def area_coroa(r1,r2):
    if r1>r2: 
        raise ValueError('r1 maior que r2')
    else:
        return area_circulo(r2)-area_circulo(r1)
#print(area_coroa(4,5))
#print(area_coroa(5,4))

#5

#def bissexto(num):
#    return (num%4 == 0 and num%100 != 0) or (num%400 == 0)

#print(bissexto(1984))
#print(bissexto(1985))
#print(bissexto(2000))

#6

def dias_mes(ini, ano):
    if ini == 'jan' or ini == 'mar' or ini == 'mai' or ini == 'jul' or ini == 'ago' or ini == 'out' or ini == 'dez':
        return 31
    elif ini == 'abr' or ini == 'jun' or ini == 'set' or ini == 'nov':
        return 30
    elif ini == 'fev' and bissexto(ano):
        return 29
    elif ini == 'fev' and not bissexto(ano):
        return 28
    else:  
        raise ValueError('Mês não existe')

#print(dias_mes('fev',2000))

#7 
 
#   a) 

def valor(q,j,n):
    if j>1 or j<0 or not isinstance(q, (int,float)) or not isinstance(j, (int,float)) or not isinstance(n, (int,float)):
        raise ValueError('Caracter não válido')
    else:
        return q*((1 + j)**n)

#print(valor(100,0.03,4))

#   b) 

def duplicar(h,i):
    m = 1
    while valor(h,i,m) < 2*h:
        m += 1
    return m

#print(duplicar(100, 0.03))

#8


def serie_geom(r,n):
    if  not isinstance(r, (int)) or not isinstance(n, (int)) or n<0:
        raise ValueError('serie_geom: argumento incorrecto')
    i = 0
    soma = 0
    while i <= n:
        soma += r**i
        i += 1
    return soma

#print(serie_geom(2,4))

#9

def dia_da_semana(dia, mes, ano):
    if mes < 3:
        m = mes + 12
        ano -= 1
    else: 
        m = mes
    k = ano%100
    j = ano//100
    q = dia
    h = (q +13*(m+1)//5 + k + k//4 + j//4 - 2*j)%7
    t = ('Sábado', 'Domingo', 'Segunda', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira')

    return t[h]

#print(dia_da_semana(18, 1, 2014))

#10

def misterio(n):
    ni = inverte(n)
    ns = abs(n-ni)
    nsi = inverte(ns)
    if ns + nsi != 1089:
        return 'Condições não verificadas'
    else:
        return ns + nsi

def inverte(y):
    res = 0
    while y>0:
        dig = y%10
        res = res*10 + dig
        y //= 10
    return res     

#print(misterio(131))

#                                                                             CAPÍTULO 4

'''
#1

soma = 0
for i in range(20,0,-2):
    soma += 1

print(soma)

'''
#2

def explode(num):
    if  not isinstance(num, int):
        raise ValueError('explode: argumento não inteiro')
    elif num < 0:
        raise ValueError('explode: argumento inteiro não positivo')
    else:
        res_tuplo = ()
        while num > 0:
            digito = num%10
            res_tuplo = (digito,) + res_tuplo
            num //= 10
    return res_tuplo

#print(explode(34500))

#3

def implode(t):
    if not isinstance(t, tuple):
        raise ValueError('implode: argumento não é um tuplo')
    res = 0
    for i in t:
        if not isinstance(i, int):
            raise ValueError('implode: elemento não inteiro')
        if i >= 10 or i < 0:
            raise ValueError('implode: elemento não é um algarismo')
        res = res*10 + i

    return res

#print(implode((3,4,0,0,4)))

#4

def filtra_pares(num):
    if not isinstance(t, tuple):
        raise ValueError('filtra_pares: argumento não é um tuplo')
    res = ()
    for i in num:
        if not isinstance(i, int):
            raise ValueError('filtra_pares: elemento não inteiro')
        if i >= 10 or i < 0:
            raise ValueError('filtra_pares: elemento não é um algarismo')
        if i % 2 == 0:
            res += (i,)
            
    return res

#print(filtra_pares((2,5,6,7,9,1,8,8)))

#5

def algarismos_pares(num):
    return implode(filtra_pares(explode(num)))

#print(algarismos_pares(6643399766641))

#6

def num_para_seq_cid(num):
    if type(num) != int:
        raise ValueError('num_para_seq_cid: argumento não inteiro')
    if num < 0:
        raise ValueError('num_para_seq_cid: argumento inferior a 0')
    res = ()
    while num > 0:
        digito = num%10
        if digito%2 == 0:
            digito += 2
            if digito == 10:
                digito = 0
        else: 
            digito -= 2
            if digito == -1:
                digito = 9
        res = (digito,) + res
        num //= 10
    return res

#print(num_para_seq_cid(1234567890))

#7

def amigas(x,y):
    pass

#8
def junta_ordenados(x,y):
    xi = 0
    yi = 0
    res = ()
    while xi < len(x) or yi < len(y):
        if xi == len(x):
            res += (y[yi],)
            yi += 1
        elif xi == len(y):
            res += (x[xi],)
            xi += 1
        elif x[xi] > y[yi]:
            res += (y[yi],)
            yi += 1
        elif x[xi] <= y[yi]:
            res += (x[xi],)
            xi += 1
    return res

#print(junta_ordenados((2, 34, 200, 210),(1, 23)))

#9

def reconhece(frase):
    for i in range(len(frase)):
        if i > 0:
            if frase[i-1] in '1234' and frase[i] in 'ABCD':
                return False
        elif frase[i] != 'A' and frase[i] != 'B' and frase[i] != 'C' and frase[i] != 'D' and frase[i] != '1' and frase[i] != '2' and frase[i] != '3' and frase[i] != '4':  
            return False
    return True

#print(reconhece('A1'))
#print(reconhece('ABBBBCDDDD23311'))
#print(reconhece('ABC12C'))

#10
#a)

def codifica(cad):
    res = ''
    res2 = ''
    for i in range(len(cad)):
        if i%2 != 0:
            res += cad[i]
        if i%2 == 0:
            res2 += cad[i]
    return res2 + res

#print(codifica('abcde'))

#b)

def descodifica(cad):
    if len(cad)%2 == 0:
        mei = int(len(cad)/2)
    else:
        mei = int((len(cad)+1)/2)
    res = ''
    for i in range(mei):
        res += cad[i]
        if (i+mei)<len(cad):
            res += cad[i+mei]                  
    return res

#print(descodifica('acebd'))

#6











#                           TESTE TICHA 

#3. (Já podes usar Tuplos) defense uma função que recebe um tuplo, com números inteiros ou floats e pelo menos dois números, e que entre cada par de números escreve os sinais <, > ou =.
#Ex: t = (1, 3, 2, 2, 9)
#(1, <, 3, >, 2, =, 2, <, 9)

def comparacao(x):
    if len(x) < 2:
        raise ValueError('erro')
    for i in x:
        if not isinstance(i, (int, float)):
            raise ValueError('erro')
    i = 0
    res = ()
    while i < len(x):
        if i == 0:
            pass
        elif x[i-1]>x[i]:
            res += ('>',)
        elif x[i-1]<x[i]:
            res += ('<',)           
        else:
            res += ('=',)
        res += (x[i],)
        i += 1
    return res   

#print(comparacao((1,3,2,2,9)))

#2. Definir uma função que recebe um número e um dígito e que devolve o número escrito mas só com os algarismos q são múltiplos do digito. (Só podes usar matéria do capítulo das funções)
#Ex: 234567 e 8
#24

def divisor(x,y):
    res = 0
    i = 0
    while x>0:
        digito = x%10
        if y%digito == 0:
            res = res + digito*10**i
            i += 1
        x //= 10
    return res

#print(divisor(23456,8))

#                                                               FICHA LISTAS

#1

#def lista_codigos(stri):
    res = []
    for i in stri:
        res += [ord(i)]
    return res

#print(lista_codigos('bom dia'))

#2

#def remove_multiplos(lst, inte):
    res = []
    for i in lst:
        if i%inte != 0:
            res += [i]
    return res

#print(remove_multiplos([2,3,5,9,12,33,34,45], 3)) 

#3

#def soma_cumulativa(lst):
    for i in range(1,len(lst)):
        lst[i] += lst[i-1]
    return lst

#print(soma_cumulativa([1,2,3,4,5]))

#4

#def elemento_matriz(mat, lin, col):
    if type(mat) != list:
        raise ValueError('não é lista')
    for i in mat:
        if type(i) != list:
            raise ValueError('não é lista')
    if lin > (len(mat) - 1):
        raise ValueError('indice invalido, linha', lin)
    if col > (len(mat[lin]) - 1):
        raise ValueError('indice invalido, linha', lin) 
    return mat[lin][col]

#m= [[1,2,3],[4,5,6]]
#print(elemento_matriz(m,0,0))

#5

#def rep_matriz(mat):
    for i in mat:
        for j in i:
            res = ''
            res += j + '\t'
        print(res)

#6

#def soma_matrizes(mat1,mat2):
    if len(mat1) != len(mat2):
        raise ValueError("matrices not the same size")
    for rowI in range(len(mat1)):
        if len(mat1[rowI]) != len(mat2[rowI]):
            raise ValueError("matrices not the same size")
    res2 = ''
    for i in range(len(mat1)):
        res = ''
        for j in range(len(mat1[i])):
            res = res + str(mat1[i][j] + mat2[i][j]) + '  '
        res2 += res + '\n'
    return res2

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
#print(soma_matrizes(m1,m2))

def multiplica_mat(mat1,mat2):
    res = ''
    for i in range(mat1):
        for j in range(mat2):
            pass

#1

def lista_codigos(cad):
    res = [] 
    for i in cad:
        res += [ord(i)]
    return res

#print(lista_codigos('bom dia'))

#2

def remove_multiplos(list, num):
    res = []
    for i in list:
        if i%num != 0:
            res += [i]
    return res        

#print(remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3))

#3

def soma_comulativa(list):
    res = []
    soma = 0
    for i in list:
        soma += i
        res += [soma]
    return res

#print(soma_comulativa([1,2,3,4,5]))~

#4

def elemento_matriz(mat, ind1, ind2):
    if type(mat) != list:
        raise ValueError('não é lista')
    for i in mat:
        if type(i) != list:
            raise ValueError('não é lista')
    if ind1 > (len(mat)-1):  
        raise ValueError('indice invalido: linha', ind1)
    if ind2 > (len(mat[ind1])-1):
        raise ValueError('indice invalido: coluna', ind2)
    return mat[ind1][ind2]

#print(elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 0))
#print(elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 3))

#5

def escreve_matriz(mat):
    res2 = ''
    for i in mat:
        res = ''
        for j in i:
            res += str(j) + '  '
        res2 += res + '\n'
    return res2

#print(escreve_matriz([[1,2,3],[3,2,1],[4,5,3]]))    

#6

def soma_mat(mat1,mat2):
    res2 = ''
    for i in range(len(mat1)):
        res = ''
        for j in range(len(mat1[i])):
            res += str(mat1[i][j]+ mat2[i][j]) + '  '
        res2 += res + '\n'
    return res2        

#m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(soma_mat(m1,m2))

#7

def multiplicar_mat(mat1,mat2):
    res = []
    for i in range(len(mat2[0])):
        linha = []
        for j in range(len(mat1)):
            mult = 0
            for k in range(len(mat2)):
                mult += (mat1[i][k]*mat2[k][j])
            linha += [mult]
        res += [linha]
    res += []
    
    return res  

#m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(multiplicar_mat(m1,m2))

#8

def seq_racaman(num):
    res = []
    for n in range(num):
        if n == 0:
            res += [0]
        elif res[n-1] > n and res[n-1] - n not in res:
            res += [res[n-1] - n]
        else:
            res += [res[n-1] + n]
    return res

#print(seq_racaman(15))

#9

def num_occ_lista(lista, num):
    counter = 0
    coudjom = lista
    for i in coudjom:
        if num == i:
            counter += 1
        if type(i) == list:
            for j in i:
                coudjom += [j]
    return counter

#print(num_occ_lista([1, 2, 3, 4, 3], 3))
#print(num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2))

#10

from random import *

def euromilhoes():
    res = []
    for i in range(5):
        res += [int((random()*50)) + 1]
    for i in range(2):
        res += [int((random()*12)) + 1]
    return res

#print(euromilhoes()) 

#           TESTE TICHA

def texto(text, letter):
    res1 = ''
    res2 = ''
    for i in text:
        if i not in letter:
            res1 += i
        else:
            res2 += i
    return res2 + res1

# CAPITULO 6

#1

#a: 2º dicionário
#b: dentro 2º dicionário, é o dicionario associado à chave 'nome'
#c: 'Doe'
#d: 'D'

#2

def agrupa_por_chave(lst1):
    res = {}
    for i in lst1:
        chave = i[0]
        valor = i[1]
        if chave in res:
            res[chave].append(valor)
        else:
            res[chave] = [valor]
    return res

#3
#a

def baralho():
    res = []
    naipes = ('esp','copas','ouros','paus')
    valores = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    for np in naipes:
        for vlr in valores:
            carta = {}
            carta['np'] = np 
            carta['vlr'] = vlr
            res.append(carta)
    return res

#print(baralho())
#b

def baralha():
    pass

# CAPITULO 7

#1

#a

#{'numerador': n, 'denominador': d}

#b

def cria_rac(n,d):
    if type(n) == int and type(d) == int:
        if d > 0:
            return {'numerador': n, 'denominador': d}
    raise ValueError('')

def num(r):
    return r['numerador']

def den(r):
    return r['denominador']

def eh_racional(arg):
    if type(arg) == dict:
        if len(arg) == 2:
            if('numerador' in arg and 'denominador' in arg):
                if type(arg['numerador']) == int and type(arg['denominador']) == int:
                    if arg['denominador'] > 0:
                        return True
    return False

def eh_rac_zero(r):
    return r['numerador'] == 0

def rac_iguais(r1, r2):
    return r1['numerador'] * r2['denominador'] == r2['numerador'] * r1['denominador']

#c

def escreve_rac(r):
    print(str(r['numerador']) + '/' + str(r['denominador']))

#d

def produto_rac(r1, r2):
        return cria_rac(num(r1)*num(r2), den(r1)*den(r2))
            
#3

#a

#{'dia': d, 'mes': m, 'ano': a}

#b
'''
def cria_data(d,m,a):
    if type(d) == int and type(m) == int and type(a) == int:
        if d > 0 and m > 0:
            if 12 >= m >= 0:
                if dias_de(m,a) >= d >= 1:
                    return True
    raise ValueError('')

def dias_de(m,a):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2 and bissexto(a):
        return 29
    elif m == 2 and not bissexto(a):
        return 28

def bissexto(a):
    return a%4 == 0 and a%100 != 0  or a%400 == 0

def dia(dt):
    return dt['dia']

def mes(dt):
    return dt['mes']

def ano(dt):
    return dt['ano']

def eh_data(arg):
    if type(arg) == dict:
        if len(arg) == 3:
            if 'dia' in arg and 'mes' in arg and 'ano' in arg:
                if type(arg['dia']) == int and type(arg['mes']) == int and type(arg['ano']) == int:
                    if  12 >= arg['mes'] >= 1:
                        if dias_de(arg['mes'],arg['ano']) >= arg['dias'] >= 1:
                            return True
    return False

def mesma_data(d1, d2):
    return d1['dia'] == d2['dia'] and d1['mes'] == d2['mes'] and d1['ano'] == d2['ano']
    
'''

#3

#a {'dia': d, 'mês': m, 'ano': a}

#b

def cria_data(d,m,a):
    return {'dia': d, 'mes': m, 'ano': a}

def dia(dt):
    return dt['dia']

def mes(dt):
    return dt['mes']

def ano(dt):
    return dt['ano']

def bissexto(a):
    return a%4 == 0 and (a%100 != 0 or a%400 == 0)
        
def dias_do_mes(m,a):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if m in [4,6,9,11]:
        return 30
    if m in 2:
        if bissexto(a):
            return 29
        else:
            return 28

def eh_data(arg):
    if type(arg) == dict:
        if len(arg) == 3:
            if 'dia' in arg and 'mes' in arg and 'ano' in arg:
                if type(arg['dia']) == int and type(arg['mes']) == int and type(arg['ano']) == int:
                    if  12 >= arg['mes'] >= 1 and dias_de(arg['mes'], arg['ano']) >= arg['dia']:
                        return True

def mesma_data(d1,d2):
    return d1['dia'] == d2['dia'] and d1['mes'] == d2['mes'] and d1['ano'] == d2['ano']

def escreve_data(data):
    if data['dia'] < 10:
        data['dia'] = '0' + str(data['dia'])
    if data['ano'] < 0:
        data['ano'] = str(abs(data['ano'])) + ' ' + 'AC'
    return str(data['dia']) + '/' + str(data['mes']) + '/' + str(data['ano'])

#print(escreve_data(cria_data(5, 9, 2018)))
#print(escreve_data (cria_data (5, 9, -10)))

def data_anterior(d1,d2):
    return ano(d1) < ano(d2) or ano(d1) == ano(d2) and mes(d1) < mes(d2) or ano(d1) == ano(d2) and mes(d1) == mes(d2) and dia(d1) < dia(d2)  

def idade(d1,d2):
    if ano(d1) > ano(d2):
        raise ValueError('idade: a pessoa ainda não nasceu')
    idade = ano(d2) - ano(d1)
    if mes(d1) < mes(d2) or (mes(d1) == mes(d2) and dia(d1) < dia(d2)):
        idade += 1
    return idade

#2

#a {w}

# CU

def resumo_FP(notas):
    negativas = 0
    total = 0
    soma = 0
    for nota in notas:
        if nota < 10:
            negativas += len(notas[nota])
        else:
            soma += nota*len(notas[nota])
            total += len(notas[nota])
    return soma/total, negativas

#print(resumo_FP({1 : [46592, 49212, 90300, 59312], 15 : [52592, 59212], 20 : [58323]}))

def mais_antigo(bib):
    antigo = bib[0]['ano']
    livro_antigo = bib[0]['titulo']
    for livro in bib:
        if livro['ano'] < antigo:
            antigo = livro['ano']
            livro_antigo = livro['titulo']
    return livro_antigo

#print(mais_antigo([{'autores': ['G. Arroz', 'J. Monteiro', 'A. Oliveira'],
'titulo': 'Arquitectura de computadores', 'editor': 'IST Press',
'cidade': 'Lisboa', 'ano': 2007, 'numpags': 799,
'isbn': '978-972-8469-54-2'}, {'autores': ['J.P. Martins'],
'titulo': 'Logica e Raciocinio', 'editor': 'College Publications',
'cidade': 'Londres', 'ano': 2014, 'numpags': 438,
'isbn': '978-1-84890-125-4'}]))
    