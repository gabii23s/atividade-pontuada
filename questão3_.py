import os
os. system ("clear")

#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois.

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo nuemro: "))

if primeiro_numero == segundo_numero:
    soma = primeiro_numero + segundo_numero
    print("valor c:", soma)
else: 
    multiplicação =  primeiro_numero * segundo_numero
    print("valor c: ", multiplicação)