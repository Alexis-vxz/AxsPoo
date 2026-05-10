import os

ruta = "test.txt"

#Bytes
size = os.path.getsize(ruta)
kb = size / 1024
mb = size / (1024 ** 2)

print(f"tamaño: {kb:.2f}KB")

print(F"tamaño: {mb:.4f}MB")