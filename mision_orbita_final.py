# ==============================================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Roberto Ulate Antonieta, María Fernanda Loría Campos, Sofía Cabas Madrigal
# Fecha: 18/11/2026 Versión: 1.0
# Descripción: Sistema integrado Misión Órbita. Administra el ciclo completo
#              de misiones espaciales (planificación, autorización, viaje de ida,
#              exploración científica, regreso o supervivencia, reporte final,
#              historial, búsqueda y estadísticas) para grupo de 3 integrantes.
# ==============================================================================

# Declaración de constantes estructurales y tuplas fijas
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))

# Cada actividad: (nombre, combustible, energía, provisiones, puntos)
ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# Constantes de posición para columnas de DESTINOS: (nombre, dias)
DES_NOMBRE = 0
DES_DIAS = 1

# Constantes de posición para columnas de ACTIVIDADES: (nombre, combustible, energía, provisiones, puntos)
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Constantes de posición para listas recursos, requeridos y consumo
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Constantes de posición para columnas de la matriz bitacora: [numero, actividad, puntos]
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Constantes de posición para columnas de la matriz historial: [numero, nombre, destino, resultado, puntos]
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes numéricas de consumo, trayectos y reservas
TRAYECTOS_MISION = 2
CONSUMO_DIARIO_COMBUSTIBLE = 8
CONSUMO_DIARIO_OXIGENO = 2
CONSUMO_DIARIO_ENERGIA = 5
CONSUMO_DIARIO_PROVISIONES = 1
RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10

# Constantes de opciones de menú principal (grupo de 3 integrantes)
OPCION_MENU_PLANIFICAR = 1
OPCION_MENU_HISTORIAL = 2
OPCION_MENU_BUSCAR = 3
OPCION_MENU_ESTADISTICAS = 4
OPCION_MENU_SALIR = 5
ACTIVIDAD_OBJETIVO_MUESTRA = "Recolectar muestra"
DECIMALES_PROMEDIO = 2


# Muestra los destinos disponibles con su duración de viaje de ida
def mostrar_destinos():
    # Recorrido de la tupla DESTINOS mediante índice para numerar desde 1
    print("Destinos disponibles:")
    for i in range(len(DESTINOS)):
        destino = DESTINOS[i]
        print(str(i + 1) + ". " + destino[DES_NOMBRE] + " (" + str(destino[DES_DIAS]) + " días)")


# Solicita al usuario las cantidades disponibles de cada recurso en el orden de RECURSOS
def leer_recursos():
    # Inicialización de lista vacía para almacenar las 4 entradas
    disponibles = []
    for recurso in RECURSOS:
        cantidad = int(input("Cantidad disponible de " + recurso + ": "))
        disponibles.append(cantidad)
    return disponibles


# Calcula los recursos totales requeridos para ida, regreso y reservas
def calcular_requeridos(dias_viaje, tripulantes):
    # Cálculo según fórmulas establecidas utilizando constantes nombradas
    combustible_req = dias_viaje * CONSUMO_DIARIO_COMBUSTIBLE * TRAYECTOS_MISION + RESERVA_COMBUSTIBLE
    oxigeno_req = dias_viaje * CONSUMO_DIARIO_OXIGENO * TRAYECTOS_MISION * tripulantes + OXIGENO_EMERGENCIA
    energia_req = dias_viaje * CONSUMO_DIARIO_ENERGIA * TRAYECTOS_MISION + ENERGIA_EXPLORACION
    provisiones_req = dias_viaje * tripulantes * TRAYECTOS_MISION + PROVISIONES_ADICIONALES
    requeridos = [combustible_req, oxigeno_req, energia_req, provisiones_req]
    return requeridos


# Muestra el resumen de planificación y evalúa el margen adicional de combustible
def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, disponibles, requeridos):
    # Salida de datos generales de la misión
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)

    # Comparación recurso por recurso usando capitalize()
    for i in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[i].capitalize()
        print(nombre_recurso + ": disponible " + str(disponibles[i]) + " | requerido " + str(requeridos[i]))

    # Cálculo y verificación del margen adicional de combustible
    margen = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print("Margen adicional de combustible:", margen, "unidades")
    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


# Verifica si todos los recursos disponibles son mayores o iguales a los requeridos
def autorizar_lanzamiento(disponibles, requeridos):
    # Variable booleana que determina si todos los recursos cumplen
    autorizado = True
    for i in range(len(RECURSOS)):
        if disponibles[i] < requeridos[i]:
            autorizado = False

    # Muestra el resultado de la evaluación
    if autorizado:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")
    return autorizado


# Calcula el consumo diario de cada recurso según la cantidad de tripulantes
def calcular_consumo_diario(tripulantes):
    # Construcción de la lista de consumo diario en el orden de RECURSOS
    consumo = [
        CONSUMO_DIARIO_COMBUSTIBLE,
        CONSUMO_DIARIO_OXIGENO * tripulantes,
        CONSUMO_DIARIO_ENERGIA,
        CONSUMO_DIARIO_PROVISIONES * tripulantes
    ]
    return consumo


# Verifica si los recursos actuales alcanzan para cubrir un día de consumo
def recursos_alcanzan(recursos, consumo):
    # Recorrido de los cuatro recursos para comprobar disponibilidad diaria
    alcanzan = True
    for i in range(len(RECURSOS)):
        if recursos[i] < consumo[i]:
            alcanzan = False
    return alcanzan


# Simula un trayecto día a día descontando el consumo diario si los recursos alcanzan
def simular_trayecto(recursos, dias, tripulantes):
    # Inicialización de consumo diario, contador de días y bandera de control
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True

    # Ciclo controlado por condición sin uso de break
    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            for i in range(len(RECURSOS)):
                recursos[i] = recursos[i] - consumo[i]
            dias_completados = dias_completados + 1
            print(
                "Día " + str(dias_completados) +
                " | Combustible: " + str(recursos[COMBUSTIBLE]) +
                " | Oxígeno: " + str(recursos[OXIGENO]) +
                " | Energía: " + str(recursos[ENERGIA]) +
                " | Provisiones: " + str(recursos[PROVISIONES])
            )
        else:
            puede_continuar = False

    return dias_completados


# Muestra las unidades restantes de cada recurso
def mostrar_recursos(recursos):
    # Listado ordenado según la tupla RECURSOS
    print("Recursos restantes:")
    for i in range(len(RECURSOS)):
        print("- " + RECURSOS[i].capitalize() + ": " + str(recursos[i]) + " unidades")


# Muestra el menú de actividades científicas y la opción para finalizar
def mostrar_menu_actividades():
    # Recorrido de ACTIVIDADES numerando desde 1 y agregando opción de salida
    for i in range(len(ACTIVIDADES)):
        actividad = ACTIVIDADES[i]
        print(str(i + 1) + ". " + actividad[ACT_NOMBRE])
    opcion_salir = len(ACTIVIDADES) + 1
    print(str(opcion_salir) + ". Finalizar exploración")


# Administra el ciclo de actividades científicas en el destino y registra la bitácora
def explorar(recursos):
    # Inicialización de bitácora vacía, opción de salida y variable de control
    bitacora = []
    opcion_finalizar = len(ACTIVIDADES) + 1
    exploracion_activa = True

    while exploracion_activa:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))

        if opcion == opcion_finalizar:
            print("Exploración finalizada por la tripulación.")
            exploracion_activa = False
        elif opcion < 1 or opcion > len(ACTIVIDADES):
            print("Opción no válida.")
        else:
            actividad = ACTIVIDADES[opcion - 1]
            # Verificación de combustible, energía y provisiones para la actividad
            if (recursos[COMBUSTIBLE] >= actividad[ACT_COMBUSTIBLE] and
                    recursos[ENERGIA] >= actividad[ACT_ENERGIA] and
                    recursos[PROVISIONES] >= actividad[ACT_PROVISIONES]):
                recursos[COMBUSTIBLE] = recursos[COMBUSTIBLE] - actividad[ACT_COMBUSTIBLE]
                recursos[ENERGIA] = recursos[ENERGIA] - actividad[ACT_ENERGIA]
                recursos[PROVISIONES] = recursos[PROVISIONES] - actividad[ACT_PROVISIONES]

                numero_registro = len(bitacora) + 1
                bitacora.append([numero_registro, actividad[ACT_NOMBRE], actividad[ACT_PUNTOS]])
                print("Actividad realizada: " + actividad[ACT_NOMBRE] + ". Puntos obtenidos: " + str(actividad[ACT_PUNTOS]))
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_activa = False

    return bitacora


# Cuenta cuántas veces aparece una actividad específica en la bitácora
def contar_actividad(bitacora, nombre_actividad):
    # Uso de contador explícito recorriendo las filas de bitacora
    contador = 0
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            contador = contador + 1
    return contador


# Suma el total de puntos científicos registrados en la bitácora
def calcular_puntos(bitacora):
    # Uso de acumulador explícito recorriendo las filas de bitacora
    total_puntos = 0
    for fila in bitacora:
        total_puntos = total_puntos + fila[BIT_PUNTOS]
    return total_puntos


# Muestra el resumen estadístico de la exploración y los recursos restantes
def mostrar_resumen_exploracion(bitacora, recursos):
    # Cálculo de métricas de exploración
    cantidad_actividades = len(bitacora)
    muestras = contar_actividad(bitacora, ACTIVIDAD_OBJETIVO_MUESTRA)
    total_puntos = calcular_puntos(bitacora)

    print("Actividades realizadas:", cantidad_actividades)
    print("Muestras recolectadas:", muestras)
    print("Puntos científicos:", total_puntos)
    mostrar_recursos(recursos)


# Determina si el combustible restante alcanza para cubrir el viaje de regreso
def puede_regresar(recursos, dias_viaje):
    # Evaluación sin considerar la reserva de emergencia
    combustible_necesario = dias_viaje * CONSUMO_DIARIO_COMBUSTIBLE
    suficiente = recursos[COMBUSTIBLE] >= combustible_necesario
    return suficiente


# Calcula los días completos de supervivencia por cada recurso vital
def calcular_supervivencia(recursos, tripulantes):
    # División entera en el orden de RECURSOS_VITALES: oxígeno, energía, provisiones
    dias_oxigeno = recursos[OXIGENO] // (tripulantes * CONSUMO_DIARIO_OXIGENO)
    dias_energia = recursos[ENERGIA] // CONSUMO_DIARIO_ENERGIA
    dias_provisiones = recursos[PROVISIONES] // (tripulantes * CONSUMO_DIARIO_PROVISIONES)
    dias_por_recurso = [dias_oxigeno, dias_energia, dias_provisiones]
    return dias_por_recurso


# Obtiene los nombres de los recursos vitales que igualan el valor mínimo de días
def obtener_limitantes(dias_por_recurso, minimo):
    # Recorrido paralelo con RECURSOS_VITALES para detectar empates
    limitantes = []
    for i in range(len(dias_por_recurso)):
        if dias_por_recurso[i] == minimo:
            limitantes.append(RECURSOS_VITALES[i])
    return limitantes


# Administra el retorno a la Tierra o el cálculo de supervivencia si queda varada
def regresar(recursos, dias_viaje, tripulantes):
    # Evaluación inicial de combustible para emprender el regreso
    if puede_regresar(recursos, dias_viaje):
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = RESULTADOS[0]
        else:
            dia_interrupcion = dias_completados + 1
            print("El regreso se interrumpió en el día " + str(dia_interrupcion) + ".")
            consumo = calcular_consumo_diario(tripulantes)
            for i in range(len(RECURSOS)):
                if recursos[i] < consumo[i]:
                    print("Recurso insuficiente:", RECURSOS[i])
            print("La tripulación no completó el regreso.")
            resultado = RESULTADOS[1]
    else:
        print("La tripulación quedó varada en el destino.")
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)
        for i in range(len(RECURSOS_VITALES)):
            print("Días por " + RECURSOS_VITALES[i] + ": " + str(dias_por_recurso[i]))
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        print("Supervivencia estimada:", minimo, "días")
        print("Recurso(s) limitante(s):", ", ".join(limitantes))
        resultado = RESULTADOS[2]

    return resultado


# Devuelve los puntos de una fila de la bitácora (clave de ordenamiento)
def obtener_puntos_actividad(fila):
    return fila[BIT_PUNTOS]


# Devuelve una nueva matriz bitácora ordenada de mayor a menor puntaje
def ordenar_bitacora(bitacora):
    bitacora_ordenada = sorted(bitacora, key=obtener_puntos_actividad, reverse=True)
    return bitacora_ordenada


# Muestra el reporte final de la misión y la bitácora ordenada
def mostrar_reporte(mision, bitacora):
    # Impresión de los datos resumen de la misión
    print("=== REPORTE FINAL ===")
    print("Misión:", mision[MIS_NOMBRE])
    print("Destino:", mision[MIS_DESTINO])
    print("Resultado:", mision[MIS_RESULTADO])
    print("Puntos científicos:", mision[MIS_PUNTOS])
    print("Bitácora de exploración (de mayor a menor puntaje):")

    if len(bitacora) == 0:
        print("Sin actividades registradas.")
    else:
        bitacora_ordenada = ordenar_bitacora(bitacora)
        for fila in bitacora_ordenada:
            print("#" + str(fila[BIT_NUMERO]) + " " + fila[BIT_ACTIVIDAD] + " - " + str(fila[BIT_PUNTOS]) + " puntos")


# Ejecuta el ciclo completo de una misión desde la planificación hasta el reporte final
def ejecutar_mision(numero):
    # Fase 1: Planificación inicial y selección de destino
    print("=== PLANIFICACIÓN ===")
    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))
    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))

    bitacora = []
    puntos = 0

    if opcion_destino < 1 or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
        nombre_destino = "Ninguno"
        resultado = RESULTADOS[4]
    else:
        destino = DESTINOS[opcion_destino - 1]
        nombre_destino = destino[DES_NOMBRE]
        dias_viaje = destino[DES_DIAS]

        # Lectura de recursos y evaluación de autorización
        recursos = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, recursos, requeridos)

        if autorizar_lanzamiento(recursos, requeridos):
            # Fase 2: Viaje de ida día a día (alcance grupo de 3 personas)
            print("=== VIAJE DE IDA ===")
            simular_trayecto(recursos, dias_viaje, tripulantes)
            print("La nave llegó a " + nombre_destino + " en " + str(dias_viaje) + " días.")
            mostrar_recursos(recursos)

            # Fase 3: Exploración científica en destino
            print("=== EXPLORACIÓN ===")
            bitacora = explorar(recursos)
            mostrar_resumen_exploracion(bitacora, recursos)
            puntos = calcular_puntos(bitacora)

            # Fase 4: Regreso o supervivencia
            print("=== REGRESO ===")
            resultado = regresar(recursos, dias_viaje, tripulantes)
        else:
            resultado = RESULTADOS[3]

    # Fase 5: Registro y reporte final de la misión
    mision = [numero, nombre_mision, nombre_destino, resultado, puntos]
    mostrar_reporte(mision, bitacora)
    return mision


# Muestra el menú principal del sistema para grupos de 3 integrantes
def mostrar_menu_principal():
    print("===== MISIÓN ÓRBITA =====")
    print("1. Planificar y ejecutar una misión")
    print("2. Ver historial de misiones")
    print("3. Buscar misión por nombre")
    print("4. Ver estadísticas")
    print("5. Salir")


# Devuelve los puntos de una fila de misión (clave de ordenamiento)
def obtener_puntos_mision(mision):
    return mision[MIS_PUNTOS]


# Devuelve una nueva matriz historial ordenada de mayor a menor puntaje
def ordenar_historial(historial):
    historial_ordenada = sorted(historial, key=obtener_puntos_mision, reverse=True)
    return historial_ordenada


# Formatea una fila de misión en una línea de texto estándar
def linea_mision(mision):
    texto = (
        "#" + str(mision[MIS_NUMERO]) + " " + mision[MIS_NOMBRE] +
        " | " + mision[MIS_DESTINO] +
        " | " + mision[MIS_RESULTADO] +
        " | " + str(mision[MIS_PUNTOS]) + " puntos"
    )
    return texto


# Muestra el historial de misiones ordenado por puntaje descendente
def mostrar_historial(historial):
    print("=== HISTORIAL DE MISIONES ===")
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        historial_ordenado = ordenar_historial(historial)
        for mision in historial_ordenado:
            print(linea_mision(mision))


# Extrae los nombres de todas las misiones del historial en orden de registro
def obtener_nombres(historial):
    nombres = []
    for mision in historial:
        nombres.append(mision[MIS_NOMBRE])
    return nombres


# Busca una misión por su nombre exacto utilizando in e index()
def mostrar_busqueda(historial):
    nombre_buscado = input("Nombre de la misión a buscar: ")
    nombres = obtener_nombres(historial)
    if nombre_buscado in nombres:
        posicion = nombres.index(nombre_buscado)
        mision_encontrada = historial[posicion]
        print("Misión encontrada:", linea_mision(mision_encontrada))
    else:
        print("No se encontró ninguna misión con el nombre:", nombre_buscado)


# Calcula y muestra las estadísticas generales del historial de misiones
def mostrar_estadisticas(historial):
    print("=== ESTADÍSTICAS ===")
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        total_misiones = len(historial)
        print("Total de misiones:", total_misiones)

        # Conteo de misiones por cada tipo de resultado posible
        for resultado_posible in RESULTADOS:
            contador_resultado = 0
            for mision in historial:
                if mision[MIS_RESULTADO] == resultado_posible:
                    contador_resultado = contador_resultado + 1
            print(resultado_posible + ": " + str(contador_resultado))

        # Acumulación de puntos para cálculo de promedio
        suma_puntos = 0
        for mision in historial:
            suma_puntos = suma_puntos + mision[MIS_PUNTOS]

        promedio = round(suma_puntos / total_misiones, DECIMALES_PROMEDIO)
        print("Promedio de puntos:", promedio)

        # Identificación de la misión con mayor puntaje mediante ordenamiento
        historial_ordenado = ordenar_historial(historial)
        mejor_mision = historial_ordenado[0]
        print(
            "Misión con más puntos: #" + str(mejor_mision[MIS_NUMERO]) + " " +
            mejor_mision[MIS_NOMBRE] + " (" + str(mejor_mision[MIS_PUNTOS]) + " puntos)"
        )


# Función principal que controla el ciclo del menú del sistema
def main():
    # Inicialización del historial vacío y bandera de control del programa
    historial = []
    sistema_activo = True

    while sistema_activo:
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))

        if opcion == OPCION_MENU_PLANIFICAR:
            numero_mision = len(historial) + 1
            nueva_mision = ejecutar_mision(numero_mision)
            historial.append(nueva_mision)
        elif opcion == OPCION_MENU_HISTORIAL:
            mostrar_historial(historial)
        elif opcion == OPCION_MENU_BUSCAR:
            mostrar_busqueda(historial)
        elif opcion == OPCION_MENU_ESTADISTICAS:
            mostrar_estadisticas(historial)
        elif opcion == OPCION_MENU_SALIR:
            sistema_activo = False
        else:
            print("Opción no válida.")

    print("Fin del sistema Misión Órbita.")


main()