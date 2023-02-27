import matplotlib.pyplot as plt

#Definicion de la función
def f1(x):
    return (3 - 2*x)

def f2(x):
    return (1/2)

def f3(x):
    return x

#Valores que toma el eje x
x = range(-10, 10)

#Graficar función
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
plt.plot(x, [f3(i) for i in x])

plt.title("2x + y > 3,\n 2y - 1 > 0, \nx >= y")

#Establecer colores de los ejes
plt.axhline(0, color = "black")
plt.axvline(0, color = "black")

#Limitar los valores de los ejes
plt.xlim(-20, 20)
plt.ylim(-20, 20)


#Guardar gráfico como imagen PNG
plt.savefig("EjercicioTres.png")

#Visualizar gráfico
plt.show()