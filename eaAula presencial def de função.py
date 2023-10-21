#Aula presencial (Aprendemos a montar uma função, "Menor nome possível representativo (que de pra entender e seja facil manutenção e entendimento de outros)"  e tambem tem que ter o return no final e ele precisa ter o que será necessário para que aquela função seja excutada exemplo: geraSequenciaAnleatoria(tamanhoSeq): precisaremos o que está dentro do () que é o tamanho da sequencia. da para usar uma função dentro da outra como podemos ver nas linhas 20 e 19 )

import random

def menorNum(lista):
  menor = lista[0]
  for x in lista:
    if x < menor:
      menor = x
  return(menor)

def geraSequenciaAnleatoria(tamanhoSeq):
  listaAleatoria = []
  for i in range(tamanhoSeq):
    numAleatorio = random.randit(10,50)
    listaAleatoria.append(numAleatorio)
  return(listaAleatoria)

listaAtual = geraSequenciaAnleatoria(10)
print(menorNum(listaAtual))




#Um jeito de se fazer 

def testeVogal(letra):
  
  vogais = "AaEeIiOoUu"
  for l in vogais:
    if(l == letra):
      return True
  return False
  
print(testeVogal("b"))
print(testeVogal("e"))

#Jeito mais otimizado

def testeVogal(letra):
  
  vogais = "AEIOU"
  if(str(letra).upper() in vogais):
    return True
  else:
    return False
  
print(testeVogal("b"))
print(testeVogal("e"))

#Função calcula maior número 


num1 = float(input("Digite um número qualquer: "))
num2 = float(input("Digite um outro número qualquer: "))

def calculaMaior(num1, num2):
  maiorNum = num1
  if(num2 >= num1):
    maiorNum = num2

  return maiorNum

#Verificação manual de algo que nós já sabemos o resultado que irá dizer se o nosso algorítmo está correto para quaisquer outras variáveis
assert calculaMaior(3,8) == 8

print(f"\n Esse é o maior número: {calculaMaior(num1,num2):,.1f}\n")
print(calculaMaior(3,8))
print(calculaMaior(5,1))
print(calculaMaior(4,4))
print(calculaMaior(3.2,5.8))



#como importar e uso de assert

import MorisCollection
print(MorisCollection.Mult4(8))
assert not MorisCollection.Mult4(10)
