# E-commerce Olist (EDA)
## Descripción del Proyecto
Este proyecto presenta un análisis exploratorio de datos (EDA) completo del dataset público de **Olist**, una plataforma de comercio electrónico brasileña. El objetivo es extraer insights sobre el comportamiento de compra, satisfacción del cliente, distribución geográfica de ventas y patrones temporales del negocio durante el período 2016-2018.

El análisis culmina con un **dashboard interactivo en Excel** que permite visualizar los KPIs más relevantes y explorar los datos de forma dinámica mediante filtros.

##  Objetivos del Análisis

1. **Comprender el comportamiento del cliente:** Métodos de pago preferidos, distribución geográfica, categorías más demandadas
2. **Evaluar la satisfacción del cliente:** Análisis del review score y factores que lo afectan
3. **Identificar patrones temporales:** Evolución de ventas, estacionalidad y tendencias
4. **Analizar la operación logística:** Tiempos de entrega, concentración de vendedores y tasas de éxito
5. **Detectar oportunidades de mejora:** Regiones desatendidas, categorías con baja satisfacción

---
##  Estructura del Proyecto

```
PROYECTO_EDA_OLISTORE
│
├── datos/
│   ├── olist_unificado.csv           # Dataset tras la unificación de los datos de los distintos csv
│   ├── olist_datos.csv               # Datos tras tratamiento preliminar previo a limpieza
│   ├── olist_limpios.csv             # Dataset tras la limpieza de datos
│   ├── df_data_no_nulos.csv          # Dataset limpio después del tratamiento de nulos
│   └── olist_dashboard.xlsx          # Datos exportados para el dashboard interactivo final
│   
│
├── datos_originales/                 # 9 documentos CSV, deben ser importados desde Kaggle
│
│
├── notebooks/
│   ├── unificacion_csv.ipynb
│   ├── eda_preliminar.ipynb
│   ├── limpieza.ipynb
│   ├── nulos.ipynb
│   └── analisis.ipynb    
│    
│
├── documentos/
│   ├── analisis_eda.pdf              # Informe detallado del análisis
│   └── word_analisis_eda.pdf         # Documento de explicación del proyecto
│
├── dashboard/
│   └── dashboard_olist.xlsx          
│
├── README.md
└── requirements.txt
```

---