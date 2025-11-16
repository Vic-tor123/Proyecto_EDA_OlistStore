#tratamiento de datos
import pandas as pd
import numpy as np

#visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import json


def subplot_col_cat(df, exclude_cols=None):
    """
    Qué realiza la función  
        Genera gráficos de barras para columnas categóricas, excluyendo IDs.
      
    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se generarán los gráficos.
    exclude_cols (list): Lista de columnas a excluir (default: IDs).

    Returns:
    None
    """
    # Columnas a excluir por defecto (IDs)
    if exclude_cols is None:
        exclude_cols = ['order_id', 'customer_id', 'product_id', 'seller_id', 'review_id']
    
    # Seleccionar columnas categóricas excluyendo IDs
    categorical_cols = [col for col in df.select_dtypes(include=['object','category']).columns 
                       if col not in exclude_cols]
    
    if len(categorical_cols) == 0:
        print("No hay columnas categóricas en el DataFrame.")
        return
    
    # Configurar el tamaño de la figura
    num_cols = len(categorical_cols)
    rows = (num_cols + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten()

    # Generar gráficos para cada columna categórica
    for i, col in enumerate(categorical_cols):
        # Limitar a TOP 20 si hay muchas categorías
        if df[col].nunique() > 20:
            top_cats = df[col].value_counts().head(20).index
            df_plot = df[df[col].isin(top_cats)]
        else:
            df_plot = df
            
        sns.countplot(data=df_plot, x=col, ax=axes[i], hue=col, palette="rocket", legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=45)

                # Rotación específica para 'product_category_name'
        if col == 'product_category_name_english':
            axes[i].tick_params(axis='x', rotation=90)
        else:
            axes[i].tick_params(axis='x', rotation=45)
 
    # Eliminar ejes sobrantes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def subplot_col_num(df):
    """
    Qué realiza la función:
        - Identifica todas las columnas numéricas del DataFrame.
        - Para cada columna, genera:
            1. Un histograma con 200 bins mostrando la distribución de los valores.
            2. Un boxplot para visualizar posibles outliers.
        - Cada columna utiliza un color distinto de la paleta 'rocket' para mantener consistencia visual.
        - Ajusta automáticamente el tamaño de la figura según el número de columnas.
        - Elimina ejes sobrantes si hay más subplots que columnas.

    Parámetros:
        df (pd.DataFrame): DataFrame sobre el que se generarán los gráficos.

    Retorna:
        None: La función muestra los gráficos directamente y no devuelve valores.

    Uso:
        subplot_col_num(df_no_nulos)
    """


    col_nums = df.select_dtypes(include='number').columns
    num_graph = len(col_nums)

    # Extraer colores de la paleta rocket
    rocket_colors = sns.color_palette('rocket', num_graph)

    num_rows = (num_graph + 2) // 2
    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows * 5))

    for i, col in enumerate(col_nums):
        color = rocket_colors[i]  # color de la columna i

        # Histograma con color
        sns.histplot(data=df, x=col, ax=axes[i,0], bins=200, color=color)
        axes[i,0].set_title(f'Distribucion de {col}')
        axes[i,0].set_xlabel(col)
        axes[i,0].set_ylabel('Frecuencia')
        
        # Boxplot con color
        sns.boxplot(data=df, x=col, ax=axes[i,1], color=color)
        axes[i,1].set_title(f'Boxplot de {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def matriz_correlacion(df):
    """
    Qué realiza la función  
        Calcula y visualiza la matriz de correlación entre las columnas numéricas del DataFrame.  
      
    Qué incluye el análisis  
        - Calcula la correlación de Pearson entre todas las columnas numéricas.  
        - Genera un gráfico de mapa de calor (heatmap) usando seaborn.  
        - Muestra solo la mitad superior de la matriz para mayor claridad.  
        - Los valores se anotan y se colorean según la intensidad de correlación (-1 a 1).  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se calculará la matriz de correlación.

    Returns:
    None
    """
    #calcular matriz de correlacion
    corr_matrix = df.corr(numeric_only=True)
    #crear la figura
    plt.figure(figsize=corr_matrix.shape)

    # crear una mascara para mostrar solo la parte triangular
    mask = np.triu(np.ones_like(corr_matrix,dtype=bool))

    #Graficar el mapa de calor
    sns.heatmap(corr_matrix,annot=True,vmin=-1,vmax=1,cmap='cool', mask=mask)
    plt.show()





def lineplot_mensual(df, eje_x, eje_y, agregacion="count", figsize=(6,4), color="#6A176E", rotation=45):
    """
    Genera un gráfico de línea mensual a partir de un DataFrame con fechas,
    permitiendo elegir entre conteo (count), suma (sum) o media (mean).
    """

    if agregacion == "count":
        df_plot = df.groupby(df[eje_x].dt.to_period('M'))[eje_y].count().reset_index()
    
    elif agregacion == "sum":
        df_plot = df.groupby(df[eje_x].dt.to_period('M'))[eje_y].sum().reset_index()
    
    elif agregacion == "mean":
        df_plot = df.groupby(df[eje_x].dt.to_period('M'))[eje_y].mean().reset_index()
    
    else:
        raise ValueError("agregacion debe ser 'count', 'sum' o 'mean'")

    df_plot[eje_x] = df_plot[eje_x].dt.to_timestamp()

    plt.figure(figsize=figsize)
    sns.lineplot(
        x=eje_x,
        y=eje_y,
        data=df_plot,
        marker="o",
        color=color
    )
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()


def objetivo_vs_categoricas(df, variables_relevantes, target):
    """
    Qué realiza la función:
        Calcula y visualiza la relación entre un target y variables categóricas.
        La función detecta automáticamente si el target es numérico o categórico:
            - Si el target es numérico → calcula el promedio por categoría.
            - Si el target es categórico con valores 'yes'/'no' → calcula la tasa de conversión (%).

    Qué incluye la visualización:
        - Gráficos de barras ordenados de mayor a menor valor.
        - Paleta 'rocket' aplicada por categoría.
        - Valores numéricos encima de cada barra.
        - Ajuste automático del ancho de la figura según el número de categorías.

    Parámetros:
        df (pd.DataFrame): DataFrame que contiene los datos.
        variables_relevantes (list): Lista de columnas categóricas a analizar.
        target (str): Nombre de la columna objetivo. Puede ser numérica o categórica tipo 'yes'/'no'.

    Returns:
        None
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    for col in variables_relevantes:
        if df[target].dtype in ['int64','float64']:
            # Target numérico → calcular promedio
            valores = df.groupby(col)[target].mean().sort_values(ascending=False)
            ylabel = f'Promedio de {target}'
        else:
            # Target categórico 'yes'/'no' → calcular tasa de conversión
            valores = df.groupby(col)[target].apply(lambda x: (x == 'yes').sum() / len(x) * 100).sort_values(ascending=False)
            ylabel = f'Tasa de conversión (%) de {target}'

        print(f"--------------------------------")
        print(f"{ylabel} por {col.upper()}")
        print(f"--------------------------------")
        print(valores.round(2))
        
        # Gráfico
        num_cats = df[col].nunique()
        fig_width = max(6, num_cats * 1.2)
        plt.figure(figsize=(fig_width, 5))
        
        sns.barplot(
            x=valores.index,
            y=valores.values,
            hue=valores.index,
            dodge=False,
            palette='rocket',
            legend=False
        )
        
        plt.title(f'{ylabel} por {col}')
        plt.ylabel(ylabel)
        plt.xlabel(col)
        plt.xticks(rotation=45, ha='right')
        
        # Añadir valores encima de las barras
        for i, v in enumerate(valores):
            plt.text(i, v + 0.5, f'{v:.1f}', ha='center', fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        plt.show()


def mapa_coropletas_estado(df, columna_estado, columna_conteo, columna_suma):
    """
    Genera un mapa coroplético de Brasil por estado, utilizando un GeoJSON 
    externo y datos agregados del DataFrame.

    Qué realiza la función:
        - Carga dinámicamente el GeoJSON oficial de estados de Brasil.
        - Agrega los datos por la columna de estado indicada.
        - Crea un mapa coroplético usando Plotly basado en el conteo o suma de variables.
        - Normaliza automáticamente los códigos de estado a mayúsculas.

    Qué incluye la visualización:
        - Mapa coroplético coloreado según el conteo de registros (columna_conteo).
        - Escala de colores continua.
        - Ajuste automático al área geográfica relevante.

    Parámetros:
        df (pd.DataFrame): DataFrame con los datos.
        columna_estado (str): Nombre de la columna que contiene los estados (ej: 'customer_state').
        columna_conteo (str): Columna a contar por estado (ej: 'order_id').
        columna_suma (str): Columna a sumar por estado (ej: 'payment_value_knn').

    Returns:
        None (muestra el mapa interactivo en pantalla).
    """
    import requests
    import plotly.express as px

    # 1. Cargar geojson de estados de Brasil
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    geojson = requests.get(url).json()

    # 2. Agregación por estado
    df_agg = df.groupby(columna_estado).agg({
        columna_conteo: 'count',
        columna_suma: 'sum'
    }).reset_index()

    # Normalizar mayúsculas
    df_agg[columna_estado] = df_agg[columna_estado].str.upper()

    # 3. Crear mapa
    fig = px.choropleth(
        df_agg,
        geojson=geojson,
        locations=columna_estado,
        featureidkey="properties.sigla",
        color=columna_conteo,
        color_continuous_scale="Purples",
        scope="south america"
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.show()        