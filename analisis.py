# ==========================================
# ANALISIS DEL DATASET TITANIC
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# 1. CARGAR EL DATASET
# ------------------------------------------

df = pd.read_csv("data/train.csv")

print("\n===== PRIMERAS FILAS =====")
print(df.head())


# ------------------------------------------
# 2. EXPLORACION INICIAL
# ------------------------------------------

print("\n===== NUMERO DE PASAJEROS =====")
print(len(df))

print("\n===== NUMERO DE COLUMNAS =====")
print(len(df.columns))

print("\n===== VARIABLES DISPONIBLES =====")
print(df.columns.tolist())

print("\n===== TIPOS DE DATOS =====")
print(df.dtypes)

print("\n===== VALORES FALTANTES =====")
print(df.isnull().sum())

print("\n===== REGISTROS DUPLICADOS =====")
print(df.duplicated().sum())

print("\n===== ESTADISTICAS DESCRIPTIVAS =====")
print(df.describe())


# ------------------------------------------
# 3. TRATAMIENTO DE VALORES FALTANTES
# ------------------------------------------

# AGE
# Se reemplazan los valores faltantes por la mediana
df["Age"] = df["Age"].fillna(df["Age"].median())

# EMBARKED
# Solo hay pocos valores faltantes,
# por eso se reemplazan por el valor más frecuente
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# CABIN
# Tiene muchos valores faltantes.
# Se coloca "Unknown" para indicar que no conocemos la cabina.
df["Cabin"] = df["Cabin"].fillna("Unknown")


print("\n===== VALORES FALTANTES DESPUES DE LA LIMPIEZA =====")
print(df.isnull().sum())


# ------------------------------------------
# 4. CREAR NUEVAS VARIABLES
# ------------------------------------------

# Variable 1: tamaño de la familia
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Variable 2: categoria de edad
def categoria_edad(edad):

    if edad < 12:
        return "Niño"

    elif edad < 18:
        return "Joven"

    elif edad < 60:
        return "Adulto"

    else:
        return "Adulto mayor"


df["AgeGroup"] = df["Age"].apply(categoria_edad)


print("\n===== NUEVAS VARIABLES =====")
print(df[["Age", "FamilySize", "AgeGroup"]].head())


# ------------------------------------------
# 5. ANALISIS 1
# ¿QUE PORCENTAJE SOBREVIVIO?
# ------------------------------------------

supervivientes = df["Survived"].mean() * 100

print("\n===== ANALISIS 1 =====")
print("Porcentaje de pasajeros que sobrevivio:",
      round(supervivientes, 2), "%")


# ------------------------------------------
# 6. ANALISIS 2
# SUPERVIVENCIA SEGUN SEXO
# ------------------------------------------

supervivencia_sexo = df.groupby("Sex")["Survived"].mean() * 100

print("\n===== ANALISIS 2 =====")
print("Supervivencia segun sexo:")
print(supervivencia_sexo.round(2))


# ------------------------------------------
# 7. ANALISIS 3
# SUPERVIVENCIA SEGUN CLASE
# ------------------------------------------

supervivencia_clase = df.groupby("Pclass")["Survived"].mean() * 100

print("\n===== ANALISIS 3 =====")
print("Supervivencia segun clase:")
print(supervivencia_clase.round(2))


# ------------------------------------------
# 8. ANALISIS 4
# SUPERVIVENCIA SEGUN GRUPO DE EDAD
# ------------------------------------------

supervivencia_edad = df.groupby("AgeGroup")["Survived"].mean() * 100

print("\n===== ANALISIS 4 =====")
print("Supervivencia segun grupo de edad:")
print(supervivencia_edad.round(2))


# ------------------------------------------
# 9. ANALISIS 5
# VIAJAR SOLO O ACOMPAÑADO
# ------------------------------------------

df["TravelingAlone"] = df["FamilySize"].apply(
    lambda x: "Solo" if x == 1 else "Acompañado"
)

supervivencia_compania = df.groupby(
    "TravelingAlone"
)["Survived"].mean() * 100

print("\n===== ANALISIS 5 =====")
print("Supervivencia viajando solo o acompañado:")
print(supervivencia_compania.round(2))


# ------------------------------------------
# 10. VISUALIZACION 1
# SUPERVIVENCIA POR SEXO
# ------------------------------------------

supervivencia_sexo.plot(
    kind="bar",
    title="Porcentaje de supervivencia por sexo"
)

plt.ylabel("Supervivencia (%)")
plt.xlabel("Sexo")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/graficos/supervivencia_sexo.png")

plt.show()


# ------------------------------------------
# 11. VISUALIZACION 2
# SUPERVIVENCIA POR CLASE
# ------------------------------------------

supervivencia_clase.plot(
    kind="bar",
    title="Porcentaje de supervivencia por clase"
)

plt.ylabel("Supervivencia (%)")
plt.xlabel("Clase")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/graficos/supervivencia_clase.png")

plt.show()


# ------------------------------------------
# 12. VISUALIZACION 3
# SUPERVIVENCIA POR EDAD
# ------------------------------------------

supervivencia_edad.plot(
    kind="bar",
    title="Porcentaje de supervivencia por grupo de edad"
)

plt.ylabel("Supervivencia (%)")
plt.xlabel("Grupo de edad")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/graficos/supervivencia_edad.png")

plt.show()


# ------------------------------------------
# 13. VISUALIZACION 4
# TARIFA Y SUPERVIVENCIA
# ------------------------------------------

df.boxplot(
    column="Fare",
    by="Survived"
)

plt.title("Tarifa pagada y supervivencia")
plt.suptitle("")
plt.xlabel("Sobrevivio (0 = No, 1 = Si)")
plt.ylabel("Tarifa")
plt.tight_layout()

plt.savefig("outputs/graficos/tarifa_supervivencia.png")

plt.show()


# ------------------------------------------
# FIN DEL ANALISIS
# ------------------------------------------

print("\n===== ANALISIS TERMINADO =====")
print("Los graficos fueron guardados en:")
print("outputs/graficos/")