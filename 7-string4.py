print ('Programa que leia uma palavra e troque as vogais por "*"')

palavra = input("Palavra: ")
cont=0
troca = ""
while cont < len(palavra):
    if palavra[cont] in "aeiou":
        troca=troca+("*")
    else:
        troca=troca+palavra[cont]
    cont=cont+1
print ("Nova palavra:%s"%troca)
