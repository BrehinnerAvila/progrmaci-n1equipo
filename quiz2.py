import math
gasto_persona = 150
personas = 80
# Consumo total diario y anual
consumo_totaldiario = gasto_persona * personas
print("se consume",consumo_totaldiario, "L diarios aproximadamente")
consumo_totalanual = consumo_totaldiario * 365
print("se consume",consumo_totalanual, "L anuales")
# Reserva mantenimiento
dias_mantenimiento = 10
reserva_mantenimiento = consumo_totaldiario * dias_mantenimiento
#no  se pide imprimir este dato
# Capacidad del tanque 
capacidad_tanque = 10000
eficiencia = 0.9  # 90%
capacidad_util_tanque = capacidad_tanque * eficiencia
print("La capacidad útil de cada tanque es:", capacidad_util_tanque, "L")
# Tanques necesarios 
tanques_necesarios = math.ceil(reserva_mantenimiento / capacidad_util_tanque)
print("Los tanques necesarios para cubrir la reserva son:", tanques_necesarios)
#area de tanques
area_por_tanque=2.5 
area_total_tanques=area_por_tanque*tanques_necesarios
print("el arera necesaria para instalar todos los tanques necesarios es de ",area_total_tanques,"m cuadrados")



