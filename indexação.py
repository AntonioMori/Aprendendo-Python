print("Seja bem-vindo ás atividades de fixação do aluno: Antonio Umberto Camargo Mori \n1º Período Engenharia da computação (UFRPE)\nProfessor: Giovanni Silva\n                          Aula 4 (Presencial)\nConteúdo 2) Listas ,len, append e pop ")
a = "Antonio"

#indice da variável a , caractere 0 de Antonio (variavel[0])
print(f"Esse é o caractere inicial da sua palavra: {a[0]}")
#len é usado para dizer o tamanho da string 
print(f"Esse é o tamanho da sequência:{len(a)}" )
#Slicing = pegar um subconjunto dessa variável (variavel[0:3])
print(f"Esse é um subconjunto da variável: {a[0:3]}")
b = a[0:3]
print(f"Esse é o novo valor do nome {a}: {b}")


lista = [1,2,3,4,5,6,8,9,10]
c = int(input("\nDigite um numero a ser adicionado:"))
d = int(input("\nDigite uma posição a ser removido:"))
print(f"{lista[0]}," , lista[len(lista)-5])
lista.append(c)
lista.pop(d)
print(f"Essa é a nova lista: {lista}")

#------------------------------------------------------

lista1 = [10,20,30,40,50]
lista2 = [60,70,80,90,100]

lista1.append(11)
lista2.pop()

lista3 = lista2 +lista1
print(len(lista1))

g = "Hello world!"
print(g)
print(g[13])


a = "Antonio"

#indice da variável a , caractere 0 de Antonio (variavel[0])
print(f"\nEsse é o caractere inicial da sua palavra: {a[0]}, um indice")
#len é usado para dizer o tamanho da string 
print(f"Esse é o tamanho da sequência:{len(a)}, len" )
#Slicing = pegar um subconjunto dessa variável (variavel[0:3])
print(f"Esse é um subconjunto da variável: {a[0:3]}, slicing")
b = a[0:3]
print(f"Esse é o novo valor do nome {a}: {b}")

#Digitar qualquer coisa com espaços
    operacao = input('''
Digite a operação desejada:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
# Esse ,.2f significa que vão ficar apenas duas casas decimais depois da virgula
  print(f"\nO valor a ser pago é {f} no {g} em  {parcelas}x vezes de R$:{valorparcelas:,.2f}")
