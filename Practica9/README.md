# Práctica 9: Manejo de Archivos en Python 🐍

Este repositorio contiene ejercicios prácticos para la manipulación de archivos de texto (`.txt`) utilizando Python, enfocándose en la escritura, el modo de anexado y el cálculo de peso en disco.

## 📂 Archivos del Proyecto

* **`add.py`**: Script principal que añade 1,048,576 caracteres ("A") al archivo `test.txt` usando el modo `append`.
* **`filesize.py`**: Utilidad para calcular y mostrar el tamaño del archivo resultante en KB y MB.
* **`Escritura.py`**: Script de apoyo para la creación inicial de documentos.
* **`test.txt`**: Archivo de texto generado durante las pruebas.

## 🛠️ Funcionamiento

El código central utiliza un ciclo para llenar el archivo de forma masiva, lo que permite observar cómo crece el tamaño del archivo en el sistema de archivos:

```python
# Ejemplo de add.py
archivo = open("test.txt", "a", encoding="utf-8")

for i in range(1024 * 1024):
    archivo.write("A")

archivo.close()
