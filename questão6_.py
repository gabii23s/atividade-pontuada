import os
os.system ("clear")

primeira_nota = float(input ("digite a primeira nota:"))
segunda_nota = float(input( "digite a segunda nota:"))

media = ( primeira_nota + segunda_nota ) / 2

print (f"média: (media)")
if media >= 6 :
    print ("parábens você foi aprovado!")
elif media <= 4 :
    print (" você está em recuperação!")
else:
    print("você foi reprovado!")