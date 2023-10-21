print("Seja bem-vindo ás atividades de fixação do aluno: Antonio Umberto Camargo Mori \n1º Período Engenharia da computação (UFRPE)\nProfessor: Giovanni Silva\n                            Atividade 2\nQuestão 1) Demonstre se o número é positivo, negativo ou neutro:")
a = int(input("\nDigite um número inteiro desejado:"))
if(a > 0):
  print(f"\nSeu número {a} é positivo!")
elif(a == 0):
  print(f"\nSeu número {a} é neutro!")
elif(a < 0):
  print(f"\nSeu número {a} é negativo!")
else:
  print("Você preencheu incorretamente! Tente novamente")


b = int(input("\nQuestão 2) Descubra se um número é par ou ímpar:\nDigite um número desejado:"))
if(b%2 == 0):
  print(f"\nO número {b} é par!")
elif(b%2 != 0 ):
  print(f"\nO número {b} é ímpar!")
else:
  print("\nVocê provavelmente não digitou um número seu boçau")


primeiro = float(input("\nQuestão 3) Descubra qual dos números informados é o maior:\nDigite o primeiro número:"))
segundo = float(input("Digite o segundo número:"))
terceiro = float(input("Digite o terceiro número:"))

maior = primeiro

if (segundo > maior):
      maior = segundo
  
if (terceiro > maior):
      maior = terceiro
print(f"O maior número informado é: {maior}")

c = float(input("\nQuestão 4) Defina se um número é ímpar, se é multiplo de 3 e se é divisor de 102:\nDigite o número á ser avaliado:"))
if(c%2 != 0):
  print("\nO número é impar!")
elif(c%2 ==0):
  print("\nO número não é impar!")

if (c%3 ==0):
  print("O número é multiplo de 3.")
elif(c%3 != 0):
  print("O número não é multiplo de 3.")

if (c % 102 == 0):
  print("O número é divisor de 102.")
elif(c % 102 != 0):
  print("O número não é divisor de 102.")



d = float(input("Questão 5) Loja de bijuterias da Natália \nDigite o valor a ser pago:"))
e = input("Digite o método de pagamento:")

if(d >= 100 and (e == "dinheiro" or e == "Dinheiro" or e == "DINHEIRO" or e == "dindin" or e == "DIMDIM" or e == "dimdim")):
  d1 = (d/100) * 90
  print(f"\nO valor a ser pago é {d1} com 10% de desconto em {e} ")
elif(d<100 and (e == "dinheiro" or e == "Dinheiro" or e == "DINHEIRO" or e == "dindin" or e == "DIMDIM" or e == "dimdim")):
  print(f"\nO valor a ser pago é {d} sem descontos aplicados")

if (e == "cartão" or e== "Cartão" or e == "CARTÃO" or e == "CARTAO" or e == "cartao" or e == "Cartao"):
  print("Perdão ainda não aceitamos cartão como método de pagamento :(")


if(e == "Cheque" or e == "cheque" or e== "CHEQUE"):
  print(f"\nO valor a ser pago é {d} com o método de pagamento {e}, portanto sem descontos :(")




f = float(input("Questão 6) Loja de bijuterias da Natália \nDigite o valor a ser pago:"))
g = input("Digite o método de pagamento(Cartão, dinheiro ou cheque):")


#Todas as condições serão verificadas:
#caso seja if e depois elif, o elif não será verificado caso o if seja True


if(f >= 100 and (g == "dinheiro" or g == "Dinheiro" or g == "DINHEIRO" or g == "dindin" or g == "DIMDIM" or g == "dimdim")):
  
  d1 = (f/100) * 90
  
  print(f"\nO valor a ser pago é {d1} com 10% de desconto em {g} ")


elif(f<100 and (g == "dinheiro" or g == "Dinheiro" or g == "DINHEIRO" or g == "dindin" or g == "DIMDIM" or g == "dimdim")):
  print(f"\nO valor a ser pago é {f} em {g} sem descontos aplicados")


if(g == "Cheque" or g == "cheque" or g == "CHEQUE"):
  print(f"\nO valor a ser pago é {f} com o método de pagamento {g}, portanto sem descontos :(")
  
if (g == "cartão" or g== "Cartão" or g == "CARTÃO" or g == "CARTAO" or g == "cartao" or g == "Cartao" or g == "cartap" or g == "cartaum" or g == "Cartaum"):
  cd6 = input("Crédito ou débito?:")


  
  if(cd6 =="débito" or cd6 =="debito" or cd6 =="DEBITO" or cd6 =="DÉBITO" or cd6 =="Débito" or cd6 =="Debito" ):
    print(f"O valor a ser pago é {f} em {g} no débito")


  elif(cd6 == "crédito" or cd6 == "credito" or cd6 == "Crédito" or cd6 == "Credito" or cd6 == "CREDITO" or cd6 == "CRÉDITO"):
    
    parcelas = int(input("Digite a quantidade de parcelas:"))
    
    if(parcelas <= 3):
      valorparcelas = f/ parcelas
      print(f"\nO valor a ser pago é {f} no {g} em  {parcelas}x vezes de R$:{valorparcelas:,.2f}")
    else:
      print("Desculpa não aceitamos pobres tao pobres assim KKKK que tem que parcelar em mais de 4 vezes... ;-;")







