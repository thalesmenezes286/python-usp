segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

 # Calcula os dias e o resto
dias = segundos // (24 * 3600)
restantes = segundos % (24 * 3600)

# Calcula as horas e o resto
horas = restantes // 3600
restantes %= 3600

# Calcula os minutos e o resto
minutos = restantes // 60
segundos = restantes % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")