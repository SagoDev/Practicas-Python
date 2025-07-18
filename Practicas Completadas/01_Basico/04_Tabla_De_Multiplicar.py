print("------ Tabla de Multiplicar ------")

numero = input("Ingrese un numero: ")
numero = int(numero)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"------ Tabla del {numero} -------")

for num in numeros:
    print(f"{numero} x {num} = {num * numero}")