import math
def pregunta_1(radio: float, angulo: float) -> float:
    resultado = radio * angulo * math.pi/180
    return round(resultado,2)

print(pregunta_1(10,90))
print(pregunta_1(7,180))
print(pregunta_1(12,60))
print(pregunta_1(8,30))
#----------------------------------------------------------------
from math import sqrt
def pregunta_2(vx: float, vy: float, vz: float) -> float:
    solucion = sqrt(vx ** 2 + vy ** 2 + vz ** 2)
    return round(solucion,2)

print(pregunta_2(-1,-2,0))
print(pregunta_2(-2,5,1))
print(pregunta_2(4,8,3))
#----------------------------------------------------------------
def pregunta_3(edad: int) -> str:
   if edad < 13:
        return "Menor"
   elif edad >= 13 and edad < 18:
       return "Adolescente"
   elif edad >= 18 and edad < 65:
        return "Adulto"
   elif edad >= 65:
       return "Adulto Mayor"

print(pregunta_3(10))
print(pregunta_3(15))
print(pregunta_3(30))
print(pregunta_3(70))
#----------------------------------------------------------------
def pregunta_4(peso: int, altura: float) -> str:
    IMC = peso / (altura * altura)
    if IMC < 18.5:
        return "Bajo peso"
    elif IMC >= 18.5 and IMC < 25:
        return "Normal"
    elif IMC >= 25 and IMC < 30:
        return "Sobrepeso"
    elif IMC >= 30:
        return "Obesidad"

print(pregunta_4(50, 1.60))
print(pregunta_4(45, 1.75))
print(pregunta_4(80, 1.50))
print(pregunta_4(70, 1.80))
