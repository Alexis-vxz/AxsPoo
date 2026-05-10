archivo = open("test.txt", "a", encoding="utf-8")

for i in range(1024 * 1024):
    archivo.write("A")
archivo.close()