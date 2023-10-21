# criando as variáveis
horaStr = input("Informe a hora: ")
hora = int(horaStr)
minutoStr = input("Informe o minuto: ")
minuto = int(minutoStr)
segundoStr = input("Informe o sgundo: ")
segundos = int(segundoStr)

# convertendo horas e minutos para segundos
segundosHora = hora * 60 * 60
segundosMinuto = minuto  * 60

#calculando total de segundos
segundosTotal = segundosHora + segundosMinuto + segundos

# exibindo a quantidade total de segundos
print(segundosTotal)

print("Resposta questão 12")
print("Programa para cálculo de excesso de peso de peixes do João")
peso_peixes = float(input("Insira quantos quilos foram pegos"))
excesso = peso_peixes - 50
multa = excesso * 4
if (excesso == 0):
print("Você não irá pagar nenhum valor adicional hoje")
else:
print("Você teve um excesso de "+str(excesso)+" peixes por isso
irá pagar uma multa de: "+str(multa)+"$")


print("Resposta questão 13")
gaph = float(input("Digite quanto voce ganha por hora"))
hotpm = int(input("Digite o numero de horas trabalhadas por mês"))
salario_mensal = gaph*hotpm
imposto_de_renda = salario_mensal * 11/100
inss = salario_mensal * 8/100
sindicato = salario_mensal * 5/100
gastos = imposto_de_renda + inss + sindicato
salario_liquido = salario_mensal - gastos
print("Seu salário bruto é "+str(salario_mensal))
print("Você pagou "+str(imposto_de_renda)+" de imposto de renda")
print("Você pagou "+str(inss)+" ao INSS")
print("Você pagou "+str(sindicato)+" ao sindicato")
print("Sobrou para você "+str(salario_liquido))


print("Resposta questão 14")
tamanho_metros = float(input("Digite a área em metros quadrados a
ser pintada"))
if tamanho_metros % 54 == 0:
latas = tamanho_metros / 54
else:
latas = int(tamanho_metros/54)+1
preco = latas * 80
print ('%d latas' %latas)
print ('R$ %.2f' %preco)


print("Questão 15")
tamanho = float(input('Entre com o tamanho da área: '))
litros = tamanho / 6
latas = litros / 18
if latas % 18 != 0:
latas += 1
preco = latas * 80
galoes = litros / 3.6
if galoes % 3.6 != 0:
galoes += 1
preco2 = galoes * 25
# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)
if litros - (mistura_lata * 18) % 3.6 != 0:
mistura_galao += 1
print('Apenas latas de 18 litros: %d' % latas, 'preço: %d' % preco)
print('Apenas galões de 3.6 litros: %d' % galoes, 'preço: %d' % preco2)
print('Mistura: %d latas e %d galoes = %.2f' % (
mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25)))) 25))))