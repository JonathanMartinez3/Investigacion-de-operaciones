import matplotlib.pyplot as plt

#Definicion de la función
def f1(x):
    return ((x/2) + 1)

#Valores que toma el eje x
x = range(-10, 10)

#Graficar función
plt.plot(x, [f1(i) for i in x])
plt.title("2(2x - y) < 2(x + y) - 4")

#Establecer colores de los ejes
plt.axhline(0, color = "black")
plt.axvline(0, color = "black")

#Limitar los valores de los ejes
plt.xlim(-15, 15)
plt.ylim(-15, 15)


#Guardar gráfico como imagen PNG
plt.savefig("EjercicioTres.png")

#Visualizar gráfico
plt.show()