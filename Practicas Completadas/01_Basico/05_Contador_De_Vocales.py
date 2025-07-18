total_vocales = 0
vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

print("------ Contador de Vocales ------")
palabra = input("Ingrese una palabra: ")


print("------ Analizando ------")
for letra in palabra:
    for vocal in vocales:
        if letra == vocal:
            total_vocales += 1

print("------ Resultado ------")
print(f"Palabra : {palabra}")
print(f"Contiene : {total_vocales} Vocales")
