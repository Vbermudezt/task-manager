import os
import sys
import json

data_file = 'data.json'

if not os.path.exists(data_file):
    with open(data_file, 'w') as file:
        json.dump({'pendientes': [], 'completadas': []}, file, indent=4)


def guardar_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)


def leer_data():
    with open(data_file) as file:
        return json.load(file)


def agregar_tareas():
    data = leer_data()
    tarea = input("Ingrese la tarea a agregar: ")
    data["pendientes"].append(tarea)
    guardar_data(data)
    print(f"La tarea {tarea} ha sido agregada")


def quitar_tareas():
    data = leer_data()
    tareas_pendientes = data['pendientes']
    if not tareas_pendientes:
        print("No hay tareas pendientes para eliminar")
        return
    print("Lista de tareas: ")
    for i, tarea in enumerate(tareas_pendientes, 1):
        print(f"{i}. {tarea}")
        try:
            indice = int(input("Ingrese el # de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas_pendientes):
                tarea_eliminada = tareas_pendientes.pop(indice)
                data["pendientes"] = tareas_pendientes
                guardar_data(data)
                print(f"La tarea {tarea_eliminada} ha sido eliminada")
            else:
                print(f"La tarea # {indice + 1} no existe")
        except ValueError:
            print("Por favor, ingrese un número")


def marcar_completada():
    data = leer_data()
    tareas_pendientes = data['pendientes']
    if not tareas_pendientes:
        print("No hay tareas pendientes para completar.")
        return

    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas_pendientes, 1):
        print(f"{i}. {tarea}")

    try:
        indice = int(input("Ingrese el número de la tarea completada: ")) - 1
        if 0 <= indice < len(tareas_pendientes):
            tarea_completada = tareas_pendientes.pop(indice)
            data['completadas'].append(tarea_completada)
            data['pendientes'] = tareas_pendientes
            guardar_data(data)
            print(
                f"La tarea '{tarea_completada}' ha sido marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")


def listar_tareas():
    """Muestra todas las tareas pendientes y completadas."""
    data = leer_data()
    tareas_pendientes = data['pendientes']
    tareas_completadas = data['completadas']

    print("\n--- Tareas Pendientes ---")
    if tareas_pendientes:
        for i, tarea in enumerate(tareas_pendientes, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

    print("\n--- Tareas Completadas ---")
    if tareas_completadas:
        for i, tarea in enumerate(tareas_completadas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas completadas.")


def main():
    print("Bienvenido al sistema de gestión de tareas.")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Listar tareas")
        print("5. Salir")
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
            continue

        if opcion == 1:
            agregar_tareas()
        elif opcion == 2:
            quitar_tareas()
        elif opcion == 3:
            marcar_completada()
        elif opcion == 4:
            listar_tareas()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == '__main__':
    main()
