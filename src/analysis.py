"""Análisis exploratorio y limpieza básica del dataset Titanic."""

from pathlib import Path

import pandas as pd


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


if __name__ == "__main__":
    main()
