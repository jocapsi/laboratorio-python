segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
final_segs_restantes = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", final_segs_restantes, "segundos.")
