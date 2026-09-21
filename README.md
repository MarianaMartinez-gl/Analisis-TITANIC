# Proyecto Titanic: análisis exploratorio

## Descripción

Este proyecto realiza un análisis exploratorio y una limpieza básica de los
datos de pasajeros del Titanic. El proyecto utiliza pandas para procesar los
datos y matplotlib para crear visualizaciones. No se utilizan modelos de
Machine Learning.

## Dataset

Se utiliza el archivo `data/train.csv`, correspondiente al dataset Titanic de
Kaggle:

[Titanic - Kaggle](https://www.kaggle.com/c/titanic/data)

## Objetivo

Explorar las características de los pasajeros y analizar qué grupos
presentan diferentes tasas de supervivencia, considerando sexo, clase, edad y
si viajaban solos o acompañados. También se compara la tarifa pagada por
supervivientes y no supervivientes.

## Requisitos

- Python 3.
- Las dependencias del proyecto, instaladas mediante `requirements.txt`.

El análisis utiliza pandas y matplotlib. El comando de instalación supone que
`requirements.txt` está disponible en la raíz del repositorio e incluye las
dependencias necesarias para ejecutar el análisis.

## Instalación y ejecución

### Clonar el repositorio

Reemplaza la URL de ejemplo por la URL real del repositorio:

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
cd REPOSITORIO
```

### Crear un entorno virtual

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

### Activar el entorno virtual en Windows

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En el símbolo del sistema (CMD):

```cmd
.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar el análisis

La ejecución debe hacerse desde la raíz del proyecto:

```bash
python src/analysis.py
```

El programa muestra los resultados en la terminal y guarda las visualizaciones
en `outputs/resultados/`.

## Exploración inicial

El script muestra:

- Número de pasajeros y columnas.
- Nombres de las variables.
- Tipos de datos.
- Valores faltantes y su porcentaje.
- Registros duplicados.
- Estadísticas descriptivas de las variables.

En el dataset analizado hay 891 pasajeros, 12 columnas y ningún registro
duplicado. Inicialmente, `Age` tiene 177 valores faltantes, `Cabin` tiene 687
y `Embarked` tiene 2.

## Limpieza y nuevas variables

- `Age`: los valores faltantes se rellenan con la mediana de la columna. Esta
  decisión es sencilla y evita que valores extremos influyan demasiado en el
  reemplazo.
- `Embarked`: los valores faltantes se rellenan con la moda, es decir, el
  puerto más frecuente.
- `Cabin`: no se inventan valores para las cabinas faltantes. Primero se crea
  `HasCabin`, que indica si la cabina era conocida (`True`) o no (`False`), y
  después se elimina `Cabin` del DataFrame utilizado para el análisis.
- `FamilySize`: suma `SibSp` y `Parch` y agrega el propio pasajero:
  `SibSp + Parch + 1`.
- `IsAlone`: vale `True` cuando `FamilySize` es igual a 1 y `False` cuando el
  pasajero viajaba acompañado.
- `AgeGroup`: divide la edad en cuatro categorías: `Niño` (0-12),
  `Adolescente` (13-17), `Adulto` (18-64) y `Adulto mayor` (65 o más).

## Análisis realizados

El programa calcula y muestra:

- Porcentaje general de pasajeros que sobrevivió.
- Número de pasajeros y porcentaje de supervivencia por sexo.
- Número de pasajeros y porcentaje de supervivencia por `Pclass`.
- Número de pasajeros y porcentaje de supervivencia por `AgeGroup`.
- Comparación entre pasajeros que viajaban solos y acompañados.
- Media y mediana de `Fare` para supervivientes y no supervivientes.

## Visualizaciones

El script genera cuatro archivos PNG en `outputs/resultados/`:

1. `cantidad_supervivencia.png`: cantidad de pasajeros que sobrevivieron y
   que no sobrevivieron.
2. `supervivencia_por_sexo.png`: tasa de supervivencia por sexo.
3. `supervivencia_por_clase.png`: tasa de supervivencia por clase (`Pclass`).
4. `supervivencia_por_grupo_edad.png`: tasa de supervivencia por grupo de
   edad (`AgeGroup`).

La carpeta de salida se crea automáticamente si no existe.

## Resultados y conclusiones

Los resultados se obtienen directamente de los cálculos realizados por
`src/analysis.py` sobre `data/train.csv`:

- La supervivencia general fue de **38.38%**.
- La supervivencia fue mayor entre las mujeres (**74.20%**) que entre los
  hombres (**18.89%**).
- La supervivencia disminuyó al pasar de primera clase (**62.96%**) a segunda
  (**47.28%**) y tercera clase (**24.24%**).
- El grupo `Niño` tuvo una supervivencia de **57.97%**, `Adolescente` de
  **47.73%**, `Adulto` de **36.51%** y `Adulto mayor` de **9.09%**.
- Los pasajeros acompañados tuvieron una supervivencia de **50.56%**, frente a
  **30.35%** entre quienes viajaban solos.
- La tarifa media fue **22.12** para quienes no sobrevivieron y **48.40** para
  quienes sobrevivieron. Las medianas fueron **10.50** y **26.00**,
  respectivamente.

En este dataset, los cálculos muestran una asociación descriptiva entre una
mayor supervivencia y ser mujer, viajar en una clase más alta, pertenecer a
grupos de menor edad o viajar acompañado. También muestran que los
supervivientes pagaron, en promedio y en mediana, una tarifa más alta. Estas
son conclusiones descriptivas del dataset; el proyecto no pretende demostrar
causalidad ni construir un modelo predictivo.
