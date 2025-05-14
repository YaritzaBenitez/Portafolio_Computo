import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("math-students.csv", sep=';')

# Información general
print("Primeras filas del dataset:")
print(df.head())
print("\nResumen estadístico:")
print(df.describe())

# Gráfica 1: Histograma de G3 (calificación final)
plt.figure(figsize=(8, 5))
sns.histplot(df["G3"], bins=15, kde=True, color='skyblue')
plt.title("Distribución de la Calificación Final (G3)")
plt.xlabel("G3")
plt.ylabel("Cantidad de Estudiantes")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/Histograma_calificaciones.png")

# Gráfica 2: Promedio de G3 por sexo
plt.figure(figsize=(6, 4))
sns.barplot(x="sex", y="G3", data=df, palette="Set2", ci=None)
plt.title("Promedio de Calificación Final por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Promedio G3")
plt.tight_layout()
plt.savefig("output/Promedio_sexo.png")

# Gráfica 3: Promedio de G3 por nivel educativo de la madre (Medu)
plt.figure(figsize=(8, 5))
sns.barplot(x="Medu", y="G3", data=df, palette="Set3", ci=None)
plt.title("Promedio de G3 por Nivel Educativo de la Madre")
plt.xlabel("Nivel Educativo Madre (0-4)")
plt.ylabel("Promedio G3")
plt.tight_layout()
plt.savefig("output/Promedio_madre.png")

# Gráfica 4: Relación entre tiempo de estudio y calificación final
plt.figure(figsize=(6, 4))
sns.boxplot(x="studytime", y="G3", data=df, palette="coolwarm")
plt.title("G3 según Tiempo de Estudio")
plt.xlabel("Tiempo de Estudio (1-4)")
plt.ylabel("G3")
plt.tight_layout()
plt.savefig("output/Relacion_estudio.png")

# Gráfica 5: Correlación entre variables numéricas
plt.figure(figsize=(12, 8))
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor de Correlación")
plt.tight_layout()
plt.savefig("output/correlacion.png")
