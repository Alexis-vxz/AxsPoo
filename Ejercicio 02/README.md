# 🐾 Prácticas: Gestión de Objetos (Mascotas y Cuentas Bancarias)

Este repositorio contiene dos implementaciones fundamentales de la **Programación Orientada a Objetos** en Python, enfocadas en la manipulación de atributos a través de métodos de instancia.

---

## 🐶 1. Clase Mascota: Gestión de Estado Emocional

Esta clase simula el comportamiento de una mascota virtual, controlando su nivel de felicidad mediante interacciones.

### ⚙️ Funcionalidades
* **Atributos**: `nombre`, `tipo`, `edad` y `nivelFelicidad`.
* **`alimentar()` y `jugar()`**: Métodos que modifican el nivel de felicidad del objeto. 
* **`esFeliz()`**: Un método de tipo booleano que evalúa si el nivel de felicidad supera el umbral de **70**.
* **`mostrarEstado()`**: Resume la situación actual de la mascota.

> **Nota técnica**: En el código proporcionado, los métodos de alimentar y jugar asignan un valor fijo (10 y 20). Una mejora lógica sería sumar esos valores al nivel actual (`self.nivelFelicidad += 10`).

---

## 💳 2. Clase CuentaBancaria: Lógica de Transacciones

Este ejercicio modela un sistema bancario básico con validaciones de seguridad para el retiro de efectivo.

### ⚙️ Funcionalidades
* **`depositar(cantidad)`**: Incrementa el saldo de la cuenta de forma directa.
* **`retirar(cantidad)`**: Incluye una **validación lógica**. Si la cantidad a retirar es mayor al saldo disponible, el programa bloquea la transacción y muestra un mensaje de "Saldo insuficiente".
* **`consultarSaldo()`**: Retorna el valor actual almacenado en la instancia.
* **`mostarInformacion()`**: Presenta el nombre del titular y su saldo disponible de forma amigable.

---

## 🎓 Conceptos de POO Aplicados

1. **Abstracción**: Se simplifican entidades complejas (un animal o una cuenta de banco) a sus atributos y acciones más relevantes para el programa.
2. **Encapsulamiento**: Los datos (como el saldo o la felicidad) no se modifican "desde fuera" directamente, sino a través de métodos (`retirar`, `jugar`) que pueden contener reglas de negocio.
3. **Instanciación Múltiple**: Se demuestra cómo una misma clase puede generar múltiples objetos independientes (`mascota1` vs `mascota2` o `cuenta1` vs `cuenta2`) con sus propios datos.

---
<div align="center">
  <sub>Vasquez Sanchez Alexis - Grupo 2SS - ITE</sub>
</div>
