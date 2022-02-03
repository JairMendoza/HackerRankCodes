import math
ejemplo = [23,69,12,61,50,84,3]
calificacionesRedondeadas = []
print(69 % 5)
for i in ejemplo:
    if i <= 35:
        calificacionesRedondeadas.append(i)
    elif i % 5 >=3:
        calificacion = math.ceil(i / 5) * 5
        calificacionesRedondeadas.append((calificacion)) 
        #print(calificacion)
    elif i % 5 <3:
        calificacionesRedondeadas.append(i)
        
print(calificacionesRedondeadas)