class Registro_calificaciones:
    """Clase para registrar calificaciones de estudiantes"""
    pass
def peedir_entero(mensaje):
    """Función para pedir un número entero al usuario con manejo de errores"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor ingresa un número entero válido.")
def registrar_calificaciones():
    estudiantes_registrados = 0

    try:
        nombre = input("Ingresa el nombre del estudiante: ")
        calificacion = peedir_entero(f"Ingresa la calificación del estudiante {nombre} (0-100): ")

# 2. Lanzar nuestra excepción personalizada
        if calificacion < 0 or calificacion > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")
        print(f"Estudiante: {nombre}, Calificación: {calificacion}")


# 3. Guardar en archivo .txt
        with open("calificaciones.txt", "a") as archivo:
            archivo.write(f"{nombre}: {calificacion}\n")

        estudiantes_registrados += 1
        print(f"Calificación registrada exitosamente Total estudiantes registrados: {estudiantes_registrados}")
    except Registro_calificaciones as e:
        print(f"Esta calificacion esta fuera de rango: {e}")
    except FileNotFoundError as e:
        print(f"Error al guardar la calificación, sorry:(: {e}")
    except PermissionError as e:
        print(f"Error no cuentas con los permisos para guardar la calificación: {e}")
    except Exception as e:
        print(f"Ocurrió un error que no se esperaba: {e}")

#Usar Finally para despedir al usuario
    finally:
        print("¡Gracias por usar el programa de registro de calificaciones!")

if __name__ == "__main__":    registrar_calificaciones()