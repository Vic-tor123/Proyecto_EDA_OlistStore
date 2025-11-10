#tratamiento de datos
import pandas as pd

def convertir_a_datetime(df, columnas):
    """
    Que realiza la funcion 
        Convierte a formato datetime las columnas especificadas de un DataFrame.
      
    Que incluye la conversion
         - Convierte las columnas de tipo object o string a datetime.
         - Utiliza 'errors="coerce"' para transformar valores no válidos en NaT.
         - Aplica la conversión solo a las columnas indicadas por el usuario.  
    
    Parametros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la conversión.
    columnas (list): Lista con los nombres de las columnas a convertir.

    Returns
    None    
    """
    for col in columnas:
        df[col] = pd.to_datetime(df[col], errors='coerce')

def corregir_columnas_y_categorias(df):
    """
    Que realiza la funcion 
        Corrige nombres de columnas y valores específicos dentro del data frame.
      
    Que incluye la correccion
         - Reemplaza la categoría 
         - Renombra columnas mal escritas:
              

    Parametros:
    df (pd.DataFrame): DataFrame al que se aplicarán las correcciones.

    Returns
    None    
    """
    # Cambiar categoría
    if 'payment_type' in df.columns:
        df['payment_type'] = df['payment_type'].replace('boleto', 'bank_slip')

    # Renombrar columnas si existen
    df.rename(columns={
        'product_name_lenght': 'product_name_length',
        'product_description_lenght': 'product_description_length'
    }, inplace=True)


def convertir_a_int(df, columnas):
    """
    Que realiza la funcion 
        Convierte a formato entero (int) las columnas especificadas de un DataFrame.
      
    Que incluye la conversion
         - Convierte columnas a tipo int, si es posible.
         - Valores que no se puedan convertir se transforman en NaN automáticamente.
         - Aplica la conversión solo a las columnas indicadas por el usuario.  
    
    Parametros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la conversión.
    columnas (list): Lista con los nombres de las columnas a convertir.

    Returns
    None    
    """
    for col in columnas:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')

def minusculas(df, columnas):
    """
    Que realiza la funcion 
        Convierte a minúsculas todas las columnas de tipo object (string) de un DataFrame.
      
    Que incluye la conversion
         - Aplica str.lower() a todas las columnas de tipo object.
    
    Parametros:
    df (pd.DataFrame): DataFrame sobre el que se aplicará la conversión.

    Returns
    None    
    """
    for col in columnas:
        df[col] = df[col].str.lower()