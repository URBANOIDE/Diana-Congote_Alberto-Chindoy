import random
import math

# Datos de ejemplo para las conferencias
conferencias = [
    {"nombre": "Conferencia 1", "duracion": 1.5, "horarioPreferido": "Mañana", "asientosDisponibles": 50},
    {"nombre": "Conferencia 2", "duracion": 2, "horarioPreferido": "Tarde", "asientosDisponibles": 30},
    {"nombre": "Conferencia 3", "duracion": 2, "horarioPreferido": "Tarde", "asientosDisponibles": 30},
    # Agrega datos para las otras conferencias
]

# Datos de ejemplo para las salas de conferencias y horarios
salas = ["Sala A", "Sala B", "Sala C"]
horarios = ["Mañana", "Tarde", "Noche"]

# Función para calcular la asistencia total de una programación
def calcular_asistencia_total(programacion):
    """
    Calcula la asistencia total de una programación dada.

    Args:
        programacion (list): Una lista de conferencias programadas.

    Returns:
        int: La asistencia total.
    """
    asistencia_total = 0
    for conferencia in programacion:
        asistencia_total += conferencia["asistentes"]
    return asistencia_total

# Función para generar una programación aleatoria
def generar_programacion_aleatoria(conferencias, salas, horarios):
    """
    Genera una programación aleatoria para las conferencias dadas.

    Args:
        conferencias (list): Una lista de conferencias disponibles.
        salas (list): Una lista de salas disponibles.
        horarios (list): Una lista de horarios disponibles.

    Returns:
        list: Una lista de conferencias programadas con salas y horarios aleatorios.
    """
    programacion = []
    for conferencia in conferencias:
        sala = random.choice(salas)
        horario = random.choice(horarios)
        programacion.append({"conferencia": conferencia, "sala": sala, "horario": horario, "asistentes": 0})
    return programacion

# Función para aplicar el algoritmo de recocido simulado
def recocido_simulado(conferencias, salas, horarios, temperatura_inicial, enfriamiento):
    """
    Aplica el algoritmo de recocido simulado para encontrar una programación óptima.

    Args:
        conferencias (list): Una lista de conferencias disponibles.
        salas (list): Una lista de salas disponibles.
        horarios (list): Una lista de horarios disponibles.
        temperatura_inicial (float): La temperatura inicial del algoritmo.
        enfriamiento (float): La tasa de enfriamiento.

    Returns:
        list: La programación óptima encontrada.
    """
    programacion_actual = generar_programacion_aleatoria(conferencias, salas, horarios)
    asistencia_actual = calcular_asistencia_total(programacion_actual)

    mejor_programacion = list(programacion_actual)
    mejor_asistencia = asistencia_actual

    temperatura = temperatura_inicial

    while temperatura > 1:
        # Selecciona dos conferencias aleatorias
        i, j = random.sample(range(len(conferencias)), 2)

        # Intercambia los horarios de las conferencias
        programacion_actual[i]["horario"], programacion_actual[j]["horario"] = (
            programacion_actual[j]["horario"],
            programacion_actual[i]["horario"],
        )

        # Calcula la asistencia con la nueva programación
        nueva_asistencia = calcular_asistencia_total(programacion_actual)

        # Calcula la diferencia de asistencia
        diferencia = nueva_asistencia - asistencia_actual

        # Si la nueva programación es mejor o se acepta con una cierta probabilidad, guárdala
        if diferencia > 0 or random.random() < math.exp(diferencia / temperatura):
            asistencia_actual = nueva_asistencia
            if asistencia_actual > mejor_asistencia:
                mejor_programacion = list(programacion_actual)
                mejor_asistencia = asistencia_actual
        else:
            # Deshace el intercambio si no se acepta
            programacion_actual[i]["horario"], programacion_actual[j]["horario"] = (
                programacion_actual[j]["horario"],
                programacion_actual[i]["horario"],
            )

        # Reduce la temperatura
        temperatura *= enfriamiento

    return mejor_programacion

# Ejemplo de uso
temperatura_inicial = 1000
enfriamiento = 0.98

programacion_optima = recocido_simulado(conferencias, salas, horarios, temperatura_inicial, enfriamiento)

print("Programación óptima:")
for conferencia in programacion_optima:
    print(f"Conferencia: {conferencia['conferencia']['nombre']}, Sala: {conferencia['sala']}, Horario: {conferencia['horario']}")

print("Asistencia total óptima:", calcular_asistencia_total(programacion_optima))
