import math
gasto_persona = float(input("ingrese el gasto de consumo de agua por persona"))
personas = int(input("ingrese el numero de personas que gastan agua"))
# Consumo total diario y anual
consumo_totaldiario = gasto_persona * personas
print("se consume",consumo_totaldiario, "L diarios aproximadamente")
consumo_totalanual = consumo_totaldiario * 365
print("se consume",consumo_totalanual, "L anuales")
# Reserva mantenimiento
dias_mantenimiento = int(input("ingrese los dias que se demoran haciendo el mantenimiento"))
reserva_mantenimiento = consumo_totaldiario * dias_mantenimiento
#no  se pide imprimir este dato
# Capacidad del tanque 
capacidad_tanque = float(input("ingrese la capacidad que tiene el tanque"))
eficiencia = float(input("ingrese el porcentaje de eficiencia en decimal 0-1")) 
capacidad_util_tanque = capacidad_tanque * eficiencia
print("La capacidad útil de cada tanque es:", capacidad_util_tanque, "L")
# Tanques necesarios 
tanques_necesarios = math.ceil(reserva_mantenimiento / capacidad_util_tanque)
print("Los tanques necesarios para cubrir la reserva son:", tanques_necesarios)
#area de tanques
area_por_tanque=float(input("ingrese el area que tiene cada tanque"))
area_total_tanques=area_por_tanque*tanques_necesarios
print("el arera necesaria para instalar todos los tanques necesarios es de ",area_total_tanques,"m cuadrados")
#autonomia de dias 
autonomia_dias = (capacidad_util_tanque * tanques_necesarios) / consumo_totaldiario
print("los dias de autonomia que tiene este sistema son:",autonomia_dias)
#sequia
litros_persona_sequia = (capacidad_util_tanque * tanques_necesarios) / (personas * 30)
print("Cada persona podría recibir",litros_persona_sequia, "litros  en caso de una sequia de 30 dias")



