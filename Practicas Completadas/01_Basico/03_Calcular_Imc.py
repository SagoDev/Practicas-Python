print("----- Calcular IMC -----")
masa = input("Ingrese peso en Kg: ")
altura = input("Igrese altura en metros: ")

masa = float(masa)
altura = float(altura)
imc = masa / (altura * altura)

print("------------------------")
print(f"El IMC es: {round(imc,2)}")
print("------ Pronóstico ------")
if imc < 18.5:
    print("Indice de masa corporal BAJO.")
elif 18.5 <= imc < 25:
    print("Indice de masa corporal NORMAL.")
elif 25 <= imc < 30:
    print("Indice de masa corporal ALTO. Presenta SOBREPESO.")
elif imc > 30:
    print("Indice de masa corporal MUY ALTO. Presenta OBESIDAD.")
print("------------------------")
