numero = float(input("Digite um número: "))
lista = []
menores = []
maiorMed = []
somadorNormal = 0
somadorQuantValores = 0 

while (numero != -1):
  lista.append(numero)
  somadorQuantValores += 1
  somadorNormal += numero
  numero = float(input("Digite um número: "))

if (somadorQuantValores == 0):
  media = somadorNormal/ 1
else:
  media = somadorNormal/ somadorQuantValores

for i in lista:
  if(i > media):
    maiorMed.append(i)
    
quantMaiorMed = len(maiorMed)

for x in lista:
  if (x < 7):
    menores.append(x)
    
tamMenor = len(menores)

print(f"\nA média dos valores informados pelo usuário é: {media} \nA quantidade de valores acima da média calculada são: {quantMaiorMed} , que são os seguintes números: {maiorMed} \nA quantidade de valores abaixo de 7 são: {tamMenor} , que são os seguintes número(s): {menores}")