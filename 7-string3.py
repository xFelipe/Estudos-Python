texto = string(input("Forneça uma palavra para verificar se é uma palíndrome:\n"))
texto2 = texto[::-1]
if texto==texto2:
    print ("A palavra %s é uma palíndrome:\n"%texto)
else:
    print ("a palavra %s não é uma palíndrome\n"%texto)
