#pede para usuario informar os segundos
segundos = int(input("fale a quantidade de segundos"))

#converte segundos em minutos
minutos = (segundos / 60)

#converte os segundos em hroas
horas = (segundos / 3600)

#mostra o resultado das operações
print("essa quantidade de segundos resulta em", horas,"horas", "ou", minutos, "minutos ou continua sendo", segundos, "segundos")

##pede para usuario informar as horas
h = int(input("fale quantas horas"))

#converte as horas em segundos
s = (h * 3600)

#converte as horas em minutos
m = (h * 60)

print("essa quantidade de horas resulta em", h,"horas", "ou", m, "minutos ou continua sendo", s, "segundos")
