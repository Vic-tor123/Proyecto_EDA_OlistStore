#tratamiento de datos
import pandas as pd

def eda_rapido(df):
    """
    Que realiza la funcion 
        Realiza un análisis exploratorio rápido del data frame
    Que incluye el analisis
      - 5 filas aleatorias
      - Info general (tipos, nulos)
      - Porcentaje de valores nulos
      - Estadísticos de columnas numéricas
    """
    print('MUESTRA:')
    display(df.sample(5))
    print('------------------------')

    print('INFO:')
    display(df.info())
    print('------------------------')

    print('NULOS:')
    display(df.isnull().mean() * 100)
    print('------------------------')

    print('ESTADISTICOS NUMERICAS:')
    display(df.describe().T)



def eda_preliminar(df):
    """
    Que realiza la funcion 
        Realiza un analisis exploratorion preliminar sobre un DataFrame dado.
      
    Que incluye el analisis
         -Muestra aleatoria de 5 filas del DataFrame
         -Informacion general del DataFrame  (tipo de datos, nulos, etc.)
         - Porcentaje de valores nulos por columna.
         -Conteo de filas duplicadas.
         -Distribucion de valores para columnas categoricas.     
    
    Parametros:
    df (pd,DataFrame): DataFrame a analizar.

    Returns
    None    
    """
    
    display (df.sample(5))
    print ('------------------------')
    print ('DIMENSIONES')
    print (f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')
    print ('------------------------')
    print ('INFO')
    display (df.info())              
    print ('------------------------')
    print ('NULOS')
    display (df.isnull().mean()*100)
    print ('------------------------')
    print ('DUPLICADOS')
    print (df.duplicated().sum())
    print ('------------------------')
    print ('FRECUENCIA CATEGORICAS')
    for col in df.select_dtypes(include='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print ('------------------------')
    print ('------------------------')
    print ('ESTADISTICOS NUMERICAS')
    display(df.describe().T)

    