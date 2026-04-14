import streamlit as st
import pandas as pd

# Título del dashboard
st.title('Dashboard de Ventas')

# Cargar los datos
@st.cache_data
def load_data():
    file_path = 'datos/SalidaVentas.xlsx'
    df = pd.read_excel(file_path)
    return df

df_ventas_dashboard = load_data()

st.subheader('Vista Previa de los Datos')
st.write(df_ventas_dashboard.head())

st.subheader('Estadísticas Descriptivas')
st.write(df_ventas_dashboard.describe())

st.subheader('Distribución por Región')
region_counts = df_ventas_dashboard['Region'].value_counts()
st.bar_chart(region_counts)

st.subheader('Ventas por Categoría')
category_sales = df_ventas_dashboard.groupby('Category')['Sales'].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

st.subheader('Ventas por Modo de Envío')
ship_mode_sales = df_ventas_dashboard.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
st.bar_chart(ship_mode_sales)
