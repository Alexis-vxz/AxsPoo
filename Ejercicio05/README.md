# 🏛️ Abstracción en Python: El Módulo ABC

Este ejercicio demuestra el uso de **Clases Abstractas** utilizando el módulo nativo de Python `abc`. Se establece un contrato de diseño donde cualquier animal que se cree debe, obligatoriamente, implementar su propia forma de "hablar".

---

## 🛠️ Componentes del Código

### 1. La Clase Abstracta (`Animal`)
* Hereda de `ABC` (Abstract Base Class).
* Utiliza el decorador `@abstractmethod` en el método `hablar()`.
* **Regla de Oro**: No se pueden crear objetos directamente de `Animal`. Si intentas hacer `animal = Animal()`, Python lanzará un error.

### 2. Implementación de Subclases
* **Perro**: Implementa el método `hablar` devolviendo un `"Guau!"`.
* **Gato**: Implementa el mismo método pero devuelve un `"Miau!"`.

---

## 🧠 Conceptos de POO Aplicados

1. **Abstracción**: Definimos el "qué" (todos los animales hablan) pero no el "cómo" (cada animal lo hace distinto).
2. **Contratos de Interfaz**: La clase base asegura que cualquier programador que cree un nuevo animal (como un `Pato` o `Vaca`) no olvide definir el método de sonido.
3. **Polimorfismo**: La función `hablar()` se comporta de manera diferente según el tipo de objeto que la llame.

---

## 🚀 Ejemplo de Uso
```python
perro = Perro()
gato = Gato()

print(perro.hablar()) # Salida: Guau!
print(gato.hablar())  # Salida: Miau!
