from sympy import *
cadeia = input("digite uma fração:")
m = cadeia.find("/")
## o numerador irá aparecer antes do ": pontos", o m separa 
numerador = int(cadeia[:m]) 