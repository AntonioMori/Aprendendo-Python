#Aula Presencial 20/09/2022


#Desenvolva uma função que recebe uma lista com números inteiros e retorna uma lista com os índices dos números que são multiplos de 3
contador = 0
lista = []
def indicesDosMultDe3(lista):
  contador = -1
  listaIndices = []
  for i in lista:
    contador += 1
    if i % 3 == 0:
      listaIndices.append(contador)
  return(listaIndices)
print(indicesDosMultDe3([3,9,12,20,50,66]))



#Busque um elemento em uma lista de inteiros , busca sequencial
num1 = int(input("Digite o número a ser procurado na lista: "))
lista1 = []
for i in range(10):
    lista1.append(i * 10)

print(f"\nO tamanho da lista são {len(lista1)} indices")
print(lista1)
def BuscaDeInteiros(lista,num):
  for i in lista:
    if i == num:
      return True 
      break
    return False
print(BuscaDeInteiros(lista1,num1))