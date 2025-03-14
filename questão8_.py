import os
os.system ("clear")

cd = str(input("digite a cor do cd: "))

match cd:
  
  case "verde":
    print("R$10,00")
  case "azul":
    print("20,00")
  case "amarelo":
    print("40,00")
  case _:
    print ("opção invalida")  