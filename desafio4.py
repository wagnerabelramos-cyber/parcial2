# pede ao usuario que escolha os numeros desejados
n1 = float(input("escolha um numero "))
n2 = float(input("escolha outro numero "))

#pede ao usuario que escolha a operação desejada
operação = input("escolha uma operação [soma, subtração, divisão ou multiplicação]")

# faz a operação de soma com os numeros escolhidos
if operação == "soma":
    print(n1 + n2)
# faz a operação de subtração com os numeros escolhidos
elif operação == "subtração":
    print(n1-n2)
# faz a operação de multiplicação com os numeros escolhidos
elif operação == "multiplicação":
    print(n1*n2)
# faz a operação de divisão com os numeros escolhidos
elif operação == "divisão":
    print(n1/n2)
#caso seja uma operação q não faça sentido diz 'esse numero não existe'
else: 
    print('esse numero não existe')
