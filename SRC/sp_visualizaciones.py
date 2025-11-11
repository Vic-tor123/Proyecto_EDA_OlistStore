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

