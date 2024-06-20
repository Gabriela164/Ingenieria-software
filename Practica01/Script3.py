
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Ejercicio 3: Instalar la biblioteca de matplotlib para graficar una función
#de la elección del alumno. 
from matplotlib import pyplot

#Definimos nuestra funcion No. 1
def f1(x):
    return x**3 + 8*x**2 + 2*x - 8
# Definimos nuestra función No. 2
def f2(x):
    return (x**2)/2

x = range(-10, 15)

# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(-20, 20)
pyplot.ylim(-20, 20)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()