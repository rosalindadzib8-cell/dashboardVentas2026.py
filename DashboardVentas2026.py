import streamlit as st
import pandas as pd

# Assuming df_ventas is already loaded from the previous steps
# If you were running this script independently, you'd reload the data like this:
file_path = 'datos/SalidaVentas.xlsx'
df_ventas = pd.read_excel(file_path)

st.set_page_config(layout='wide')
st.title('Sales Dashboard for USA Regions')

# Overall KPIs
st.subheader('Overall Sales Performance')

col1, col2 = st.columns(2)

with col1:
    total_sales = df_ventas['Sales'].sum()
    st.metric(label="Total Sales", value=f"${total_sales:,.2f}")

with col2:
    total_profit = df_ventas['Profit'].sum()
    st.metric(label="Total Profit", value=f"${total_profit:,.2f}")

# Sidebar for filters
st.sidebar.header('Filter Options')
selected_region = st.sidebar.multiselect(
    'Select Region(s)',
    options=df_ventas['Region'].unique(),
    default=df_ventas['Region'].unique()
)

# Filter DataFrame based on selected region(s)
df_filtered = df_ventas[df_ventas['Region'].isin(selected_region)]

st.subheader('Sales and Profit by Region (Filtered)')

if not df_filtered.empty:
    sales_by_region = df_filtered.groupby('Region')['Sales'].sum().reset_index()
    profit_by_region = df_filtered.groupby('Region')['Profit'].sum().reset_index()

    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.write("Sales by Region:")
        st.bar_chart(sales_by_region.set_index('Region'))

    with col_chart2:
        st.write("Profit by Region:")
        st.bar_chart(profit_by_region.set_index('Region'))

else:
    st.write("No data to display for the selected regions.")

st.subheader('Raw Data Preview (Filtered)')
st.dataframe(df_filtered.head())
