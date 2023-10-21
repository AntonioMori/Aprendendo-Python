numeros = []
import random

g = int(input("Digite o tamanho da sequência: "))
for x in range(g):
  y = random.randint(0,100)
  numeros.append(y)

contador = 0
print(f"\nEssa é a lista: {numeros}\n")
for num_atual in numeros: 
  if(num_atual % 3 == 0):
    print(f"O número {num_atual} é divisível por 3")
    contador = contador + 1
    
  elif(num_atual % 3 != 0):
    print(f"O número {num_atual} Não é div")

print(f'\nEssa é a quantidade de números que são divisiveis por "3": {contador} ')

#-----------------------------------------------------------------------

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
tamanho_lista = int(input("Digite quantos números vão ter na lista: "))
print( "\nDigite os números a serem adicionados na lista: \n")

for i in range(10):
  x = int(input("Digite o valor: "))
  lista_numeros.append(x)



lista_numeros.reverse()
print(lista_numeros)

print(lista_numeros[::-1])  

#---------------------------------
#questão 3

notas = []
g = int(input("Digite a quantidade de notas a serem verificadas: "))

somador = 0

for x in range(g):
  y = int(input("Digite a nota do aluno: "))
  notas.append(y)
  somador += notas[x]

print(somador)

#--------------------------------
#questão 4

notas = []
g = int(input("Digite a quantidade de notas a serem verificadas: "))

maior_numero = 0

for x in range(g):
  y = int(input("Digite a nota do aluno: "))
  notas.append(y)
  if(notas[x] > maior_numero):
    maior_numero = notas[x]

print(f"O maior número informado é: {maior_numero}")

#---------------------------------------
# questão 5

notas = []
g = int(input("Digite a quantidade de notas a serem verificadas: "))

somador = 0

for x in range(g):
  y = int(input("Digite a nota do aluno: "))
  notas.append(y)
  somador += notas[x]

media = somador / len(notas)
print(f"\nA soma dos números é: {somador}")
print(f"A média dos números é: {media}")

# -----------------------------------------
#  Questão 6
#  Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50

lista=[]
for x in range(51):
  if(x % 2 == 1):
    lista.append(x)
    
print(lista)


#Questão 7)
#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num_inicial = int(input("Digite o número inicial: "))
num_final = int(input("Digite o número final: "))
lista = []
for x in range(num_inicial , num_final + 1 , 1):
  lista.append(x)

print(f"\n{lista}")



#Questão 8)
#Altere o programa anterior para mostrar no final a soma dos números

num_inicial = int(input("Digite o número inicial: "))
num_final = int(input("Digite o número final: "))
somador = 0
for x in range(num_inicial , num_final + 1 , 1):
  somador = somador + x

print(f"\nA soma dos valores entre {num_inicial} e {num_final} é o total de {somador}")



#Questão 9)
#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


num_tabuada = int(input("Digite o número do qual você deseja ver a tabuada: "))

alteracao = input("Você deseja aumentar a tabuada para exibir quantidades superiores a dez? ")

if(alteracao == "Sim" or alteracao == "sim" or alteracao == "SIM" or alteracao == "yes" ):
  
  tamanho_tabuada = int(input(f"Qual o tamanha desejado da tabuada do {num_tabuada}? "))
  print()
  
  for x in range(tamanho_tabuada+1):
    valor = num_tabuada * x
    print(f"{num_tabuada} x {x} = {valor}")


elif(alteracao == "Não" or alteracao == "NÃO" or alteracao == "Nao" or alteracao == "NAO" or alteracao == "não" or alteracao == "nao" or alteracao == "n" or alteracao == "N"):
  
  for x in range(11):
    valor = num_tabuada * x
    print(f"{num_tabuada} x {x} = {valor}")





#Questão 10)
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

condicao = input('Digite "a" se você quer digitar os 10 números manualmente, digite "b" se desejar o intervalo entre dois números: ')
lista = []
somador_imp = 0
somador_par = 0
if(condicao == "a" or condicao == "A"):
  print("\nDigite os valores a seguir:\n")
  
  for x in range(10):
    valor = int(input(f"Número {x+1}º é: "))
    lista.append(valor)

    
elif(condicao == "b" or condicao == "B"):
  
  num_inicial = int(input("\nDigite o número inicial: "))
  num_final = int(input("Digite o número final: "))
  lista = []
  
  for x in range(num_inicial , num_final + 1 , 1):
    lista.append(x)



for y in lista:
  if(y % 2 == 1):
    somador_imp = somador_imp + 1
  elif(y % 2 == 0):
    somador_par = somador_par + 1
    
print(f"\nEssa é a lista: {lista} e tem como tamanho: {len(lista)} elemento(s)")
print(f"\nA lista tem {somador_par} número(s) par(es).\nA lista tem {somador_imp} número(s) ímpar(es).")

#Questão 11)
# Faça um programa que leia uma frase, e, em seguida, diga quantas vogais existem na frase.
vogais = "AaEeIiOoUu"
palavra = input("Digite uma palavra: ")
contador_vogais = 0

for x in palavra:
  if x in vogais:
    contador_vogais += 1

print(f"\nNa palavra {palavra} existem {contador_vogais} vogais.")


#Questão 12)
# Faça um programa que leia 20 números inteiros e armazene-os em uma sequência. Armazene os números pares na sequência PAR e os números ÍMPARES na sequência ímpar. Ao final, imprima as três sequência.
condicao = input('Digite "a" se você quer digitar os 20 números manualmente, digite "b" se desejar o intervalo entre dois números: ')
lista = []
lista_impar = []
lista_par = []
if(condicao == "a" or condicao == "A"):
  print("\nDigite os valores a seguir:\n")
  
  for x in range(20):
    valor = int(input(f"Número {x+1}º é: "))
    lista.append(valor)

    
elif(condicao == "b" or condicao == "B"):
  
  num_inicial = int(input("\nDigite o número inicial: "))
  num_final = int(input("Digite o número final: "))
  lista = []
  
  for x in range(num_inicial , num_final + 1 , 1):
    lista.append(x)



for y in lista:
  if(y % 2 == 1):
    lista_impar.append(y)
  elif(y % 2 == 0):
    lista_par.append(y)
    
print(f"\nEssa é a lista: {lista} e tem como tamanho: {len(lista)} elemento(s)")
print(f"\nA lista Par tem a seguinte sequência: {lista_par}")
print(f"A lista impar tem a seguinte sequência: {lista_impar}")


#Questão 13)
# Faça um programa que peça as quatro notas de 5 alunos, calcule e armazene numa sequência a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

quant_alunos = int(input("Digite a quantidade de alunos: "))
quant_notas = int(input("Digite a quantidade de notas por aluno: "))
media = []
medias_aprovadas = []
for aluno in range(quant_alunos):
  notas = 0
  print(f"\nNotas do aluno {aluno+1}:\n")
  
  for nota in range(quant_notas):
    nota1 = int(input(f"Digite a sua {nota +1}º nota: "))
    notas += nota1

  media1 = notas / quant_notas
  media.append(media1)

for indice in media:
  if(indice >= 7):
    medias_aprovadas.append(indice)

print(f"\nAs médias são: {media}")
print(f"As médias aprovadas são: {medias_aprovadas}")


#Questão 14)
# Faça um programa que leia uma sequência de 5 números inteiros, e, em seguida, mostre a soma, a multiplicação e os números lidos


#lista de numeros lidos
lista = []
somador = 0
multiplicador = 1
print("Digite a seguir os valores da sequência de 5 números:\n")
for i in range(5):
  num = int(input("Digite um número: "))
  lista.append(num)
  somador += num
  multiplicador = multiplicador* num

print(f"\n A sequência é: {lista}, a soma dessa sequência é: ({somador}) e a multiplicação é: ({multiplicador})")


# Questão 15
#Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação na sua respectiva sequência. Imprima a idade e a altura na ordem inversa a ordem lida.

print("Olá, por favor preencha os campos a seguir em centímetros e idade respectivamente:\nExemplo: 175, 19\n")
alturas = []
idades = []
for pessoa in range(3):
  altura = int(input("Qual a sua altura? "))
  idade = int(input("Digite a sua idade: "))
  print()
  alturas.append(altura)
  idades.append(idade)

alturas.reverse()
idades.reverse()
print(f"Essa é a ordem inversa da sequencia de dados referentes a idades: {idades}\n")
print(f"Essa é a ordem inversa da sequencia de dados referentes a altura: {alturas}")



# Questão 16
#Faça um programa que leia uma sequência A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos da sequência.
print("Preencha os dados a seguir com números inteiros:\n")

sequencia = []
somador = 0
for numero in range(2):
  num = int(input("Digite um número: "))
  sequencia.append(num)
  quad = num * num
  somador += quad

print(f"\nA soma do quadrado dos elementos {sequencia}\nserá o equivalente á: {somador}")



# Questão 17
#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, etc).

temp_media_lista = []
somador = 0
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
meses_ac_med = []
meses_ac_med_nomes = []

print("Preencha com as temperaturas médias dos meses a seguir:\n")

for mes in range(12):
  
  mes2 = meses[0+mes]
  temp = int(input(f"{mes2}: "))
  temp_media_lista.append(temp)
  somador += temp

  
media_anual = somador / 12

print(f"\nEssa é a media anual de temperatura: {media_anual}")

for mes in range(12):
  mes2 = meses[0+mes]
  if (temp_media_lista[mes] >= media_anual ):
    print(f"\nNo mês de {mes2} - {temp_media_lista[mes]}º")
    
    meses_ac_med.append(temp_media_lista[mes])
    meses_ac_med_nomes.append(mes2)

print(f"\nEssa é a sequencia de meses que ultrapassou a média anual {meses_ac_med_nomes}")
print(f"Essa é a sequencia de temperaturas que ultrapassou a média anual {meses_ac_med}")





# Questão 18
#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em uma sequência . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use uma sequência de contadores (1-6), e, ao invés de solicitar ao usuário, gere números aleatórios para o lançamento dos dados.


dados = []
import random
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

tam_seq = int(input("Digite o tamanho da sequência: "))
for x in range(tam_seq):
  numeros_aleatorios = random.randint(1,6)
  dados.append(numeros_aleatorios)

for numero in dados:
  if (numero == 1):
    contador1 += 1
  elif (numero == 2):
    contador2 += 1
  elif (numero == 3):
    contador3 += 1 
  elif(numero == 4):
    contador4 += 1
  elif (numero == 5):
    contador5 += 1
  elif (numero == 6):
    contador6 += 1


print(f"\n{dados}\n")
print(f"O número 1 foi gerado {contador1} vezes.")
print(f"O número 2 foi gerado {contador2} vezes.")
print(f"O número 3 foi gerado {contador3} vezes.")
print(f"O número 4 foi gerado {contador4} vezes.")
print(f"O número 5 foi gerado {contador5} vezes.")
print(f"O número 6 foi gerado {contador6} vezes.")
