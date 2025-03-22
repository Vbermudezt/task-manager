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


def agregar_tareas(parametros):
    data = leer_data()
    tarea = " ".join(map(str, parametros))
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

    if len(sys.argv) < 3:
        print("Uso: python cli.py <comando> <accion> [parametros...]")
        return

    comando = sys.argv[1]
    accion = sys.argv[2]
    parametros = sys.argv[3:]

    # Verificar si el comando es correcto
    if comando != "todo":
        print(
            f"Error: Comando '{comando}' no reconocido. Usa 'todo' para empezar.")
        return

    if accion == "add":
        agregar_tareas(parametros)
    elif accion == "remove":
        quitar_tareas()
    elif accion == "complete":
        marcar_completada()
    elif accion == "list":
        listar_tareas()
    else:
        print("Opción no válida. Intente de nuevo.")


if __name__ == '__main__':
    main()
