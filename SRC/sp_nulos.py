#tratamiento de datos
import pandas as pd

#visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns




def estadist_col_cat (df): 
    """
    Qué realiza la función  
        Calcula y muestra la distribución porcentual de valores para todas las columnas categóricas del DataFrame. Excluyendo las columnas ID  
        
    Qué incluye el análisis  
        - Recorre todas las columnas de tipo texto (object) excluyendo las columnas ID  
        - Imprime el nombre de la columna en mayúsculas.  
        - Muestra el porcentaje de cada categoría respecto al total de registros.  
        - Separa cada columna con una línea divisoria para mayor claridad.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se realizará el análisis.

    Returns:
    None
    """
    id_cols = ['order_id', 'customer_id', 'product_id', 'seller_id', 'review_id']
    
    for col in df.select_dtypes(include='O').columns:
        if col not in id_cols:
            print (col.upper())
            print (df[col].value_counts()/df.shape[0]*100)
            print('------------------------')         