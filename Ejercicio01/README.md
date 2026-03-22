# 🎓 Práctica: Clase Estudiante (Fundamentos de POO)

Este proyecto implementa una estructura básica en Python para la gestión de estudiantes, demostrando conceptos clave de la **Programación Orientada a Objetos** como la encapsulación de datos y la manipulación de objetos mediante métodos.

---

## 🛠️ Estructura del Código

La clase `Estudiante` permite modelar a un alumno con sus datos básicos y gestionar su historial académico.

### 1. El Constructor (`__init__`)
Define los atributos iniciales de cada estudiante:
* `nombre`, `edad`, `carrera`: Datos proporcionados al crear el objeto.
* `calificaciones`: Una lista vacía `[]` que se inicializa automáticamente para cada instancia.

### 2. Métodos Principales
* **`setCalificaciones(calificacion)`**: Permite añadir una nueva nota a la lista del estudiante.
* **`mostrarPromedio()`**: Calcula la media aritmética de las notas. Incluye una validación para evitar errores de división por cero si el alumno no tiene notas.
* **`mostrarInformacionUsuario()`**: Devuelve un saludo formal con los datos del estudiante usando *f-strings*.

---

## 🚀 Ejemplo de Ejecución

En el script se realizan las siguientes acciones:

1.  **Instanciación**: Se crean tres objetos (`estudiante1`, `estudiante2`, `estudiante3`) con diferentes carreras.
2.  **Interacción**: Se agregan calificaciones a "Pepe" (100, 50 y 40).
3.  **Salida de Datos**:
    * Se muestra la información personal.
    * Se imprime el promedio calculado (para Pepe el promedio es `63.33`).

```python
# Ejemplo de salida esperada:
# "Hola, soy Pepe, tengo 30 años y estudio Ing. en sistemas"
# "La calificación del Pepe es: 63.333333333333336"
