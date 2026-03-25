#pede para informar o capital

C = float(input("quanto de capital você possui?    "))

#pede para informar a taxa
I = float(input("quanto qual a taxa?    "))

#pede para informar o tempo
T = float(input("em quanto tempo?    "))

#usa a formula de juros simples

J = (C *I* T) / 100 

# mostra o resultado 
print(J)
