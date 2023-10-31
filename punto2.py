import tkinter as tk

# Función para verificar si alguien ganó
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if "".join(fila).count(jugador * 3) > 0:
            return True
    
    # Verificar columnas
    for columna in range(5):
        if "".join([tablero[fila][columna] for fila in range(5)]).count(jugador * 3) > 0:
            return True

    # Verificar diagonales
    diagonal1 = "".join([tablero[i][i] for i in range(5)])
    diagonal2 = "".join([tablero[i][4 - i] for i in range(5)])
    
    if diagonal1.count(jugador * 3) > 0 or diagonal2.count(jugador * 3) > 0:
        return True

    return False

# Función para manejar clics en los botones del tablero
def hacer_jugada(fila, columna):
    global jugador_actual, tablero

    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador_actual
        botones[fila][columna].config(text=jugador_actual)
        if verificar_ganador(tablero, jugador_actual):
            mensaje.config(text=f"¡El jugador {jugador_actual} ha ganado!")
            deshabilitar_botones()
        else:
            jugador_actual = "X" if jugador_actual == "O" else "O"

# Función para reiniciar el juego
def reiniciar_juego():
    global jugador_actual, tablero
    jugador_actual = "X"
    tablero = [[" " for _ in range(5)] for _ in range(5)]
    mensaje.config(text="")
    for fila in botones:
        for boton in fila:
            boton.config(text=" ", state=tk.NORMAL)

# Función para deshabilitar todos los botones del tablero
def deshabilitar_botones():
    for fila in botones:
        for boton in fila:
            boton.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Triqui 5x5")

# Inicializar variables
jugador_actual = "X"
tablero = [[" " for _ in range(5)] for _ in range(5)]
botones = []

# Crear botones del tablero
for fila in range(5):
    fila_botones = []
    for columna in range(5):
        boton = tk.Button(ventana, text=" ", font=("Arial", 20), width=4, height=2,
                          command=lambda fila=fila, columna=columna: hacer_jugada(fila, columna))
        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)
    botones.append(fila_botones)

# Crear mensaje de resultado
mensaje = tk.Label(ventana, text="", font=("Arial", 16))
mensaje.grid(row=5, columnspan=5)

# Botón para reiniciar el juego
reiniciar_button = tk.Button(ventana, text="Reiniciar", font=("Arial", 16), command=reiniciar_juego)
reiniciar_button.grid(row=6, columnspan=5)

ventana.mainloop()
