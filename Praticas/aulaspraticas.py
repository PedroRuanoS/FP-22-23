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

def bissexto(num):
    return (num%4 == 0 and num%100 != 0) or (num%400 == 0)

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

def lista_codigos(stri):
    res = []
    for i in stri:
        res += [ord(i)]
    return res

#print(lista_codigos('bom dia'))

#2

def remove_multiplos(lst, inte):
    res = []
    for i in lst:
        if i%inte != 0:
            res += [i]
    return res

#print(remove_multiplos([2,3,5,9,12,33,34,45], 3)) 

#3

def soma_cumulativa(lst):
    for i in range(1,len(lst)):
        lst[i] += lst[i-1]
    return lst

#print(soma_cumulativa([1,2,3,4,5]))

#4

def elemento_matriz(mat, lin, col):
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

def rep_matriz(mat):
    for i in mat:
        for j in i:
            res = ''
            res += j + '\t'
        print(res)

#6

def soma_matrizes(mat1,mat2):
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

             
