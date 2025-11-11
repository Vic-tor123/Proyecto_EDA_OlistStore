#tratamiento de datos
import pandas as pd

#visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns




def estadist_col_cat (df): 
    """
    Qué realiza la función  
        Calcula y muestra la distribución porcentual de valores para todas las columnas categóricas del DataFrame.  
      
    Qué incluye el análisis  
        - Recorre todas las columnas de tipo texto (object).  
        - Imprime el nombre de la columna en mayúsculas.  
        - Muestra el porcentaje de cada categoría respecto al total de registros.  
        - Separa cada columna con una línea divisoria para mayor claridad.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se realizará el análisis.

    Returns:
    None
    """
    for col in df.select_dtypes(include='O').columns:
        print (col.upper())
        print (df[col].value_counts()/df.shape[0]*100)
        print('------------------------')         