numero = int(input("Digite um numero inteiro:"))
#Todas as condições serão verificadas:
#caso seja if e depois elif, o elif não será verificado caso o if seja True
if  (numero % 2 == 0):
  print("Seu número é divisível por 2")
if(numero % 5 == 0):
  print("Seu número é divisivel por 5 ")
if(numero % 7 == 0):
  print("Seu número é divisivel por 7 ")
if(numero % 3 == 0):
  print("Seu número é divisivel por 3 ")
#----------------------------------------------
precoGasolina = 5.5
precoEtanol = 3.3
precoDisel = 3.1


tipoCombustivel = input("Qual o tipo de combustível? ")
qtLitros = float(input("Quantos litros? "))

valor = 0.0

if (tipoCombustivel == "gasolina" or tipoCombustivel == "gas" or tipoCombustivel == "GASOSA"):
     valor = precoGasolina * qtLitros
elif (tipoCombustivel == "disel"):
     valor = precoDisel * qtLitros
elif (tipoCombustivel == "etanol"):
     valor = precoEtanol * qtLitros
else:
     print("Tipo de combustível não é válido!")

print(valor)
print(90>=100)

