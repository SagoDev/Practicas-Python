print("------ Pálindromos ------ \n")

palabra = input("Ingrese una palabra: ")

print(" \n------ Analizando ------ \n")

reverso = palabra[::-1]

print(f"Palabra : {palabra}")
print(f"Reverso : {reverso} \n")

print("------ Conclusión ------ \n")

if palabra == reverso:
    print(f"La palabra '{palabra}' SI es un pálindromo. \n")
else:
    print(f"La palabra '{palabra}' NO es un pálindromo. \n")