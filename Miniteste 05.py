#QIESTÃO 1 
#Desenvolva uma função que receba uma string como argumento e retorne a quantidade de espaços em branco contidos nessa String. O nome da função deve ser: 
#variavelText = input("Digite uma frase , texto ou palavra: ")
def contaBrancos(texto):
  #Tamanho inicial do texto
  tamanhoInicialStr = len(texto)
  #Função para substituição dos espaçoes em branco
  texto = texto.replace(" ", "")
  #Tamanho após a comparação, a diferença é a quantidade de espações em branco.
  tamanhoFinalStr = len(texto)
  diferença = tamanhoInicialStr - tamanhoFinalStr
  if diferença > 0:
    return diferença
  elif diferença <= 0:
    return 0
  
texto1 = "Antonio é muito bonito teste "
assert contaBrancos(texto1) == 5
print(contaBrancos(texto1))

#Esse if foi adicionado pois ao utilizar a função criada eu percebi que caso não fosse informado nenhum espaço em branco não iria haver retorno
#uma solução seria tambem a seguinte

  #if diferença > 0:
  #  return diferença
 #elif diferença <= 0:
  #  return 0



#Desenvolva uma função que receba uma string como argumento e retorne a quantidade de vezes que alguma vogal (não precisa considerar acentos) aparece no texto. O nome da função deve ser: contaVogais(texto)

def contaVogais(texto):
  somadorDeVogais = 0
  for letra in texto:
    vogais = "AaEeIiOoUu"
    for caractere in vogais:
      if(caractere == letra):
        somadorDeVogais +=1
    
  return somadorDeVogais
    
      

texto1 = "A"

print(contaVogais(texto1))



#Questão 3
#Desenvolva um programa que interaja com o usuário solicitando que ele informe uma string (tal como palavra, frase ou texto) até que ele não queira mais informar. Após a inserção das strings, ao final da execução, esse programa deve exibir a quantidade de strings informadas que possuem espaços em branco e também a quantidade total de vogais considerando todos os textos informados pelo usuário. Note que não é necessário armazenar todos os textos, mais sim calcular as variáveis de interesse do programa.
#É importante destacar que esse programa deve usar as funções desenvolvidas nas questões anteriores: contaBrancos(texto) e contaVogais(texto)
def contaBrancos(texto):
  #Tamanho inicial do texto
  tamanhoInicialStr = len(texto)
  #Função para substituição dos espaçoes em branco
  texto = texto.replace(" ", "")
  #Tamanho após a comparação, a diferença é a quantidade de espações em branco.
  tamanhoFinalStr = len(texto)
  diferença = tamanhoInicialStr - tamanhoFinalStr
  if diferença > 0:
    return diferença
  elif diferença <= 0:
    return 0

def contaVogais(texto):
  somadorDeVogais = 0
  for letra in texto:
    vogais = "AaEeIiOoUu"
    for caractere in vogais:
      if(caractere == letra):
        somadorDeVogais +=1
    
  return somadorDeVogais    

print('Caso não deseje adicionar mais frases digite: "nao" ')
texto1 = str(input("Digite uma frase, texto ou palavra: "))
strsComBrancos = 0
vogaisTotais = 0

while texto1 != "nao":
  
  if contaBrancos(texto1) > 0:
    strsComBrancos += 1 
  if contaVogais(texto1) >= 1: 
    vogaisTotais += contaVogais(texto1)
    
  texto1 = str(input("Digite uma frase, texto ou palavra: "))
 

print(f"\nEssa é a quantidade de textos com espaçamentos em branco: {strsComBrancos}")
print(f"\nEssa é a quantidade de vogais totais encontradas em todas as palavras/textos digitados: {vogaisTotais}")
  