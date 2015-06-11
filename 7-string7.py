text='batatinha quando nasce'
print (text.split())
print (text.split()[0])
print (text.split()[1])
print (text.split()[2])

data='21/02/2015'
print (data.split('/'))
data=((data.split('/')[0])+'/'+(data.split('/')[1])+'/'+'2012')
print (data)
ip='198.188.10.144'
print (ip)
print (ip.split('.'))
print('\ncaracter nº 1 da casa nº 2):')
print (ip.split('.')[2][1])

ip=(ip.split('.'))
print (ip)
ip='/'.join(ip)
print (ip)
time=('vasco','flamengo','palmeiras')
print (', '.join(time))
print("o comando join, usada da forma acima, junta strings em uma, separando os textos com algo que a gente especifica, como feito acima")
