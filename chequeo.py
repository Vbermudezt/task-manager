tareas = []


def agregar_tarea():
    tarea_nueva = (input("Ingrese la tarea a agregar: "))
    tareas.append(tarea_nueva)
    print(f"La tarea {tarea_nueva} ha sido agregada")


def lista_tareas():
    if not tareas:
        print("No hay tareas")
    else:
        print("Lista de tareas: ")
        for index, tarea in enumerate(tareas):
            print(f"tarea {index}. {tarea}")


def eliminar_tarea():
    # lista_tareas()
    try:
        tarea_a_eliminar = int(input("Ingrese el # de la tarea a eliminar: "))
        if tarea_a_eliminar >= 0 and tarea_a_eliminar < len(tareas):
            tareas.pop(tarea_a_eliminar)
            print(f"La tarea # {tarea_a_eliminar} ha sido eliminada")
        else:
            print("La tarea # {tarea_a_eliminar} no existe")
    except:
        print(f"hay un error al eliminar la tarea")


print("Bienvenido al sistema de chequeo de tareas")
while True:
    print("1. Agregar tarea")
    print("2. eliminar tarea")
    print("3. lista de tareas")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        agregar_tarea()

    elif opcion == 2:
        eliminar_tarea()

    elif opcion == 3:
        lista_tareas()

    elif opcion == 4:
        break
    else:
        print("Que tengas un buen día")
