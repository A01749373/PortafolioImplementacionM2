# -*- coding: utf-8 -*-
"""PortafolioImplementacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HOSiywCri6B0RKkgvBj_n7o76l4zOAXK
"""

'''
Ariadna Jocelyn Guzmán Jiménez A01749373
27-08-2022
"Implementación de refinamiento de modelos"
'''

# Librerias 

import pandas as pd, matplotlib.pyplot as plt

# Importación de datos 

columns = ["sepal length","sepal width","petal length","petal width", "class"]
df = pd.read_csv("iris.data", names = columns)

x= df["sepal length"]
y= df["sepal width"]

n = len(x)

theta = [1,1]
alpha = 0.0001
iterations = 100000

def h0(x, theta):
  '''
  Calculo de la funcion de hipotesis
  '''
  return theta[0] + theta[1] * x



def linearRegression(iterations, theta, alpha):
  '''
  Funcion que realiza el metodo de regresion lineal
  con gradiente descendiente
  '''
  
  i = iterations
  while (i != 0):

    all_h0 = []
    delta = []
    deltaX = []
    for xi, yi in zip(x,y):
      all_h0.append(h0(xi, theta)) #h0
      delta.append(h0(xi, theta) - yi)  #h0-y
      deltaX.append((h0(xi, theta) - yi) * xi) #(h0-y) * x
    i -=1 
    # Refinamiento de theta
    theta[0] = theta[0] - alpha/n * sum(delta)
    theta[1] = theta[1] - alpha/n * sum(deltaX)
  plt.plot(x, all_h0, color="#C6E5B1")
  plt.scatter(x,y,marker=".", color="#F7D917")
  plt.title("Sepal width vs sepal length iris species")
  plt.xlabel("Sepal length")
  plt.ylabel("Sepal width")
  plt.show()
  print("Predicción\n", all_h0)
  print("\nDelta\n", delta)
  print("\nDeltaX\n", deltaX)
  print("\nTheta actualizada después de {} iteraciones \n".format(iterations), theta)



linearRegression(iterations, theta, alpha)
