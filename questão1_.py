import os
os.system

# faça um algoritmo que leia os valores A,B,C e imprima na tela se a soma de A + B é menor que C


primeiro_numero = int(input("digite o primeiro numero:"))
segundo_numero = int(input("digite o segundo numero:"))
terceiro_numero = int(input("digite o terceiro numero:"))

soma = primeiro_numero + segundo_numero

if soma > terceiro_numero :
    print("é maior que terceiro_numero.")
else :
    print("é menor que terceiro_numero.")
