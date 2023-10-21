#Questão 2 Escreva um programa que receba como entrada números inteiros até que um número maior que 100 seja digitado. Em seguida, esse programa deve exibir a quantidade de números que são pares e positivos. 

listaNum = []
listaPar = []
listaImp = []

num = int(input("Digite um número:"))

while( num <= 100):
  listaNum.append(num)

  num = int(input("Digite um número:"))

for i in listaNum:
  if (i % 2 == 0):
    listaPar.append(i)
  elif(i % 2 != 0):
    listaImp.append(i)
    
print(listaNum)
print(f"\nLista dos números pares: {listaPar}\nLista dos números ímpares: {listaImp}")




#Questão 3 Escreva um programa que receba como entrada números inteiros até que o número 0 seja informado. Em seguida, o programa deve exibir a soma dos números que são múltiplos de 3. 

num = int(input("Digite um número: "))
listaNum = []
mult3 = []
somaMult3 = 0
while (num > 0):
  listaNum.append(num)
  if(num % 3 == 0):
    mult3.append(num)
    somaMult3 += num
  num = int(input("Digite um número: "))
print(f'\nA lista de números digitados: {listaNum}\nMultiplos de 3:   {mult3}\nSoma dos multiplos de 3:   "{somaMult3}"')



#Questão 4 Escreva um programa que receba como entrada vários números, até que seja informado o valor 100, e exiba a média dos números pares. (Dica: a média dos números é calculada dividindo-se sua soma pela quantidade de números. Porém, como não é possível dividir por zero, se houver dúvida sobre a quantidade, é preciso testar antes de fazer o cálculo) 
#for e len
num = int(input("Digite um número: "))
lista = []
numPar = []
somadorPar = 0
while (num != 100):
  lista.append(num)
  
  if(num % 2 == 0 ):
    numPar.append(num)
    somadorPar += num
  num = int(input("Digite um número: "))



if(somadorPar == 0):
  print(f"\nEssa é a lista de números informados: {lista}\n\nNão houveram números pares informados.")

else:
  media = somadorPar / len(numPar)
  print(f"\nEssa é a lista de números informados: {lista}\n\nNúmeros pares da lista: {numPar}\n\nMédia dos números pares: {media:,.0f}")


# O Ministério da Saúde deseja aplicar uma nova dose de reforço contra o COVID19 em todas as pessoas acima de 60 anos. Escreva um programa para ser usado em uma secretaria municipal que receba como entrada a idade de várias pessoas até que o usuário não deseje mais informar dados (considere que o usuário não quer mais informar dados quando ele informar uma idade negativa). O programa deve calcular e exibir a quantidade total de doses de vacinas necessárias. 
vermelho = "\033[1;31m"
bold = "\033[;1m"
idade = int(input("Digite uma idade: "))
pessoas = []
idosos = []
while(idade > 0):
  if(idade > 125):
    print(f"{vermelho}Idade {idade} anos inválida!\033[m")
    idade = int(input("\nDigite uma idade válida:"))
  elif(idade >= 60):
    idosos.append(idade)
    idade = int(input("Digite uma idade: "))
  else:
    idade = int(input("Digite uma idade: "))

print(f"A quantidade de idosos são: {len(idosos)}\nPortanto serão necessárias {len(idosos)} vacinas.")


#Ultima questão Escreva um programa que receba como entrada a quantidade de filhos dos vários funcionários de uma empresa, até que seja informada uma quantidade negativa, e exiba a quantidade média de filhos do grupo. (Dica: a média pode ser obtida dividindo-se a soma dos números pela quantidade deles) 
quantFilhos = 0
somadorDePais = 0
filhos = int(input("Digite a quantidade de filhos: "))

while (filhos >= 0):
  quantFilhos += filhos
  
  somadorDePais += 1
  filhos = int(input("Digite a quantidade de filhos: "))
media = quantFilhos / somadorDePais
print(f'A idade média de filhos do grupo são: "{media} filhos" por pai.')