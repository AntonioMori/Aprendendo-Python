print("Seja bem-vindo ás atividades de fixação do aluno: Antonio Umberto Camargo Mori")
print("1º Período Engenharia da computação (UFRPE)")
print("Professor: Giovanni Silva")

print("\nQuestão 1) - (Calculadora de porcentagem)")
# np1 = Número desejado 1
nd1 = int(input("Digite o número desejado:"))
# np = Número da porcentagem
np = int(input("Digite a porcentagem desejada:"))
# rs1 = Resultado da porcentagem 1
rp1 = (nd1/100) * np
print("Resultado:", np,"% de",nd1,"é",rp1)

print("\nQuestão 2) - (Conversor do horário para minutos)")
#qd = Quantidade de dias , qh = quant de horas , qm = min
qd = int(input("Digite a quantidade de dias:"))
qh = int(input("Digite as horas desejadas:"))
qm = int(input("Digite os minutos desejados:"))
# md = Minutos dos dias
md = (qd*24) * 60
# mh = Minutos das horas
mh = qh*60
# mt = Minutos totais
mt = md + mh + qm
print("A quantidade de minutos desejada são:", mt,"minutos dentro de",qd,"dias", qh,"horas e", qm, "minutos.")

print("\nQuestão 3) - (Conversor metros para centímetros)" )
#qm3 = Quantidade de metros questão 3
qm3 = int(input("Digite a quantidade de metros desejados para conversão em centímetros:"))
#cmt = centímetros totais 
cmt = qm3 * 100
print("A quantidade de", qm3, "metros em centimetros são:",cmt,"cm's")

print("\nQuestão 4) - (Calculadora da área de uma forma circular)")
# ri = Raio do círculo desejado
ri= int(input("Digite o raio do círculo desejado:"))
# r2 =  raio ao quadrado
areac = (3.14 * ri*ri)
print("A área de um circulo cujo raio é", ri, "é equivalente a:",areac) 
print("Area =", areac)

print("\nQuestão 5) - (Calculadora da área de um quadrado perfeito)")
#tm1 = tamanho do quadrado largura ou altura
tm1 = int(input("Digite a altura ou largura do quadrado perfeito desejado:"))
# ard = area do quadrado
ard = tm1 * tm1
print("A área de um quadrado perfeito de altura de", tm1, "por",tm1,"de largura é equivalente á:",ard)
ard2 = ard * 2
print("Seu dobro é equivalente a:",ard2)

print("\nQuestão 6) - (Calculadora de salários)" )
# sph = Salário por hora
sph = int(input("Digite o seu salário por hora:"))
# ht = Horas trabalhadas por semana
hts = int(input("Digite a quantidade de horas trabalhadas por semana:"))
salarioporsemana = sph * hts 
# st = salário total
st= salarioporsemana * 4
print("De acordo com os cálculos do robozin Mori, ganhando",sph,"hora, trabalhando", hts,"horas por semana, você ganhará", st,"reais como salário ao final do mês.")

print("\nQuestão 7) - (Conversor de temperaturas Fahrenheit para Celsius)" )
# tempf = temperatura fahrenheit
tempf = int(input("Digite a temperatura em Fahrenheit:"))
# c =  celsius
c = ((tempf-32) /1.8)
print("A temperatura em graus Celsius é",c)

print("\nQuestão 8) - (Conversor de temperaturas graus Celsius para Fahrenheit)" )
#tempc =  temperatura celsius
tempc = int(input("Digite a temperatura em Celsius:"))
#f = fahrenheit
f = (tempc* 1.8) + 32 
print("A temperatura",tempc,"graus serão",f,"Fahrenheit")

print("\nQuestão 9) - (Entrada de dados números inteiros e reais)")
n1 = int(input("Digite o primeiro numero inteiro desejado:"))
n2 = int(input("Digite o segundo numero inteiro desejado:"))
n3 = int(input("Digite um numero real:"))
a9 = (n1 * 2)*(n2 / 2)
b9 = (n1 * 3)+ n3 
c9 = (n3*n3)*n3
print("a) O produto do dobro do primeiro com metade do segundo será:",a9)
print("b) A soma do triplo do primeiro com o terceiro será:",b9)
print("c) O terceiro elevado ao cubo será:",c9)

print("\nQuestão 10) - (Calculadora do peso ideal baseado em sua altura)")
h10 = float(input("Digite sua altura em metros:"))
# pi = peso ideal
pi = (72.7 * h10) - 58
print("O seu peso ideal baseado na algura",h10,"será de",pi,"kilogramas")

print("\nQuestão 11) - (Calculadora do peso ideal baseado em sua altura baseado no gênero)")
h = float(input("Digite a sua altura:")) 

gn = input("Digite seu gênero:")
if(gn =="homem")or(gn== "Homem") or(gn=="macho")or(gn=="Macho"):
  ph11 = (72.7 * h) - 58
  print("O seu peso ideal são:",ph11, "kilogramas")
  
elif(gn== "mulher")or(gn== "Mulher"):
  pm11 = (62.1 * h) - 58
  print("O seu peso ideal são:",pm11,"kilogramas")

else:
  print("você preencheu incorretamente a parte do gênero")

print("\nQuestão 12) - (Calculadora de multas do joão pescador)")
peso = 0
while(peso == 0):
  peso = float(input("Digite a quantidade em Kilogramas de peixes pegos:"))
  if(peso >50):
    vlm =(peso - 50) * 4
    print("A quantidade de peixes é",peso,"portanto, excedeu a quantidade legal e voce deverá pagar: R$:",vlm,"reais.")

  elif(peso <= 50 and peso > 0 ):
    print("A quantidade de peixes pescados é",peso,"kg, inferior ou equivalente a quantidade legal de kilogramas permitidas, portanto não haverá multas.")
  else:
    print("Você não preencheu corretamente")

print("\nQuestão 13) - (Calculadora de taxas pagas ao governo)")
# sph = Salário por hora
sph2 = int(input("Digite o seu salário por hora:"))
# ht = Horas trabalhadas por semana
hts2 = int(input("Digite a quantidade de horas trabalhadas por semana:"))
salarioporsemana2 = sph2 * hts2 
# st = salário total
st2= salarioporsemana2 * 4
print("De acordo com os cálculos do robozin Mori, ganhando",sph2,"hora, trabalhando", hts2,"horas por semana, você ganhará", st2,"reais como salário ao final do mês.")

print("\nQuestão 14) - (Loja de tintas)")
import math
lado1 = float(input("Digite o tamanho do primeiro plano:"))
lado2 = float(input("Digite o tamanho do segundo plano:"))
area14 = lado1 * lado2
rendlata = 18 * 3
custlata = 80
qnt = area14 / rendlata
preco = qnt * custlata
print("Área:",area14)
if(lado1 >0 and lado2>0):
  math.ceil()
  print("Pintando uma área de",area14,"")

elif(lado1 == 0 or lado2 == 0):
  print("Digite um valor correto")

