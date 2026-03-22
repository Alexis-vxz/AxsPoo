# 📝 Registro de Calificaciones: Manejo de Excepciones y Archivos

Este proyecto implementa un sistema robusto para la captura y almacenamiento de datos académicos, utilizando técnicas avanzadas de **manejo de errores** para prevenir fallos durante la ejecución.

---

## 🛡️ Gestión de Errores (Try-Except-Finally)

El programa está diseñado para ser "a prueba de errores" mediante el uso de bloques `try-except`, cubriendo los siguientes escenarios:

1.  **Validación de Tipo (`ValueError`)**: Se utiliza una función auxiliar `peedir_entero` que asegura que el usuario ingrese un número y no texto, repitiendo la petición hasta que el dato sea válido.
2.  **Validación de Rango**: Se lanza una excepción personalizada si la calificación no está en el rango de **0 a 100**, asegurando la integridad de los datos académicos.
3.  **Gestión de Archivos**:
    * `FileNotFoundError`: Captura errores si el archivo de destino no existe o la ruta es incorrecta.
    * `PermissionError`: Maneja situaciones donde el programa no tiene permisos de escritura (ej. si el archivo está bloqueado).

---

## 💾 Persistencia de Datos

El programa utiliza el manejo de archivos en Python para guardar la información de manera permanente:
* **Modo de Apertura (`"a"`)**: Se utiliza el modo *append* para añadir nuevos estudiantes al final del archivo `calificaciones.txt` sin borrar los registros anteriores.
* **Context Manager (`with`)**: Garantiza que el archivo se cierre correctamente después de escribir, incluso si ocurre un error durante el proceso.

---

## 🏗️ Estructura del Flujo

* **Lógica Principal**: Captura el nombre y la nota, valida el rango y escribe en el disco.
* **Contador de Sesión**: Realiza un seguimiento de cuántos estudiantes se registraron con éxito en la ejecución actual.
* **Bloque `finally`**: Se ejecuta siempre al terminar el proceso, garantizando un mensaje de despedida cordial para el usuario, independientemente de si hubo errores o no.

---

## 🚀 Ejemplo de Uso
1. El usuario ingresa: `Alexis`
2. El usuario ingresa: `95`
3. El sistema guarda: `Alexis: 95` en el archivo local y confirma el registro exitoso.

---
<div align="center">
  <sub>**Vasquez Sanchez Alexis** - Grupo 2SS - ITE</sub>
</div>
