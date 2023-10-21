# Seja bem vindo á Biblioteca do Robozinho Mori

#Funções que eu já conheço:
# print() = usado para retornar ou printar algo no console
# int() =  converte em número inteiro
# str() = converte em uma string
# def = é usado como função built in para criar nossas próprias funções
#for i in range(10) = é usado para repetição
#range() = define um tamanho , uma quantidade, um range, usado muito com o for.
#while() = usado para repetições controladas pelo usuário(devemos ter cuidado com as 3 regrinhas)
#if = condicional se verdadeiro ... ou se tal condição for verdadeira, o elif é se outra condição for verdadeira
#else = se nenhum if ou elif for verdadeiro vai rodar os else.
#return = usado para dar um valor a ser retornado ao usar uma função criada usando o #def
#import = usado para importar uma biblioteca através pelo seu nome.
#Função Pura = não modifica o domínio, não produz efeitos colaterais em listas já existentes ou variáveis, e sim cria um produto daquilo, um resultado novo.


#Verificação Números multíplos de 4 
def Mult4(num):
  mult = False
  if(num % 4 == 0):
    mult = True
  return mult

#verificação de um menor número em uma lista
def menorNumLista(lista):
  menor = lista[0]
  for x in lista:
    if x < menor:
      menor = x
  return(menor)

#verificação de um menor número de dois números

def menorNum2(n1,n2):
  if n1 < n2:
    return n1
  else:
    return n2





#verificação de um MAIOR número em uma lista



    
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



#Modo de percorrer uma lista do final para o início, de traz para frente

def remove_impares(lista):
    
    # remove da lista usando a função pop(indice) versão FUNÇÃO NÃO PURA
    for indice in range(len(lista) - 1, -1, -1):
        if (lista[indice] % 2 != 0):
            lista.pop(indice)


lista = [10, 3, 6, 7, 9, 11, 22]

print(type(remove_impares(lista)))
assert lista == [10, 6, 22]


#Criar uma lista de tamanho personalizado com espaçamento de 10 em 10 
#lista = [10, 20, 30, 40, 50, 60, 70, 80]

lista = []
for i in range(1000):
    lista.append(i * 10)

print("O tamanho da lista é: ", len(lista))