# ============================================================
# Archivo: Ejercicio1Proyecto.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Sofía Cabas, Maria Fernanda Loria y Roberto Alonso Ulate 
# Fecha: 10/10/2026 Versión: 1.0
# Descripción: Cálculo los recursos necesarios para una misión.
# ============================================================

# Entrada de datos

nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
cantidad_dias_de_viaje = int(input("Ingrese cantidad de días estimados para llegar al destino: "))

# Declaración de la constante reserva.

# Toda misión debe transportar 10 unidades adicionales de combustible para emergencias.

RESERVA_COMBUSTIBLE = 10

# Procesameintos:

# Por cada día durane el viaje de ida y regreso (ya que duran lo mismo) se consumen 8 unidades de combustible.

combustible_ida = cantidad_dias_de_viaje * 8
combustible_regreso = cantidad_dias_de_viaje * 8
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Cada tripulante consume 2 unidades de oxígeno por día durante el viaje de ida y regreso. Además, se agregan 5 unidades de emergencia.

oxigeno_requerido =  cantidad_dias_de_viaje * 2 * 2 * cantidad_tripulantes + 5

# La nave consume 5 unidades de energía por día durante el viaje de ida y regreso. Además, de 10 unidades para las operaciones de exploración.

energia_requerida =  cantidad_dias_de_viaje * 5 * 2 + 10

# cada tripulante consume 1 unidad de provisiones por día durante el viaje de ida y regreso. Además, se agregan 3 unidades adicionales.

provisiones_requeridas = cantidad_dias_de_viaje * cantidad_tripulantes * 2 + 3

# Salida de resultados

print("Combustible de ida:", combustible_ida, "unidades")
print("Combustible de regreso:", combustible_regreso, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible de reserva:", RESERVA_COMBUSTIBLE, "unidades")

print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")

# ============================================================
# Archivo: Ejercicio2Proyecto.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Sofía Cabas, Maria Fernanda Loria y Roberto Alonso Ulate 
# Fecha: 12/10/2026 Versión: 1.0
# Descripción: Verificación de combustible
# ============================================================

# Entrada de datos 

combustible_disponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustible_requerida_viaje_ida = int(input("Ingrese la cantidad requerida de combustible para el viaje de ida: "))
combustible_requerida_viaje_regreso = int(input("Ingrese la cantidad requerida de combustible para el viaje de regreso: "))

# Declaración de la constante reserva.

# Toda misión debe transportar 10 unidades adicionales de combustible para emergencias.

RESERVA_COMBUSTIBLE = 10

# Procesamientos:

#El combustible total requerido para completar la misión incluye el viaje de ida, el viaje de regreso y una reserva de emergencia de 10 unidades.

combustible_total = combustible_requerida_viaje_ida + combustible_requerida_viaje_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Condición:

# Si el combustible adicional es menor a 10, eneseñar una advertencia de que el margen adicional es bajo pero si no es bajo no se va a mostrar la advertencia

if combustible_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo, ya que es de:", combustible_adicional, "unidades")

else:
    print("El margen de combustible adicional es de:", combustible_adicional, "unidades")

# Salidas de resultados

print("Combustible total requerido:", combustible_total, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")

"""

Ejercicio numero 3
Descripción: Verifica si la nave cuenta con suficientes recursos de oxígeno y provisiones para la tripulación.
"""

# Entrada de datos
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# Procesamiento y decisiones (Estructura condicional doble if/else)
# Se evalúa que ambos recursos cumplan con el mínimo necesario sin indicar cuál falló específicamente.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    resultado = "La nave posee recursos suficientes para la tripulación."
else:
    resultado = "La nave no posee recursos suficientes para la tripulación."

# Salida de resultados
print(resultado)

# ==============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate 
# Fecha: 12/10/2026
# Versión: 1.0
# Descripción: Realiza la verificación general de recursos y 
#              determina la autorización inicial de lanzamiento.
# ==============================================================

# Declaración de constantes
reserva_combustible = 10

# Entrada de datos por consola
print("--- SISTEMA DE AUTORIZACIÓN DE LANZAMIENTO ---")
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_llegada = int(input("Ingrese el combustible requerido para llegar: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))

energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# Procesamiento: cálculo del combustible total requerido con reserva
combustible_total_requerido = combustible_llegada + combustible_regreso + reserva_combustible

# Decisión: verificación condicional doble de todas las condiciones simultáneas
if (combustible_disponible >= combustible_total_requerido and 
    oxigeno_disponible >= oxigeno_requerido and 
    energia_disponible >= energia_requerida and 
    provisiones_disponibles >= provisiones_requeridas):
    
    # Salida por cumplimiento de condiciones
    print("Lanzamiento autorizado.")
else:
    # Salida por incumplimiento de alguna condición
    print("Lanzamiento no autorizado. La misión debe ser revisada.")

# ==============================================================================
# Archivo: ejercicio5_destino.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate
# Fecha: 08/11/2026 Versión: 1.0
# Descripción: Selecciona el destino de la misión, calcula recursos requeridos
#              mediante condicionales múltiples y anidadas, y autoriza el lanzamiento.
# ==============================================================================

# Declaración de constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos iniciales
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
opcion_destino = int(input("Seleccione el destino (1: Luna, 2: Marte, 3: Europa): "))

# 1. Validación de la opción de destino
if opcion_destino < 1 or opcion_destino > 3:
    print("Opción de destino no válida. La misión no puede planificarse.")
else:
    # 2. Duración del viaje según la opción (Condicional múltiple)
    if opcion_destino == 1:
        nombre_destino = "Luna"
        dias_viaje = 3
    elif opcion_destino == 2:
        nombre_destino = "Marte"
        dias_viaje = 5
    else:
        nombre_destino = "Europa"
        dias_viaje = 7

    # Solicitud de recursos disponibles (solo si la opción es válida)
    combustible_disponible = int(input("Ingrese el combustible disponible: "))
    oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
    energia_disponible = int(input("Ingrese la energía disponible: "))
    provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

    # 3. Cálculo de recursos requeridos
    combustible_ida = dias_viaje * 8
    combustible_regreso = dias_viaje * 8
    combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = dias_viaje * 2 * 2 * tripulantes + 5
    energia_requerida = dias_viaje * 5 * 2 + 10
    provisiones_requeridas = dias_viaje * tripulantes * 2 + 3

    # Salidas obligatorias: Resumen de la misión
    print()
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)
    print("Combustible disponible:", combustible_disponible, "| requerido:", combustible_total_requerido, "unidades")
    print("Oxígeno disponible:", oxigeno_disponible, "| requerido:", oxigeno_requerido, "unidades")
    print("Energía disponible:", energia_disponible, "| requerida:", energia_requerida, "unidades")
    print("Provisiones disponibles:", provisiones_disponibles, "| requeridas:", provisiones_requeridas, "unidades")

    # 4. Autorización de la misión (Condicional anidada)
    if combustible_disponible >= combustible_total_requerido and oxigeno_disponible >= oxigeno_requerido and energia_disponible >= energia_requerida and provisiones_disponibles >= provisiones_requeridas:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")

# ==============================================================================
# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate
# Fecha: 08/11/2026 Versión: 1.0
# Descripción: Simula día a día el viaje hacia el destino validando recursos
#              disponibles antes de cada consumo, sin utilizar break ni funciones.
# ==============================================================================

# Declaración de constantes de consumo diario fijo
CONSUMO_COMBUSTIBLE = 8
CONSUMO_ENERGIA = 5

# Entrada de datos
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# Inicialización de variables de control y contadores
dia_actual = 1
viaje_activo = True

# Ciclo para simular el paso de los días
while viaje_activo and dia_actual <= dias_viaje:
    # Cálculo del consumo diario dependiente de los tripulantes
    consumo_oxigeno_diario = 2 * tripulantes
    consumo_provisiones_diario = 1 * tripulantes

    # 1. Verificar antes del consumo si todos los recursos alcanzan
    if combustible >= CONSUMO_COMBUSTIBLE and oxigeno >= consumo_oxigeno_diario and energia >= CONSUMO_ENERGIA and provisiones >= consumo_provisiones_diario:
        # 2. Descontar consumo y actualizar estado
        combustible = combustible - CONSUMO_COMBUSTIBLE
        oxigeno = oxigeno - consumo_oxigeno_diario
        energia = energia - CONSUMO_ENERGIA
        provisiones = provisiones - consumo_provisiones_diario

        print("Día", dia_actual, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
        
        # Incrementar contador de días
        dia_actual = dia_actual + 1
    else:
        # 3. Si algún recurso no alcanza, se detiene el viaje sin descontar el día
        viaje_activo = False

# Salidas obligatorias según el resultado del viaje
if dia_actual > dias_viaje:
    print()
    print("La nave llegó al destino en", dias_viaje, "días.")
    print("Combustible restante:", combustible, "unidades")
    print("Oxígeno restante:", oxigeno, "unidades")
    print("Energía restante:", energia, "unidades")
    print("Provisiones restantes:", provisiones, "unidades")
else:
    print()
    print("Viaje interrumpido en el día", dia_actual, ".")
    
    # Verificación de recursos insuficientes en orden estricto: combustible, oxígeno, energía, provisiones
    consumo_oxigeno_diario = 2 * tripulantes
    consumo_provisiones_diario = 1 * tripulantes

    if combustible < CONSUMO_COMBUSTIBLE:
        print("Recurso insuficiente: combustible")
    if oxigeno < consumo_oxigeno_diario:
        print("Recurso insuficiente: oxigeno")
    if energia < CONSUMO_ENERGIA:
        print("Recurso insuficiente: energia")
    if provisiones < consumo_provisiones_diario:
        print("Recurso insuficiente: provisiones")
        
    dias_completados = dia_actual - 1
    print("Días completados:", dias_completados)