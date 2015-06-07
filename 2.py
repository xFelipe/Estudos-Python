metq=int(input("Quantidade de metros quadrados da Área a ser pintada:"))
quantl=int(metq/54)
if metq % 54 != 0:
    quantl=quantl+1
print ("Você deverá comprar %i latas e isto custará:R$:%.2f"%(quantl,quantl*80))
