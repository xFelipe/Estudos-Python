import random

x= random.randint(1,100)
print (x)

nomes = ["fulano","ciclano","beltrano","garibalda","gilbernarsom"]
print ('Nome aleatório gerado:', random.choice(nomes))
print ('Nomes em ordem normal:', nomes)
random.shuffle(nomes)
print("o comando usado acima modificou as posições dos nomes de forma aleatória, dentro da variável, e não deu saida")
print (nomes)
