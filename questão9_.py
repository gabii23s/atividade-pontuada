import os
os.system ("clear")

renda_mensal = float(input("digite sua renda mensal: "))
valor_emprestimo = float(input("digite o valor total do emprestimo desejado: "))
num_prestacoes = int(input("digite o número de prestações desejado: "))

prestacao_mensal = valor_emprestimo / num_prestacoes

if valor_emprestimo <= 10 * renda_mensal and prestacao_mensal <= 0.3 * renda_mensal:
    print("empréstimo APROVADO!")
else:
    print("empréstimo NEGADO!")