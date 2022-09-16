#------------ Tabla resultados----------------
entrada = "Datasets/results.json"
salida = "Datasets/results_formateado.json"

# Leer fichero completo
with open(entrada, "r",encoding='utf-8') as fichero:
    datos = fichero.read()

# Añadir coma al final de cada linea
datos = datos.replace("\n", ",\n")

# Volcar resultado a otro fichero
with open(salida, "w",encoding='utf-8') as fichero:
    fichero.write(datos)

#------------ Tabla pilotos----------------
entrada = "Datasets/drivers.json"
salida = "Datasets/drivers_formateado.json"

# Leer fichero completo
with open(entrada, "r",encoding='utf-8') as fichero:
    datos = fichero.read()

# Añadir coma al final de cada linea
datos = datos.replace("\n", ",\n")

# Volcar resultado a otro  fichero
with open(salida, "w",encoding='utf-8') as fichero:
    fichero.write(datos)

#------------ Tabla pilotos----------------
entrada = "Datasets/constructors.json"
salida = "Datasets/constructors_formateado.json"

# Leer fichero completo
with open(entrada, "r",encoding='utf-8') as fichero:
    datos = fichero.read()

# Añadir coma al final de cada linea
datos = datos.replace("\n", ",\n")

# Volcar resultado a otro (o el mismo) fichero
with open(salida, "w",encoding='utf-8') as fichero:
    fichero.write(datos)