**Análisis Exploratorio de Datos del Titanic**

Este proyecto realiza un análisis exploratorio del dataset **Titanic**, utilizando Python y diferentes técnicas de análisis y visualización de datos. El objetivo es conocer las características de los pasajeros del Titanic e identificar patrones relacionados con su supervivencia.


**Titanic — train.csv**

### Fuente

El dataset fue obtenido de **Kaggle**, en la competencia Titanic:

https://www.kaggle.com/c/titanic/data

### Descripción

El dataset contiene información sobre los pasajeros del Titanic. Entre las variables disponibles se encuentran:

* `PassengerId`: identificador del pasajero.
* `Survived`: indica si el pasajero sobrevivió.
* `Pclass`: clase del pasajero.
* `Name`: nombre del pasajero.
* `Sex`: sexo del pasajero.
* `Age`: edad.
* `SibSp`: número de hermanos o cónyuges a bordo.
* `Parch`: número de padres o hijos a bordo.
* `Ticket`: número del boleto.
* `Fare`: tarifa pagada.
* `Cabin`: número de cabina.
* `Embarked`: puerto de embarque.

El archivo utilizado principalmente en este proyecto es `train.csv`.

---

## Objetivo

El objetivo del proyecto es realizar un **análisis exploratorio de los datos del Titanic** para conocer las características de los pasajeros y analizar la relación entre diferentes variables y la supervivencia.

Se busca identificar patrones relacionados con:

* Sexo de los pasajeros.
* Edad.
* Clase del pasajero.
* Tarifa pagada.
* Número de familiares a bordo.
* Supervivencia.
* Datos faltantes.

No se pretende construir modelos predictivos de Machine Learning.

---

## Requisitos

Para ejecutar este proyecto se requiere:

* **Python 3**
* Las dependencias indicadas en el archivo `requirements.txt`.

Las principales librerías utilizadas son:

* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar al proyecto

```bash
cd nombre-del-repositorio
```

### 3. Crear el entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En **Windows**:

```bash
.venv\Scripts\activate
```

En **Linux o macOS**:

```bash
source .venv/bin/activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

Después de instalar las dependencias y activar el entorno virtual, ejecutar el análisis con:

```bash
python src/analysis.py
```

El programa leerá el archivo:

```text
data/train.csv
```

y realizará los análisis definidos en el archivo `analysis.py`.

Los resultados y gráficos generados se almacenarán en:

```text
outputs/resultados/
```

---

## Análisis realizados

En este proyecto se realizaron diferentes análisis exploratorios, entre ellos:

### 1. Exploración del dataset

Se revisó:

* Número de filas y columnas.
* Tipos de datos.
* Primeros registros.
* Estadísticas descriptivas.

### 2. Datos faltantes

Se identificaron las columnas que contienen valores faltantes y se analizó la cantidad de datos ausentes.

### 3. Análisis de supervivencia

Se analizó la cantidad de pasajeros que sobrevivieron y los que no sobrevivieron.

### 4. Supervivencia por sexo

Se comparó la supervivencia entre hombres y mujeres.

### 5. Supervivencia por clase

Se analizó la relación entre la clase del pasajero (`Pclass`) y la supervivencia.

### 6. Distribución de edades

Se analizó la distribución de las edades de los pasajeros mediante gráficos.

### 7. Análisis de tarifas

Se estudió la distribución de las tarifas (`Fare`) pagadas por los pasajeros.

### 8. Visualización de datos

Se utilizaron gráficos para facilitar la interpretación de los resultados, incluyendo:

* Gráficos de barras.
* Histogramas.
* Gráficos circulares.
* Gráficos de dispersión.
* Gráficos relacionados con la supervivencia.

---

## Resultados y conclusiones

El análisis exploratorio permite observar diferentes patrones dentro de los pasajeros del Titanic.

Entre los principales hallazgos se encuentran:

* La supervivencia no fue igual para todos los pasajeros.
* Se observaron diferencias importantes en la supervivencia entre hombres y mujeres.
* La clase del pasajero presentó una relación con la supervivencia.
* La edad de los pasajeros presentó diferentes distribuciones entre los grupos analizados.
* Las tarifas pagadas variaron considerablemente entre los pasajeros.
* El dataset contiene valores faltantes, especialmente en variables como `Age` y `Cabin`, que deben considerarse durante el análisis.

En conclusión, el análisis exploratorio permite comprender mejor las características de los pasajeros del Titanic y observar relaciones entre variables como **sexo, edad, clase, tarifa y supervivencia**, sin utilizar modelos de Machine Learning.

---

## Estructura del proyecto

```text
nombre-proyecto/
│
├── data/
│   └── train.csv
│
├── src/
│   └── analysis.py
│
├── outputs/
│   └── resultados/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Git
* GitHub
