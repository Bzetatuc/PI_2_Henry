
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
try:
    df_crypto_dashboard = pd.read_csv('/Users/benjaminzelaya/Desktop/PI_DA-main/PI_2_Henry/DASHBOARD/dataframes_dashboard.csv')
    df_crypto_dashboard['date'] = pd.to_datetime(df_crypto_dashboard['date']).dt.date
except Exception as e:
    print("Error al leer el archivo CSV:", e)

# Título de la aplicación
st.title('Análisis de Criptomonedas')

# Mostrar el DataFrame
st.write('Datos de criptomonedas:')
st.dataframe(df_crypto_dashboard)

# Calcular KPIs
max_price = df_crypto_dashboard['price'].max()
min_price = df_crypto_dashboard['price'].min()
avg_price = df_crypto_dashboard['price'].mean()


# Seleccionar token
selected_token = st.selectbox('Selecciona un token:', df_crypto_dashboard['symbol'].unique())

# Filtrar datos por token seleccionado
df_selected_token = df_crypto_dashboard[df_crypto_dashboard['symbol'] == selected_token]

# Mostrar KPIs específicos del token seleccionado
st.subheader(f'Key Performance Indicators (KPIs) para {selected_token}')
token_max_price = df_selected_token['price'].max()
token_min_price = df_selected_token['price'].min()
token_avg_price = df_selected_token['price'].mean()

st.write(f'Maximum Price: {token_max_price:.2f}')
st.write(f'Minimum Price: {token_min_price:.2f}')
st.write(f'Average Price: {token_avg_price:.2f}')

# Crear gráfico de precio a lo largo del tiempo para el token seleccionado
st.subheader(f'Precio a lo largo del tiempo para {selected_token}')
fig = px.line(df_selected_token, x='date', y='price', title=f'Precio a lo largo del tiempo para {selected_token}')
st.plotly_chart(fig)


# Sección para calcular ganancias potenciales
st.subheader('Calcular Ganancias Potenciales')
selected_investment_date = st.date_input('Selecciona una fecha para invertir:')
selected_future_date = st.date_input('Selecciona una fecha futura:')
investment_amount = st.number_input('Inversión en USD:', min_value=0.0)

if selected_investment_date and selected_future_date and investment_amount > 0:
    investment_row = df_selected_token[df_selected_token['date'] == selected_investment_date]
    future_row = df_selected_token[df_selected_token['date'] == selected_future_date]
    
    if not investment_row.empty and not future_row.empty:
        initial_price = investment_row['price'].values[0]
        future_price = future_row['price'].values[0]
        
        potential_gain = investment_amount * (future_price / initial_price)
        roi = ((future_price - initial_price) / initial_price) * 100
        
        st.write(f"Si hubieras invertido ${investment_amount:.2f}$ en ${selected_token}$ el ${selected_investment_date}, "
                 f"$a la fecha ${selected_future_date}$ tendrías un valor de ${potential_gain:.2f}$ en {selected_token}.")
        
        # Mostrar ROI
        st.write(f'Return on Investment (ROI): {roi:.2f}%')

        # Crear gráfico de cambio en el valor (gráfico de barras agrupadas)
        fig_change = px.bar(
            x=['Valor Inicial', 'Valor Futuro'],
            y=[initial_price, future_price],
            title='Cambio en el Valor',
            labels={'x': 'Valor', 'y': 'Precio'},
            color=['Valor Inicial', 'Valor Futuro']
        )
        st.plotly_chart(fig_change)
        
    else:
        st.write('Alguna de las fechas seleccionadas no está en el conjunto de datos o el token no coincide.')



### streamlit run crypto_dashboard_app.py  (PARA CORRER)