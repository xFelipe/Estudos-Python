min=int(input("Quantidade de minutos gastos é de:"))
if min<200:
    print ("A conta está no valor de R$:%6.2f" % (min*0.20))
else:
        if min<400:
            print ("A conta está no valor de R$:%6.2f" % (min*0.18))
        else:
                print ("A conta está no valor de R$:%6.2f" % (min*0.15))
