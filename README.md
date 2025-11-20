# Proyecto E-commerce Olist (EDA)
## Descripción del Proyecto


Este proyecto presenta un análisis exploratorio de datos (EDA) completo del dataset público de Olist, una plataforma de comercio electrónico brasileña. 

El objetivo es extraer insights sobre el comportamiento de compra, satisfacción del cliente, distribución geográfica de ventas y patrones temporales del negocio durante el período 2016-2018. 

El dataset original comprende 9 archivos CSV interrelacionados con aproximadamente 120,000 registros que, tras un proceso de unificación y limpieza, resultan en 104,243 pedidos completados analizados a través de 28 variables consolidadas. 

El análisis utiliza técnicas de imputación de valores nulos (KNN Imputer e Iterative Imputer), análisis estadístico descriptivo y visualización de datos, culminando con un dashboard interactivo en Excel que permite explorar dinámicamente los KPIs más relevantes del negocio.


El análisis culmina con un dashboard interactivo en Excel que permite visualizar los KPIs más relevantes y explorar los datos de forma dinámica mediante filtros.

##  Objetivos del Análisis

1. **Comprender el comportamiento del cliente:** Métodos de pago preferidos, distribución geográfica, categorías más demandadas
2. **Evaluar la satisfacción del cliente:** Análisis del review score y factores que lo afectan
3. **Identificar patrones temporales:** Evolución de ventas, estacionalidad y tendencias
4. **Analizar la operación logística:** Tiempos de entrega, concentración de vendedores y tasas de éxito
5. **Detectar oportunidades de mejora:** Regiones desatendidas, categorías con baja satisfacción


##  Estructura del Proyecto

```
PROYECTO_EDA_OLISTORE
│
├── datos/
│   ├── olist_unificado.csv           # Dataset tras la unificación de los datos de los distintos csv
│   ├── olist_datos.csv               # Datos tras tratamiento preliminar previo a limpieza
│   ├── olist_limpios.csv             # Dataset tras la limpieza de datos
│   ├── df_data_no_nulos.csv          # Dataset limpio después del tratamiento de nulos
│   └── olist_dashboard.xlsx          # Datos exportados a excel para el dashboard interactivo final
│   
│
├── datos_originales/                       # 9 documentos CSV, deben ser importados desde Kaggle
│   ├── olist_customers_dataset.csv         # Datos de clientes
│   ├── olist_geolocation_dataset.csv       # Información geográfica
│   ├── olist_order_items_dataset.csv       # Detalles de los productos por pedido
│   ├── olist_order_payments_dataset.csv    # Información de pagos
│   ├── olist_order_reviews_dataset.csv     # Opiniones y puntuaciones de pedidos
│   ├── olist_orders_dataset.csv            # Pedidos realizados
│   ├── olist_products_dataset.csv          # Datos de productos
│   ├── olist_sellers_dataset.csv           # Información de vendedores
│   └── product_category_name_translation.csv  # Traducción de categorías de productos
│
├── notebooks/
│   ├── unificacion_csv.ipynb         # Jupyter notebook en el que se lleva a cabo la unificacion de varios csv
│   ├── eda_preliminar.ipynb          # Jupyter notebook en el que se realiza un primer acercamiento a los datos 
│   ├── limpieza.ipynb                # Jupyter notebook con la limpieza de los datos
│   ├── nulos.ipynb                   # Jupyter con el tratamiento de nulos 
│   └── analisis.ipynb                # Analisis con los datos ya limpios
│    
├── SRC/
│   ├── sp_eda.py                     # Script con el análisis exploratorio inicial: estadísticas básicas y revisión general del dataset.
│   ├── sp_limpieza.py                # Procesos de depuración: eliminación de duplicados, estandarización y corrección de valores.
│   ├── sp_nulos.py                   # Identificación y tratamiento de valores faltantes según su impacto en el análisis.
│   └── sp_visualizaciones.py         # Gráficos y representaciones visuales utilizados para interpretar los principales hallazgos.
│    
├──imagenes/
│   ├── portada.png                   # Portada del proyecto
│   └── dashboard.png                 # Imágen del dashboard
│
├── .gitignore                        # Lista de archivos a ignorar por Git
│
├── README.md
└── requirements.txt
```

##  Instalación y Requisitos

### 1. Obtención de los Datos

**Nota:** Los datos originales no están incluidos en este repositorio. Deben descargarse directamente desde Kaggle:

👉 **[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**

**Pasos:**
1. Accede al enlace de Kaggle
2. Descarga el dataset completo (puede requerir crear una cuenta gratuita)
3. Extrae los archivos CSV en la carpeta `datos_originales/` del proyecto

### 2. Herramientas

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- openpyxl
- Jupyter Notebook / JupyterLab
- Visual Studio Code
- Git / GitHub

**Instalación:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

O mediante el archivo de requisitos:
```bash
pip install -r requirements.txt
```


##  Estructura de Datos

El dataset consolidado contiene **41 variables** organizadas en las siguientes categorías:

### **Información del Pedido**
- **order_id**: Identificador único del pedido
- **order_status**: Estado del pedido (entregado, cancelado, en tránsito, etc.)
- **order_purchase_timestamp**: Fecha y hora de compra del pedido
- **order_approved_at**: Fecha y hora de aprobación del pedido
- **order_delivered_carrier_date**: Fecha de entrega del pedido al transportista
- **order_delivered_customer_date**: Fecha de entrega del pedido al cliente
- **order_estimated_delivery_date**: Fecha estimada de entrega
- **order_item_id**: Identificador del producto dentro del pedido
- **shipping_limit_date**: Fecha límite de envío

### **Información del Producto**
- **product_id**: Identificador único del producto
- **product_category_name**: Categoría del producto
- **product_name_lenght**: Longitud del nombre del producto (caracteres)
- **product_description_lenght**: Longitud de la descripción del producto (caracteres)
- **product_photos_qty**: Cantidad de fotos del producto
- **product_weight_g**: Peso del producto en gramos
- **product_length_cm**: Largo del producto en centímetros
- **product_height_cm**: Alto del producto en centímetros
- **product_width_cm**: Ancho del producto en centímetros

### **Información del Cliente**
- **customer_id**: Identificador del cliente en el pedido
- **customer_unique_id**: Identificador único del cliente
- **customer_zip_code_prefix**: Código postal del cliente
- **customer_city**: Ciudad del cliente
- **customer_state**: Estado (región) del cliente

### **Información del Vendedor**
- **seller_id**: Identificador único del vendedor
- **seller_zip_code_prefix**: Código postal del vendedor
- **seller_city**: Ciudad del vendedor
- **seller_state**: Estado (región) del vendedor

### **Información de Pago**
- **payment_sequential**: Número secuencial del método de pago usado
- **payment_type**: Tipo de pago (tarjeta crédito, débito, bank_slip, voucher)
- **payment_installments**: Número de cuotas del pago
- **payment_value**: Valor total del pago (precio + envío)
- **price**: Precio del producto
- **freight_value**: Costo del envío

### **Información de Reseñas**
- **review_id**: Identificador único de la reseña
- **review_score**: Puntuación de satisfacción del cliente (1-5 estrellas)
- **review_comment_title**: Título del comentario de la reseña
- **review_comment_message**: Mensaje completo de la reseña
- **review_creation_date**: Fecha de creación de la reseña
- **review_answer_timestamp**: Fecha de respuesta a la reseña

### **Información Geográfica**
- **geolocation_lat**: Latitud geográfica
- **geolocation_lng**: Longitud geográfica


## Resultados y Conclusiones

### **Principales Hallazgos:**

**Operación Logística:**
- Tasa de entrega exitosa del **99.99%** (104,236 de 104,243 pedidos completados)
- Tiempo promedio de entrega: 10-15 días
- Fuerte concentración geográfica: São Paulo representa el 42% de clientes y 71% de vendedores

**Comportamiento de Compra:**
- **74.5%** de pagos realizados con tarjeta de crédito
- Ticket promedio: R$157 (31 USD)
- Precio promedio de productos: R$124 (25 USD)

**Satisfacción del Cliente:**
- Rating promedio: **4.12/5 estrellas**
- **58.1%** de clientes otorgan 5 estrellas (máxima satisfacción)
- Solo 10.4% otorgan 1 estrella (muy insatisfechos)

**Categorías de Productos:**
- TOP 5 categorías representan el **39.9%** de las ventas
- Categorías líderes: bed_bath_table (10.2%), health_beauty (8.7%), sports_leisure (7.6%)
- Productos pequeños y digitales generan mayor satisfacción que productos grandes

**Insight Clave:**
- **La satisfacción NO depende del precio** (correlación 0). Los factores más relevantes son el tiempo de entrega y la ubicación geográfica del cliente.



##  Próximos Pasos

- Realizar un **análisis regional detallado** para comparar el desempeño entre norte y sur de Brasil
- **Estudio por categoría** para identificar factores específicos que impactan la satisfacción (peso, precio, tiempo de entrega)
- **Análisis de mejores prácticas de vendedores** para crear programas de capacitación basados en vendedores exitosos
- Explorar la **estacionalidad** con modelos de series temporales para proyectar demanda futura

---

##  Contribuciones

Si tienes alguna propuesta o corrección, no dudes en compartirla. Cualquier tipo de colaboración, ya sea en forma de código, documentación o comentarios, será apreciada y considerada. ¡Gracias por tu participación!

## Autor


* GitHub [Vic-tor123](https://github.com/Vic-tor123)
* LinkedIn [Vic-tor123LinkedIn](https://www.linkedin.com/in/Vic-tor123LinkedIn/)





