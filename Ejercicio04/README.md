# 🚀 Proyecto Integrador: Sistemas de Combate y Gestión de Menú

Estos ejercicios contienen una colección de implementaciones en Python que demuestran el dominio de la **Programación Orientada a Objetos (POO)** aplicada a dos escenarios distintos: un sistema de personajes RPG y un gestor de productos de restaurante.

---

## ⚔️ 1. Módulo de Combate (RPG)
En esta sección se utiliza la **Herencia** y el **Polimorfismo** para crear diferentes clases de héroes que comparten una base común pero ejecutan habilidades únicas.

### 🛡️ Personajes y Habilidades
* **Guerrero**: Especialista en combate físico. Su habilidad depende del arma equipada (ej. Espada).
* **Mago**: Usuario de artes místicas. Su poder reside en el uso de hechizos y conjuros.
* **Arquero**: Atacante a distancia que requiere la gestión de proyectiles (flechas).

> **Concepto POO**: Se aplica la **Sobrescritura de Métodos** (`usar_habilidad`), permitiendo que cada héroe responda de forma distinta a una misma instrucción.

---

## 🍽️ 2. Módulo de Restaurante (Menú)
Este módulo organiza los productos de un establecimiento en categorías lógicas, permitiendo una gestión eficiente de precios y características dietéticas.

### 📋 Categorías del Menú
1.  **Comida**: Clasificada por estilo (ej. Saludable).
2.  **Bebida**: Diferenciada por temperatura de servicio (Frío/Caliente).
3.  **Postre**: Incluye validación booleana para el contenido de azúcar (apto para restricciones alimentarias).

---

## 🛠️ Tecnologías y Estructura
* **Lenguaje**: Python 3.
* **Arquitectura**: Modular (uso de `import` desde archivos externos como `Guerrero.py`, `Comida.py`, etc.).
* **Principios Aplicados**:
    * **Abstracción**: Modelado de entidades reales en clases de software.
    * **Modularidad**: Separación de responsabilidades en diferentes archivos.
    * **Instanciación**: Creación de múltiples objetos con estados independientes.

---

<div align="center">
  <sub><strong>Alexis Vasquez Sanchez</strong> - Grupo 2SS - ITE</sub>
  <br>
  <sub>Materia: Programación Orientada a Objetos | Prof. Xenia Padilla</sub>
</div>
