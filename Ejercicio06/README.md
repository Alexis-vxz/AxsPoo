# ⛏️ Minecraft Logic: Gestión de Herramientas y Mobs

Este proyecto final aplica todos los conceptos avanzados de la **Programación Orientada a Objetos** en Python para simular un sistema de interacción entre herramientas (Picos, Espadas, Arcos) y criaturas (Vaca, Creeper, Wither).

---

## 🏗️ Estructura de Clases y Abstracción

El proyecto utiliza clases base abstractas para garantizar que todos los objetos sigan una estructura rígida pero flexible:

### 1. Sistema de Herramientas (`Herramienta`)
Se implementan herramientas con durabilidad limitada y lógicas de uso específicas:
* **Pico, Espada y Pala**: Consumen durabilidad con cada uso.
* **Arco (Bonus 💎)**: Incluye una lógica especial que requiere **flechas**. Si las flechas se agotan, el arco no puede ser utilizado aunque tenga durabilidad.

### 2. Sistema de Criaturas (`Mob`)
Utiliza el módulo `abc` para definir comportamientos obligatorios en todos los seres vivos del juego:
* **Sonido, Comportamiento y Movimiento**: Cada subclase (Vaca, Enderman, Creeper, Wither) implementa estos métodos de forma única.

---

## 🧠 Desafíos de POO Resueltos

### ❌ Punto 2: Instanciación de Clase Abstracta
Se documentó el comportamiento de Python al intentar ejecutar `Mob("test", 10)`:
> **Observación**: El programa arroja un `TypeError`. Esto ocurre porque `Mob` es una clase abstracta y funciona únicamente como plantilla; no posee una implementación completa, por lo que Python prohíbe crear objetos directamente de ella.

### 🏹 Punto 3: Lógica del Arco
Se desarrolló una clase `Arco` que sobrescribe el método `.usar()` para añadir una validación de inventario (`flechas`). Es un ejemplo claro de cómo una subclase puede añadir nuevas reglas de negocio sin romper la estructura del padre.

### 🐉 Polimorfismo en Acción
Mediante un bucle `for` y la función `zip()`, el programa procesa una lista de herramientas y objetivos diferentes, ejecutando la acción correcta para cada par (minar, atacar o excavar) de forma automática.

---

## 📋 Entidades Implementadas
* **Herramientas**: Pico (Diamante), Espada (Hierro), Pala (Madera), Arco (Madera).
* **Mobs**: Vaca, Creeper, Enderman y **Wither** (Boss con 100 HP).

---
<div align="center">
  <sub>**Vasquez Sanchez Alexis** - Grupo 2SS - ITE</sub>
  <br>
  <sub>Materia: Programación Orientada a Objetos | Prof. Xenia Padilla</sub>
</div>
