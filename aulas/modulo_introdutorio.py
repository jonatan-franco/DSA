lista = [1,2,3,5]

print(lista.count(5))

# CRIANDO FUNCOES

def primeirafunc():
    nome = 'bob'
    print("hello "f"{nome}")
primeirafunc()


def secfunc(first_numb,second_numb):
    print("Primeiro numero: "f"{first_numb}")
    print("Segundo numero: "f"{second_numb}")
    print("Soma: "f"{first_numb+second_numb}")

secfunc(1,5)

def thirdfunc():
    for i in range(0,10):
        print('numero '+str(i))


def qfunc(arg1, *vartuple):
    # imprimindo o valor do primeiro argumento
    print("o parametro passado foi: ", arg1)
    
    # imprimindo o valor do segundo argumento
    for item in vartuple:
        print("o parametro passado foi: ", item)
    return;

qfunc(15, 'choc')
qfunc(15,16)

# funcao que multiplica

def qifunc(numb1, numb2):
    var_glob = numb1 * numb2
    print("\n",var_glob)
    
qifunc(5,2)
qifunc(6,2)

# funcao para numeros primos
import math

def numeros_primos(num):
    if (num % 2) == 0 and num > 2:
        return "este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este numero nao é primo"
    return "este numero é primo"

print(numeros_primos(1))

# funcao upper/lowercase

def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()
vari = 'casa'
print(lowercase(vari))
print(uppercase(vari))

# fazendo split

def split_palavras(text):
    return text.split(" ")

v = "esta é uma nova coleção"
print(split_palavras(v))

def split_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

print(split_letras(v))


# LAMBDA

def potencia(num):
    return num**2

def potencia(num): return num**2
print(potencia(5))

'''lambda é uma função anonima, sendo desnecessário defini-la, serve para facilitar passar os parametros'''

addnum = lambda num1, num2: num1 + num2
potencia = lambda x: x**2
subtracao = lambda x, y:  abs(x - y)
print("\nEssa é a operação de soma: ", addnum(2,5), "\n-----","\nEssa é a operação de subtração: ", subtracao(5,2))

# LIST E DICT COMPREHENSION

list = [x for x in range(11)]
print(list)

# list comprehension
list_menor = [x for x in range(11) if x<5]
print(list_menor)

# usando for
palavras = ['cachorro', 'pato', 'vaca', 'ave']
nova_palavras = []

for palavra in palavras:
    if "o" in palavra:
        nova_palavras.append(palavra)
print(nova_palavras)

#usando list comprehension
nova_palavras = [palavra for palavra in palavras if "o" in palavras]

# usando dict comprehension

    # dicionario normal
dic_alunos = {'bob': 68, 'jonas': 25}
    # dict comprehension
dic_alunos_notas = {k:v for (k,v) in dic_alunos.items()}
print(dic_alunos_notas)
    # dict comprehension de outro jeito
dic_alunos_Status = {k: 'Aprovado' if v > 50 else 'Reprovado' for (k,v) in dic_alunos_notas.items()}
print(dic_alunos_Status)
