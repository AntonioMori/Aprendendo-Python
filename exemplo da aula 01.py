
nota1 = float(input("Digite a primeria nota: "))

nota2 = float(input("Digite a segunda nota: "))

frequencia = float(input("Qual o percentual de sua frequência (0 - 1)?"))

media = (nota1 + nota2)/2

reprovado_falta = frequencia < 0.75

print("A média obtida foi:", media)

if media >= 7 and not reprovado_falta:
    print("Aluno aprovado! Parabéns!")
elif media >=3 and not reprovado_falta:
    print("Aluno está na final! Estude!")
else:
    print("Aluno foi reprovado! Fica para próxima!")

print("Fim do programa!")



print(" (Calculadora de salários v1.0)" )
# sph2 = Salário por hora
sph2 = float(input("Digite o seu salário por hora:"))
# htm2 = Horas trabalhadas por mes
htm2 = float(input("Digite a quantidade de horas trabalhadas por mês:"))
# st2 = salário total por mes
st2 = sph2 * htm2 
print("O salário desse mês é R$:", st2)

print(" (Calculadora de salários v1.1)" )
# sph = Salário por hora
sph = float(input("Digite o seu salário por hora:"))
# ht = Horas trabalhadas por semana
hts = float(input("Digite a quantidade de horas trabalhadas por semana:"))
# sps = salário por semana
sps = sph * hts 
# st = salário total
st= sps * 4
print("De acordo com os cálculos do robozin Mori, ganhando",sph,"hora, trabalhando", hts,"horas por semana, você ganhará", st,"reais como salário ao final do mês.")





