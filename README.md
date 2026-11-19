Sistema Integrado Misión Órbita

Descripción del proyecto

Simulador imperativo de exploración espacial desarrollado en Python para la asignatura SOFT-01 Principios de Programación 1 (Sección SCV6, Periodo 2026-C3, Universidad CENFOTEC). El programa integra el ciclo completo de gestión de misiones espaciales: planificación, cálculo de requerimientos, autorización de lanzamiento, simulación diaria de trayectos, exploración científica con registro en bitácora, evaluación de regreso o cálculo de supervivencia, generación de reportes finales ordenados, historial de misiones, búsqueda por nombre y estadísticas generales.

Integrantes del grupo (3 personas)

Roberto Ulate Antonieta

María Fernanda Loría Campos

Sofía Cabas Madrigal

Convenciones y estilos de programación utilizados

Paradigma imperativo estructurado: Modularización mediante funciones con parámetros y un único return al final de cada función que devuelve valor.

Estructuras de datos: Uso exclusivo de listas, tuplas y matrices (sin diccionarios, conjuntos, objetos ni librerías externas).

Nomenclatura: Variables y funciones en snake_case en minúscula; constantes globales al inicio del archivo en MAYÚSCULAS_CON_GUION_BAJO, incluyendo constantes de posición para evitar números mágicos.

Control de flujo: Ciclos terminados únicamente mediante sus condiciones lógicas (sin break, continue, exit() ni quit()), contadores y acumuladores explícitos, y ordenamiento mediante sorted() con funciones clave nombradas.

Formato y documentación: Indentación uniforme de 4 espacios, encabezado institucional completo y comentarios descriptivos por bloque lógico.

Instrucciones para ejecutar el sistema

Asegúrese de contar con Python 3 instalado en su equipo.

Abra una terminal en la carpeta avance3/ donde se ubica el archivo mision_orbita.py (o ábralo desde Visual Studio Code).

Ejecute el comando:

python mision_orbita.py


Siga las instrucciones en consola seleccionando las opciones numéricas del menú principal (1 a 5) e ingresando valores enteros positivos según lo solicite cada etapa de la misión.
