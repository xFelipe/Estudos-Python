data= input("Por favor, entre com uma data formato dd/mm/aaaa:")
mes=''
if data.split('/')[1]=='01':
    mes='Janeiro'
elif data.split('/')[1]=='02':
    mes='Fevereiro'
elif data.split('/')[1]=='03':
    mes='Março'
elif data.split('/')[1]=='04':
    mes='Abril'
elif data.split('/')[1]=='05':
    mes='Maio'
elif data.split('/')[1]=='06':
    mes='Junho'
elif data.split('/')[1]=='07':
    mes='Julho'
elif data.split('/')[1]=='08':
    mes='Agosto'
elif data.split('/')[1]=='09':
    mes='Setembro'
elif data.split('/')[1]=='10':
    mes='Outubro'
elif data.split('/')[1]=='11':
    mes='Novembro'
elif data.split('/')[1]=='12':
    mes='Dezembro'
else:
    print('Valor do mês incrompreendido, processo parado')
    
print ("A data informada é %s de %s de %s"%(data.split('/')[0],mes, data.split('/')[2]))
