s='um tigre, dois tigres, três tigres'
print (s)
print (s.find('tigre'))
print (s.find('tigre',4))
print (s.find('tigre',16))
print ('este comando expôs onde no texto está a string buscada, e na segunda e terceira tentativa, foi colocado um "começo" para esta busca. No caso começar a busca A PARTIR do caracter 4 e 16')

print (s.replace ('tigre','gato'))
print (s)
