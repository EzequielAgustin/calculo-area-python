

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# El Usuario quiere saber cual es el área de un círculo teniendo el radio"
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

#------------------------
# Algoritmo
# -----------------------

# 1: Solicitar al usuario que ingrese el radio del círculo.
# 2: Vamos a calcular el área del círculo utilizando la fórmula área = pi * radio²  
# 3: Mostrar al usuario el área calculada

# -----------------------

#------------------------
# Pseudocódigo
# -----------------------

# Inicio
#  Paso 1: Solicitar al usuario que ingrese el radio del círculo.
#  Mostrar mensaje: "Por favor, ingrese el radio del círculo: "
#  Leer el dato ingresado y asignarlo a variable radio de tipo flotante

#  Paso 2: Calcular el área del círculo utilizando la fórmula area = pi * radio²
#  Definir y asignar a la variable area el resultado de pi * radio²

#  Paso 3: Mostrar al usuario el área calculada
#  Mostrar mensaje: "El área del círculo con radio", radio, "es:", area
# Fin

# -----------------------
# Diagrama de flujo adjunto
# -----------------------

import math

#  Paso 1: Solicitar al usuario que ingrese el radio del círculo.



radio = float(input("Por favor ingrese el radio del círculo: "))

#  Paso 2: Calcular el área del círculo utilizando la fórmula area = pi * radio²

area = math.pi * (radio**2)

#  Paso 3: Mostrar al usuario el área calculada

print("El área del círculo con radio", radio, "es:", area)