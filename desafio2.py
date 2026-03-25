#permite o usuario a escolher um numero

numero = int(input("escolha um numero aleatório:  "))

#se o numero escolhido pelo usuario a '% 2' dele for igual 0 mostra que é um numero par, se diferente de 0 é impar

if  numero % 2 == 0:
    print("esse numero é par")
else:
    print("esse numero numero é impar")
