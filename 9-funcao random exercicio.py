
def embaralha(x):
    import random
    x=list(x)
    random.shuffle(x)
    return x

import random
lista = []
for cont in range(15):
    lista.append(random.randint(10,1000))
print (lista)
