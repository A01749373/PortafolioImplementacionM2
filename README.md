<h1 align = "center">
  Módulo 2: Portafolio de Implementacion sin Framework : Regresión lineal
</h1>

<h3 align = "center">
 Ariadna Jocelyn Guzmán Jiménez A01749373
</h3>

<h3 align = "center">
 18-09-2022
</h3>
 
#### Nombre del archivo a revisar:
portafolioimplementacion.py

#### Librerías utilizadas:
* **numpy** : Para la creación de vectores y matrices.
* **pandas** : Para la creación y operaciones de dataframes.
* **seaborn** : Basada en matplotlib para la graficación de datos estadísticos.
* **matplotlib.pyplot** : Para la generación de gráficos.
* **sklearn.model_selection - train_test_split** : Para la división de los datos en subconjuntos de entrenamiento y prueba.
* **sklearn.linear_model - LinearRegression** : Para la comparación de resultados del modelo implementado con la librería.

#### Dataset utilizado: 
  	
Fish market, obtenido de la página https://www.kaggle.com/datasets/aungpyaeap/fish-market

*Set de datos de especies diferentes comunes en la venta del mercado de pescado, que predice su peso de acuerdo a sus medidas*

Atributos:
1. Species - nombre de la especie
2. Weight - peso en gramos
3. Length1 - medida vertical en cm
4. Length2 - medida diagonal en cm
5. Length3 - medida cruzada en cm
6. Height - altura en cm
7. Width - ancho en cm

#### Métrica de desempeño:
Se utilizó un modelo prueba de 30% y entrenamiento 70%, donde solo evaluamos el ancho en cm contra el peso del pez.

<img width="551" alt="image" src="https://user-images.githubusercontent.com/58440787/190930470-09892bd5-dccc-4255-9870-2b787d0d3e85.png">


Posteriormente, se realizó una variación de estimaciones (1000,10000,100000) para visualizar cual era el mejor y más preciso y así, calcular las predicciones.

**1000 iteraciones**

<img width="351" alt="image" src="https://user-images.githubusercontent.com/58440787/190930436-47fc2c64-f7a4-4e44-ab48-f11f9ea2a076.png">

**10000 iteraciones**

<img width="348" alt="image" src="https://user-images.githubusercontent.com/58440787/190930446-a4285c93-f669-41d2-bc7f-446945fbfb03.png">

**100000 iteraciones**

<img width="345" alt="image" src="https://user-images.githubusercontent.com/58440787/190930452-9a7eb9ce-c2ed-42f5-a5e5-c5f4b88aa713.png">



#### Predicciones de prueba: 
Visualizamos que el modelo fue preciso pero tuvo algunas fallas al tener una precisión del 84%. Nos dimos cuenta que conforme se elevaba el número de iteraciones, se mejoraba dicha presición, sin embargo, las diferencias no eran muy notables.
Se utilizó el modelo con **100000 iteraciones** y a continuación, se reflejan tablas que nos mencionan las entrada de X (ancho), el peso estimado y la predicción.


<img width="243" alt="image" src="https://user-images.githubusercontent.com/58440787/190930584-8ba44536-d958-46ce-90dd-015e82fb2e3a.png">


#### Comparación con la librería sklearn.linear_model LinearRegression()
Finalmente, hacemos la regresión lineal con la librería de sklearn, viendo que nuestro score de precisión, fue el mismo en train y test al del modelo implementado sin librería.

<img width="576" alt="image" src="https://user-images.githubusercontent.com/58440787/190930737-fd2c104e-9455-46ce-b16c-595344352c93.png">
