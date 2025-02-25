# introdução python hello
print('olá Luan')
first_name = 'luan'
last_name = 'tonetto'
full_name = first_name + '' + last_name
print(full_name)
message = 'Hello,' + full_name.title() + '!'
print(message)

# calculo soma 2 numeros
n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
s = n1+n2
print('a soma vale', s)
print('A soma vale ()'.format(s))

n = float(input('digite um valor'))
print(n)
n = str(input('digite um valor'))
n = bool(input('digite um valor'))

n1 = int(input('digite um valor'))
n2 = int(input('digite um valor:'))
s = n1+n2

# Soma, numero, alfabeto, verdadeiro falso
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))
a = input('digite algo')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços?', a.isspace())
print('é um numero?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('Esta em maisculo?', a.isupper())
print('Esta em minusculo?', a.islower())
print('Esta cpaitalizada?', a.istitle())

# msg prazer em conhecer
nome = input('Qual é seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

# antecessor e sucessor
n = int(input('digite um numero: '))
a = n-1
s = n+1
print('analisando o Valor {}, seu antecessor é {}, e o sucessor é {}'.format(n, a, s))
print('analisando o Valor {}, seu antecessor é {}, e o sucessor é {}'.format(
    n, (n-1), (n+1)))

# medidas
medida = float(input('Qual a distancia em metros?'))
cm = medida*100
mm = medida*1000
print('A medida de {} corresponde a{}cm e {}mm '.format(medida, cm, mm))

# tabuada
num = int(input('Qual o numero?'))
print('{}x{}={}'.format(num, 1, num*1))
print('{}x{}={}'.format(num, 2, num*2))
print('{}x{}={}'.format(num, 3, num*3))
print('{}x{}={}'.format(num, 4, num*4))
print('{}x{}={}'.format(num, 5, num*5))
print('{}x{}={}'.format(num, 6, num*6))
print('{}x{}={}'.format(num, 7, num*7))
print('{}x{}={}'.format(num, 8, num*8))
print('{}x{}={}'.format(num, 9, num*9))
print('{}x{}={}'.format(num, 10, num*10))

# calculo dinheiro conversao em dolar
real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real/3.27
print('com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))

# calculo area de parede
larg = float(input('Qual a largura da parede?'))
alt = float(input('altura da parede'))
area = larg*alt
print("sua parede tem a dimensao de {}x{} e sua area é de {}".format(larg, alt, area))
tinta = area/2
print('para pintar essa parede voce precisara de {}l de tinta'.format(tinta))

# calculo produto
preço = float(input('qual é o preço do produto?R$'))
novo = preço-(preço*5/100)
print('O produto com 5% de desconto vai custar R${}'.format(novo))

# calculo salario
salario = float(input('qual é o seu salario R$?'))
novo = salario+(salario*15/100)
print('Seu salario é R${} com 15% de aumento ele fica R${:.2f}'.format(salario, novo))

# Calculo temperatura
c = float(input('Informe a temperatura em C:'))
f = ((9*c)/5)+32
print('A temperatura de {}C corresponde a {}*F'.format(c, f))

# calculo aluguel de carro
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos KM rodados?'))
pago = (dias*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

# importando biblioteca math
num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil))
print('A raiz de {} é igual a {}'.format(num, math.floor))
num = int(input('Digite um numero'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# gerar numero aleatorio
num = random.randint(1, 100)
print(num)

# importando biblioteca do site python
print(emoji.emojize('Olá Luan :octopus:'))

#quebrando numero
#com import
import math 
from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {}e a sua porção inteira é {}'.format(num,math.trunc(num)))
#sem import
num=float(input('digite um valor:'))
print('O valor digitado foi{}sua porção inteira é{}'.format(num,int(num)))

#calculando hipotenusa (sem import)
co=float(input('Qual é o comprimento do cateto oposto:'))
ca= float(input('Qual é o comprimento do cateto adjacente:'))
soma=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(soma))
#com import
import math
co=float(input('Qual é o comprimento do cateto oposto:'))
ca= float(input('Qual é o comprimento do cateto adjacente:'))
soma=math.hypot(co,ca)
print('A hipotenusa é:{:.2f}'.format(soma))

#seno cosseno e tangente
import math
angulo = float(input('Digite o Angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de{} tem o SENO de {:.2f}'.format(angulo,seno))
print('O angulo de{} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
print('O angulo de{} tem a TANGENTE de {:.2f}'.format(angulo,tangente))

#sorteando nomes 
import random
aluno1=input('primeiro aluno? ')
aluno2=input('segundo aluno? ')
aluno3=input('terceiro aluno? ')
aluno4=input('quarto aluno? ')
alunos=[aluno1,aluno2,aluno3,aluno4]
msg=random.choice(alunos)
print('O aluno escolhido foi {}'.format(msg))

#sorteando nomes em ordem
import random
aluno1=input('primeiro aluno? ')
aluno2=input('segundo aluno? ')
aluno3=input('terceiro aluno? ')
aluno4=input('quarto aluno? ')
lista=[aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print('A ordem escolhida foi')
print(lista)
 
 #tocando mp3 
import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/Luan/Desktop/ex021.mp3') #caminho onde tem a msc
pygame.mixer.music.play()
input()
pygame.event.wait()

#fatiando frases
frase = 'curso em video python'
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[13])
print(frase[3:13:1])
print("""Uma frase muito grande """ )

#nome em maisculo e minusculo e contador
nome = str(input('Qual Seu Nome?')).strip()
print ('Analisando seu nome...')
print ('Seu nome em maiusculas é {}'.format(nome.upper()))
print ('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome)))
print('Seu primeiro nome tem {} letras ' .format(nome.find(' ')))

#unidade,dezena,centena,milhar
numero = int(input('Informe um numero ' ))
n = str(numero)
print('Analisando o numero {} '.format(numero))
print('Unidade {} '.format(n[3]))
print('Dezena {} '.format(n[2]))
print('Centena {} '.format(n[1]))
print('Milhar {} '.format(n[0]))
#jeito 2 sem 3 numeros para ler
numero = int(input('Informe um numero ' ))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {} '.format(numero))
print('Unidade {} '.format(u))
print('Dezena {} '.format(d))
print('Centena {} '.format(c))
print('Milhar {} '.format(m))

#verificando as letra de um texto
cid= str(input('Qual o nome da sua cidade?'))
print(cid[:5] == 'Santo')
#(retirando espaço)
cid= str(input('Qual o nome da sua cidade?')).strip()
print(cid[:5].upper == 'Santo')

#procurando uma palavra dentro de uma spring
nome=str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva?{}'.format('SILVA'in nome.upper()))

#lendo uma frase e mostrando quantas vezes uma letra aparece
frase=str(input('Digite uma frase: ')).upper().strip()
print('Analisando Frase')
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} .'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {} .'.format(frase.rfind('A')+1))

#nome completo fatiando
n=str(input('Digite seu nome completo: ')).strip()
nome=n.split()
print('Muito prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0] ))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

#tempo do seu carro com condição
tempo=int(input('Quantos anos tem seu carro ? '))
print('Carro novo'if tempo<3 else'carro velho')
print('--FIM--')

#EXEMPLO
nome= str(input('Qual seu nome? ')).strip()
if nome == 'Luan':
    print('Que nome bonito voce tem!')

else: 
    print('Bom dia, {}'.format(nome))

#jogo de advinhação
from random import randint
computador = randint(0,10)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar ... ')
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
print('-=-'*100)
msg="O numero escolhido foi {} ".format(computador)
print(msg)
if jogador == computador:      
    print('Voce Acertou')
else:
    print('Voce errou')

#radar eletronico
velocidade = float(input('Qual a velocidade do Carro? '))
multa = (velocidade-80) * 7

if velocidade > 80:
    print('Voce Foi multado em R${:.2f} '.format(multa))

if velocidade < 80: 
    print('Voce esta dentro do limite permitido boa viagem')  

#par ou impar
numero = (int(input('Me diga um numero ')))
resultado = numero % 2 
if resultado == 0:
    print('par')
else:
    print('Impar')

#calculando passagem de uma viagem 
distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a Viajar {}km'.format(distancia))

preço = distancia *0.50 if distancia < 200 else distancia *0.45

'''if distancia < 200 :
    preço = distancia * 0.50
else:  
    preço = distancia * 0.45'''

print('O preço da sua passagem será de R${:.2f}'.format(preço))

#calculo de ano bissexto
ano = int(input('Que ano quer analisar?'))

if ano == 0 :
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))

else:
    print('O ano de {} Não é bissexto'.format(ano))

#calculo menor valor
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

if primeiro<segundo and primeiro<terceiro:
    menor = primeiro 

if segundo<primeiro and segundo<terceiro:
    menor = segundo

if terceiro<primeiro and terceiro<segundo:
    menor = terceiro


print('O menor valor digitado foi {} '.format(menor))

