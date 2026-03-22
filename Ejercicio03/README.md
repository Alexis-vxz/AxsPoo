# 🐕 Herencia y Polimorfismo: Clases Perro y Gato

Este proyecto demuestra cómo utilizar la **Herencia** en Python para crear clases especializadas a partir de una estructura base, organizando el código en módulos separados para una mejor mantenibilidad.

---

## 🏗️ Estructura del Proyecto

El código sigue una arquitectura modular, donde cada animal tiene su propio archivo, permitiendo que el script principal sea limpio y fácil de leer:

* **`Perro.py`**: Contiene la definición de la clase Perro (hereda de una clase base `Animal`).
* **`Gato.py`**: Contiene la definición de la clase Gato (hereda de una clase base `Animal`).
* **`main.py`**: El archivo que coordina la creación de objetos y ejecuta sus comportamientos.

---

## 🧠 Conceptos de POO Aplicados

### 1. Herencia (Inheritance)
Tanto `Perro` como `Gato` comparten atributos comunes (como `nombre` y `edad`) y métodos (como `describir`). En lugar de repetir código, ambos heredan de una clase padre, permitiendo la reutilización de lógica.

### 2. Polimorfismo (Polymorphism)
Aunque ambos animales tienen el método **`.hablar()`**, cada uno responde de manera distinta:
* El objeto `Gato` responderá con un "Miau".
* El objeto `Perro` responderá con un "Guau".
> Esto permite que el programa trate a diferentes objetos de la misma forma, ejecutando la acción específica que le corresponde a cada uno.

---

## 🚀 Ejecución y Resultados

En el script principal, se instancian cuatro objetos distintos:
1.  **Gatos**: `michi` (4 años) y `milk` (2 años).
2.  **Perros**: `firulais` (6 años) y `peke` (8 años).

Al ejecutar los métodos, el programa identifica automáticamente qué sonido y descripción corresponden a cada instancia, demostrando que los objetos mantienen su propio **estado** y **comportamiento**.

---
<div align="center">
  <sub>Vasquez Sanchez Alexis - Grupo 2SS - ITE</sub>
</div>
