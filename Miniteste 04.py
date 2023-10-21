#questão 1
a = 2
b = 9
while ( b - a > 1 ) :
 c = 2 * b
 b = b - 1
 a = a + 2
c = ( c / 2 ) + a

print(f"valor de a = {a}")
print(f"valor de b = {b}")
print(f"valor de c = {c}")

#questão 2

a = 8
b = 5
while ( a + b < 20 ) :
 c = a - b
 if ( c > 4 ) :
  d = 7 + c
 else :
  d = 2 + c
 a = a +1
 b = b + 2

print(f"valor de a = {a}")
print(f"valor de b = {b}")
print(f"valor de c = {c}")
print(f"valor de d = {d}")

#questão 3

b = 5
c = 1
a = b + c
d = b - c
while ( b > 1):
 d = b - c + 1
 while ( d > 1 ) :
  if ( d >= 3 ) :
   a = c + 1
  else :
   a = a +4
  d = d - 2
 b = b - 2
c = a + b + d

print(f"valor de a = {a}")
print(f"valor de b = {b}")
print(f"valor de c = {c}")
print(f"valor de d = {d}")

#Questão 1

#Desenvolva um programa que leia números informados pelo usuário até que o usuário informe o valor -100. Em seguida, exiba a soma, o maior dentre os números e a média dos números. Lembre que você não deve usar nenhuma função já disponibilizada em python que encontre esses valores de interesse, mas sim desenvolver seu algoritmo para isso. Além disso, desenvolva a sua solução de modo a não possuir trechos de código repetidos.

num = int(input("Digite um número: "))
#soma dos números digitados
somador = 0
#quatidade de vezes em que um número foi digitado
somador2 = 0
maiorNum = 0

while(num != -100):
  somador += num
  somador2 += 1 
  
  if num > maiorNum:
    maiorNum = num
    
  num = int(input("Digite um número: "))

  
#media dos números informados
med = somador / somador2

print(f"Essa é a soma dos números informados: {somador}\nO maior número informado: {maiorNum}\nMédia dos números: {med:,.2f}")


#Questão 2
#Escreva um programa que receba como entrada dois números inteiros informados pelo usuário, e, em seguida, exiba a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos. Por exemplo, se o usário informar os números 3 e 7, o programa deve exibir o valor 25 (3 + 4 + 5 + 6 + 7). Caso não exista números positivos no intervalo, a soma será 0.
print("Digite o número inicial e o número final desejado para gerarmos uma lista\n")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o ultimo número: "))
lista = []
somaPositivos = 0
for i in range(n1,n2+1,1):
  lista.append(i)

for x in lista:
  if (x >= 0):
    somaPositivos += x
print(f"\nA soma dos números positivos da lista é: {somaPositivos}")



#Questão 3

#Desenvolva um programa que leia um texto (string) informado pelo usuário, e, em seguida, exiba o total de vogais presentes no texto informado. Lembre de considerar a posssibilidade de vogais estarem presentes de forma maiúsculas ou minúsculas.

#para cada letra ela irá verificar se é uma vogal ou não, se for vai retornar o valor verdadeiro "True" senão irá retornar o valor negativo "false".
def testeVogal(letra):
  vogais = "AaEeIiOoUu"
  
  for i in vogais:
    if(i == letra):
      return True
  return False

palavra = input("Digite uma palavra:")
somadorDeVogais = 0

#para cada letra na palavra dada pelo usuário ele irá fazer aquela função de verificar se é uma vogal "testeVogal", se for vai retornar o valor verdadeiro e logo podemos somar a quantidade de vezes em que a função retornou o valor verdadeiro, tendo então um contador de vogais.
for letra in palavra:
  if (testeVogal(letra) == True):
    somadorDeVogais +=1

print(f"\nEssa é a quantidade de vogais nesta palavra: {somadorDeVogais}")