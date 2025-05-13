import math

def verificar_cedula(cedula=""):
    if len(cedula) != 10:
        raise Exception("Error numero de cedula incompleto")
    
    ced_array = [int(d) for d in cedula[:9]]
    ultimo_digito = int(cedula[9])
    multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    
    resultado = []
    for i, (digito, mult) in enumerate(zip(ced_array, multiplicador)):
        producto = digito * mult
        resultado.append(producto - 9 if producto >= 10 else producto)
    
    suma = sum(resultado)
    siguiente_decena = math.ceil(suma / 10) * 10
    complemento = siguiente_decena - suma
    
    return ultimo_digito == complemento

# Prueba con la cédula proporcionada
print(verificar_cedula("3006628393"))