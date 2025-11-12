#tratamiento de datos
import pandas as pd

#visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns

#imputacion de datos
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, IterativeImputer



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



def calculo_outliers (df, cols):
    """
    Qué realiza la función  
        Calcula y muestra la cantidad y el porcentaje de outliers para columnas numéricas especificadas en el DataFrame.  
      
    Qué incluye el análisis  
        - Para cada columna, calcula el rango intercuartílico (IQR).  
        - Define los límites inferior y superior como Q1 - 1.5*IQR y Q3 + 1.5*IQR.  
        - Identifica los registros que están fuera de estos límites como outliers.  
        - Imprime el número total de outliers y su porcentaje respecto al total de filas.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se realizará el cálculo.  
    cols (list): Lista de nombres de columnas numéricas a analizar.

    Returns:
    None
    """
    for col in cols:
        q_75 = df[col].quantile(0.75)
        q_25 = df[col].quantile(0.25)
        rango_itq = q_75 - q_25
        inferior = q_25 - (rango_itq*1.5)
        superior = q_75 + (rango_itq*1.5) 
        outliers = df[(df[col]<inferior) | (df[col]>superior)]
        num_outliers = len(outliers)

        per_outliers = num_outliers/df.shape[0]*100
        print(f'En la columna {col.upper()} tenenemos un total de {num_outliers} outliers, lo que representa un {per_outliers}% del total') 




def imputar_iterative(df, lista_columnas):
    """
    Qué realiza la función  
        Imputa valores faltantes en columnas numéricas utilizando el método Iterative Imputer.  
      
    Qué incluye la transformación  
        - Aplica IterativeImputer con un máximo de 50 iteraciones y semilla fija para reproducibilidad.  
        - Genera nuevas columnas con el sufijo '_iterative' que contienen los valores imputados.  
        - Muestra un resumen estadístico (describe) de las columnas imputadas.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la imputación.  
    lista_columnas (list): Lista de nombres de columnas numéricas a imputar.

    Returns:
    pd.DataFrame: DataFrame original con nuevas columnas imputadas añadidas.
    """
    iter_imputer = IterativeImputer (max_iter=50,random_state=42)
    data_imputed = iter_imputer.fit_transform(df[lista_columnas])
    new_col = [col +"_iterative" for col in lista_columnas]
    df[new_col]= data_imputed
    display(df[new_col].describe().T)
    return df      




def imputar_knn(df, lista_columnas):
    """
    Qué realiza la función  
        Imputa valores faltantes en columnas numéricas utilizando el método KNN Imputer.  
      
    Qué incluye la transformación  
        - Aplica KNNImputer con 5 vecinos para estimar los valores faltantes.  
        - Genera nuevas columnas con el sufijo '_knn' que contienen los valores imputados.  

    Parámetros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la imputación.  
    lista_columnas (list): Lista de nombres de columnas numéricas a imputar.

    Returns:
    pd.DataFrame: DataFrame original con nuevas columnas imputadas añadidas.
    """
    knn_imputer = KNNImputer (n_neighbors=5)
    data_imputed = knn_imputer.fit_transform(df[lista_columnas])
    new_col = [col +"_knn" for col in lista_columnas]
    df[new_col]= data_imputed
    return df