temperatura = float(input("Ingresa la temperatura actual en grados Celsius: "))

if temperatura < 10:
    print("Mucho frío")
elif temperatura >= 10 and temperatura <= 25:
    print("Clima templado")
elif temperatura >= 26 and temperatura <= 35:
    print("Clima cálido")
else:
    print("Alerta de calor extremo")
