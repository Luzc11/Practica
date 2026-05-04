nota = float(input("Ingrese la nota: "))

if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 60:
    print("Aprobado")
elif nota >= 0:
    print("Reprobado")
else:
    print("Nota inválida")