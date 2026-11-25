import os
os.system("cls")
horas = float(input("Quanmtas horas você estuda?"))
if horas < 2:
    print("Pouco estudo")
elif horas <=4:
    print("Estudo médio")
else:
    print("Muito estudo")