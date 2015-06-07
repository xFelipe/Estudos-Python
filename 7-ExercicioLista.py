vetor = []
contador = 0
n=int
while contador<=9:
    n=int(input("Diga um número"))
    vetor.append(n)
    contador=contador+1
contador=contador-1
while contador>=0:
    print ("O número armazenado na posição %i é o %f"%(contador, vetor[contador]))
    contador=contador-1
