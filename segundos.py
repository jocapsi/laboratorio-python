segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

total_segs = int(segundos)

dias = total_segs // 86400
seg_restantesdias = total_segs % 86400
horas = seg_restantesdias // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
final_segs_restantes = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", final_segs_restantes, "segundos.")
