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
    id_cols = ['order_id', 'customer_id', 'product_id', 'seller_id', 'review_id']

    cols_sin_id = [c for c in df.columns if c not in id_cols]

    # SAMPLE sin IDs
    display(df[cols_sin_id].sample(5))
    print('------------------------')

    print('DIMENSIONES')
    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')
    print('------------------------')

    print('INFO (sin ID)')
    display(df[cols_sin_id].info())
    print('------------------------')

    print('NULOS')
    display(df[cols_sin_id].isnull().mean() * 100)
    print('------------------------')

    print('DUPLICADOS')
    print(df.duplicated().sum())
    print('------------------------')

    print('FRECUENCIA CATEGORICAS')
    for col in df.select_dtypes(include="object").columns:
        if col not in id_cols:
            print(col.upper())
            print(df[col].value_counts())
            print('------------------------')

    print('ESTADISTICOS NUMERICAS')
    display(df.describe().T) 


    