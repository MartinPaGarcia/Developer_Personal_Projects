import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un dataframe

df = pd.read_csv("")

# Imprimir el promedio de X

print(df["X"].mean())

# Imprimir el cuartil de 25 de Z

print(df["Z"].quantile(0.25))

# Definir una variable "X_Y" que almacene la diferencia entre X y Y

df["X_Y"] = df["X"] - df["Y"]
print(df["X_Y"])

# Definir un nuevo Dataframe que seleccione los datos que tengan a x entre 3 y 5

datos_2 = df[(df["X"] >= 3) & (df["X"] <= 5)]

# Definir un nuevo Dataframe que corte los datos en la variable W, y almacene aquellos... No se especifica en el pizarron

datos_3 = df[df["W"] > 0]