"""Análisis exploratorio y limpieza básica del dataset Titanic."""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def print_survival_by(dataframe, column, title):
    """Muestra pasajeros y porcentaje de supervivencia agrupados por una variable."""
    summary = (
        dataframe.groupby(column, observed=False)["Survived"]
        .agg(Pasajeros="count", Supervivencia="mean")
    )
    summary["Supervivencia (%)"] = (summary["Supervivencia"] * 100).round(2)
    summary = summary.drop(columns="Supervivencia")

    print(f"\n{title}")
    print(summary.to_string())


def save_survival_charts(dataframe, output_path):
    """Crea y guarda las visualizaciones principales del análisis."""
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Cantidad de sobrevivientes y no sobrevivientes.
    survival_counts = dataframe["Survived"].map(
        {0: "No sobrevivió", 1: "Sobrevivió"}
    ).value_counts().reindex(["No sobrevivió", "Sobrevivió"])
    plt.figure(figsize=(7, 5))
    survival_counts.plot(kind="bar", color=["#d95f02", "#1b9e77"])
    plt.title("Cantidad de sobrevivientes y no sobrevivientes")
    plt.xlabel("Resultado")
    plt.ylabel("Cantidad de pasajeros")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path / "cantidad_supervivencia.png")
    plt.close()

    # 2. Tasa de supervivencia por sexo.
    survival_by_sex = dataframe.groupby("Sex", observed=False)["Survived"].mean() * 100
    plt.figure(figsize=(7, 5))
    survival_by_sex.plot(kind="bar", color="#7570b3")
    plt.title("Tasa de supervivencia por sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Supervivencia (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path / "supervivencia_por_sexo.png")
    plt.close()

    # 3. Tasa de supervivencia por clase.
    survival_by_class = dataframe.groupby("Pclass", observed=False)["Survived"].mean() * 100
    plt.figure(figsize=(7, 5))
    survival_by_class.plot(kind="bar", color="#e7298a")
    plt.title("Tasa de supervivencia por clase")
    plt.xlabel("Clase (Pclass)")
    plt.ylabel("Supervivencia (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path / "supervivencia_por_clase.png")
    plt.close()

    # 4. Tasa de supervivencia por grupo de edad.
    survival_by_age = dataframe.groupby("AgeGroup", observed=False)["Survived"].mean() * 100
    plt.figure(figsize=(8, 5))
    survival_by_age.plot(kind="bar", color="#66a61e")
    plt.title("Tasa de supervivencia por grupo de edad")
    plt.xlabel("Grupo de edad")
    plt.ylabel("Supervivencia (%)")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path / "supervivencia_por_grupo_edad.png")
    plt.close()

    print(f"\nGráficas guardadas en: {output_path}")
    for chart_path in sorted(output_path.glob("*.png")):
        print(f"- {chart_path}")


def main():
    # La ruta funciona al ejecutar el archivo desde la raíz del proyecto.
    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "train.csv"
    df = pd.read_csv(data_path)

    print("=" * 70)
    print("EXPLORACIÓN INICIAL")
    print("=" * 70)
    print(f"Número de pasajeros: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")

    print("\nNombres de variables:")
    print(list(df.columns))

    print("\nTipos de datos:")
    print(df.dtypes.to_string())

    print("\nValores faltantes por variable:")
    missing = df.isna().sum().to_frame("Valores faltantes")
    missing["Porcentaje (%)"] = (missing["Valores faltantes"] / len(df) * 100).round(2)
    print(missing.to_string())

    print(f"\nRegistros duplicados: {df.duplicated().sum()}")

    print("\nEstadísticas descriptivas:")
    print(df.describe(include="all"))

    print("\n" + "=" * 70)
    print("LIMPIEZA Y PREPROCESAMIENTO")
    print("=" * 70)

    # La mediana es sencilla y resistente a valores extremos en la edad.
    age_median = df["Age"].median()
    df["Age"] = df["Age"].fillna(age_median)

    # La moda representa la categoría más frecuente de puerto de embarque.
    embarked_mode = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(embarked_mode)

    # No se inventan cabinas: solo se conserva si la información estaba disponible.
    df["HasCabin"] = df["Cabin"].notna()
    df = df.drop(columns="Cabin")

    # Variables nuevas solicitadas para el análisis.
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = df["FamilySize"] == 1

    # Grupos de edad: niño (0-12), adolescente (13-17), adulto (18-64),
    # y adulto mayor (65 o más).
    age_bins = [-1, 12, 17, 64, float("inf")]
    age_labels = ["Niño", "Adolescente", "Adulto", "Adulto mayor"]
    df["AgeGroup"] = pd.cut(
        df["Age"], bins=age_bins, labels=age_labels, right=True
    )

    print(f"Edad: {df['Age'].isna().sum()} valores faltantes después de limpiar")
    print(f"Embarked: {df['Embarked'].isna().sum()} valores faltantes después de limpiar")
    print("Cabin: eliminada después de crear HasCabin")

    print("\n" + "=" * 70)
    print("ANÁLISIS DE SUPERVIVENCIA")
    print("=" * 70)

    survival_rate = df["Survived"].mean() * 100
    print(f"\nPorcentaje de pasajeros que sobrevivió: {survival_rate:.2f}%")

    print_survival_by(df, "Sex", "Supervivencia por sexo")
    print_survival_by(df, "Pclass", "Supervivencia por clase (Pclass)")
    print_survival_by(df, "AgeGroup", "Supervivencia por grupo de edad")

    alone_summary = (
        df.groupby("IsAlone", observed=False)["Survived"]
        .agg(Pasajeros="count", Supervivencia="mean")
        .rename(index={True: "Solo", False: "Acompañado"})
    )
    alone_summary["Supervivencia (%)"] = (
        alone_summary["Supervivencia"] * 100
    ).round(2)
    alone_summary = alone_summary.drop(columns="Supervivencia")
    print("\nSupervivencia: pasajeros solos frente a acompañados")
    print(alone_summary.to_string())

    fare_summary = df.groupby("Survived", observed=False)["Fare"].agg(
        Pasajeros="count", Media="mean", Mediana="median"
    )
    fare_summary.index = fare_summary.index.map(
        {0: "No sobrevivió", 1: "Sobrevivió"}
    )
    fare_summary[["Media", "Mediana"]] = fare_summary[["Media", "Mediana"]].round(2)
    print("\nComparación de la tarifa Fare entre supervivientes y no supervivientes")
    print(fare_summary.to_string())

    output_path = project_path / "outputs" / "resultados"
    save_survival_charts(df, output_path)


if __name__ == "__main__":
    main()
