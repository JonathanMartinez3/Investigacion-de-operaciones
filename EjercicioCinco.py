import matplotlib.pyplot as plt

#Definicion de la función
def f1(x):
    return (20 - (2*x)/3)

def f2(x):
    return (0)

#Valores que toma el eje x
x = range(-100, 100)

#Graficar función
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])

plt.title("2x + 3y <= 60,\nx >= 0,\ny >= 0")

#Establecer colores de los ejes
plt.axhline(0, color = "black")
plt.axvline(0, color = "black")

#Limitar los valores de los ejes
plt.xlim(-100, 100)
plt.ylim(-100, 100)


#Guardar gráfico como imagen PNG
plt.savefig("EjercicioTres.png")

#Visualizar gráfico
plt.show()