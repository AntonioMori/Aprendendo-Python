print("Seja bem-vindo à Atividade do miniteste de número 3) \nDiscente: Antonio Umberto Camargo Mori \n1º Período Engenharia da computação (UFRPE)\nProfessor: Giovanni Silva\n                      Questão 1 - Calculadora")

#criei uma função só de bobeira mesmo
def calculadora():
#adição, subtração, multiplicação ou divisão    
    operacao = input("\nDigite o tipo de operação desejada: ")

#valores dos numeros desejados para a operação em float pq vc pediu
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

# se for adição ou sinonimos da palavra
    if (operacao == '+' or operacao == "adição" or operacao == "Adição" or operacao == "adicao" or operacao == "adiçao" or operacao == "adicão" or operacao == "Adiçao" or operacao == "Adicão" or operacao == "soma" or operacao == "Soma" or operacao == "SOMA" or operacao == "somar"):
        
        nsoma = n1 + n2
       
        print(f"\nA operação de adição dos números {n1} e {n2} trará como resultado: {nsoma:,.2f}")
      
        print(f"\n{n1} + {n2} = {nsoma:,.2f}")
        
      
# se for Subtração ou sinonimos da palavra e se a condição anterior "if" não for satisfeito.  
    elif (operacao == "-" or operacao == "Subtração" or operacao == "subtração" or operacao == "subtracao" or operacao == "subtraçao" or operacao == "subtracão" or operacao == "Subtraçao" or operacao == "Subtracão" or operacao == "diminuir" or operacao == "sulbtração" or operacao == "SUBTRAÇÃO" or operacao == "SUBTRACAO"): #se vc escrever errado kkkkk 
        
        nsub = n1 - n2
        
        print(f"\nA operação de subtração dos números {n1} e {n2} trará como resultado: {nsub:,.2f}")

        print(f"\n{n1} - {n2} = {nsub:,.2f}")


 #se for uma multiplicação ou sinonimos da palavra e se a condição anterior "elif" não for satisfeita
    elif (operacao == "*" or operacao == "Multiplicação" or operacao == "multiplicação" or operacao == "multiplicar" or operacao == "Multiplicacao" or operacao == "Multiplicaçao" or operacao == "Multiplicacão" or operacao == "multiplicaçao" or operacao == "multiplicacao" or operacao == "Multiplicar" or operacao == "MUTIPLICAÇÃO"):

        mult = n1 * n2
      
        print(f"\nA operação de multiplicação dos números {n1} e {n2} trará como resultado: {mult:,.2f}")
      
        print(f"\n{n1} * {n2} = {mult:,.2f}")

      
#se for uma divisão ou sinonimos da palavra e se a condição anterior "elif" não for satisfeita
    elif (operacao == "/" or operacao == "divisão" or operacao == "Divisão" or operacao == "Divisao" or operacao == "Divisaum" or operacao == "divisao" or operacao == "Dividir" or operacao == "me da um ponto extra ai vai pff" or operacao == "DIVISÃO" or operacao == "DIVISAO"):

        div = n1 / n2
        
        print(f"\nA operação de divisão dos números {n1} e {n2} trará como resultado: {div:,.2f}")

        print(f"\n{n1} / {n2} = {div:,.2f}")

      
    else:
        print("Você digitou uma operação inválida, por favor tente novamente ;-;")




calculadora()
print("\nObrigado por utilizar a calculadora do robozin Mori <3 .")











def lavanderia():
    qual_op = input('''\nSeja Bem vindo a Lavanderia do Robozin Mori
Digite o tipo de lavagem, temos as seguintes opções disponíveis:
\n(a) R$: 7,00 por peça de roupa ou
(b) R$: 5,00 por quilo de roupa
\nDigite a opção desejada: ''')

    if(qual_op == "a" or qual_op == "A" or qual_op == "peça" or qual_op == "peca" or qual_op == "por peça" or qual_op == "por peças" or qual_op == "por peca" or qual_op == "por pecas" or qual_op == "Por peças" ):
        secoa = input("Deseja acrescentar lavagem a seco por uma taxa de R$ 3,50 por peça? ")    
        if(secoa == "Sim" or secoa == "sim" or secoa == "si" or secoa == "sin" or secoa == "Sin"):
            quant1 = int(input("Digite a quantidade de peças:"))
            valor1 = (quant1 * 7) + (quant1 * 3.5) 
            print(f"\nO valor a ser pago é R${valor1:,.2f} por {quant1} peças lavadas com o acrescimo a seco.")
        elif(secoa == "Não" or secoa == "não" or secoa == "nao" or secoa == "Nao" or secoa == "NÃO" or secoa == "NAO"):
            quant2 = int(input("Digite a quantidade de peças:"))
            valor2 = quant2 * 7
            print(f"/nO valor a ser pago é R${valor2:,.2f} por {quant2} de peças de roupa lavadas.")
        else:
            print("\nVocê não respondeu corretamente a pergunta sobre lavagem a seco.")      
    
    elif(qual_op == "b" or qual_op == "B" or qual_op == "por quilo" or qual_op == "Por quilo" or qual_op == "quilo" or qual_op == "Quilo" or qual_op == "QUILO" or qual_op == "Quilograma" or qual_op == "quilograma" or qual_op == "POR QUILO"):
        secob = input("Deseja acrescentar lavagem a seco por uma taxa de R$ 3,50 por quilo de peças de roupa?")
        if(secob == "Sim" or secob == "sim" or secob == "si" or secob == "sin" or secob == "Sin"):
            quant3 = float(input("Digite a quantidade de quilos peças:"))
            valor3 = (quant3 * 5) + (quant3 * 3.5) 
            print(f"\nO valor a ser pago é R${valor3:,.2f} por {quant3} quilos de peças de roupa com acrescimo a seco.")
        elif(secob == "Não" or secob == "não" or secob == "nao" or secob == "Nao" or secob == "NÃO" or secob == "NAO"):
            quant4 = float(input("Digite a quantidade de quilos de peças:"))
            valor4 = quant4 * 5
            print(f"/nO valor a ser pago é R${valor4:,.2f} por {quant4} quilos de peças de roupa.")
        else:
            print("\nVocê não respondeu corretamente a pergunta sobre lavagem a seco.")
    else:
        print("Você não escolheu uma opção valida.")      
