#tratamiento de datos
import pandas as pd
import numpy as np

#visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt



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