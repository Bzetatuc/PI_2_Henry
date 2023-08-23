import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV y procesar los datos
try:
    df_crypto_dashboard = pd.read_csv('dataframes_dashboard.csv')
    df_crypto_dashboard['date'] = pd.to_datetime(df_crypto_dashboard['date']).dt.date
except Exception as e:
    print("Error al leer el archivo CSV:", e)

## Título de la aplicación
st.title('Análisis de Criptomonedas 🚀📊')
st.markdown('<hr style="border: 2px solid #e74c3c;">', unsafe_allow_html=True)


# Sidebar para seleccionar token
# Explorando el Mercado
st.header('Explorando el Mercado 📈')
st.write("Comenzamos con un vistazo general al mercado. Cargamos los datos de diferentes criptomonedas y mostramos las principales estadísticas. Además, puedes seleccionar el token que más te interese en el menú de la barra lateral.")
st.sidebar.subheader('🔷 Selecciona un token')
selected_token = st.sidebar.selectbox('Elije un token:', df_crypto_dashboard['symbol'].unique())



# Filtrar datos por token seleccionado
df_selected_token = df_crypto_dashboard[df_crypto_dashboard['symbol'] == selected_token]

# Calcular KPIs para el token seleccionado
# Análisis de un Token Específico
st.header('Análisis de un Token Específico 📊')
st.write("Una vez seleccionado un token, presentamos detalles clave sobre su rendimiento. Mostramos el precio máximo, mínimo y promedio a lo largo del tiempo. Esto te permitirá obtener una visión rápida de cómo ha evolucionado el token en el período analizado.")
st.write("También proporcionamos un gráfico interactivo que muestra la evolución del precio de ese token a lo largo del tiempo. Puedes explorar las tendencias y cambios en el valor con facilidad.")
token_max_price = df_selected_token['price'].max()
token_min_price = df_selected_token['price'].min()
token_avg_price = df_selected_token['price'].mean()

# Diseño en columnas para mostrar los primeros KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Máximo Precio", f"${token_max_price:.2f}")
col2.metric("Mínimo Precio", f"${token_min_price:.2f}")
col3.metric("Precio Promedio", f"${token_avg_price:.2f}")

# Gráfico de precio a lo largo del tiempo para el token seleccionado
fig = px.line(df_selected_token, x='date', y='price', title=f'Precio a lo largo del tiempo para {selected_token}')
st.plotly_chart(fig)

# Agregar separador visual
st.markdown('<hr style="border: 2px solid #e74c3c;">', unsafe_allow_html=True)

# Sección para calcular ganancias 
# Ganancias y Pérdidas
st.header('Ganancias y Pérdidas 💰')
st.write("¿Te preguntas cuánto podrías haber ganado si hubieras invertido en un token específico en el pasado? ¡Te tenemos cubierto! Puedes seleccionar una fecha de inversión y una fecha futura, junto con la cantidad que habrías invertido. Nuestra aplicación calculará y mostrará tus posibles ganancias o pérdidas, así como el retorno de inversión (ROI).")

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
        
        st.write(f"Si hubieras invertido ${investment_amount:.2f}$ dolares en ${selected_token}$ el ${selected_investment_date}, "
                 f"$ a la fecha ${selected_future_date}$ podrias haber obtenido un valor de ${potential_gain:.2f}$ dolares en {selected_token}.")
        
        # Mostrar ROI
        st.markdown(f'Retorno de Inversion (Return on Investment "ROI"): **{roi:.2f}%**', unsafe_allow_html=True)

        # Gráfico de cambio en el valor (gráfico de barras agrupadas)
        fig_change = px.bar(
            x=['Valor Inicial', 'Valor Futuro'],
            y=[initial_price, future_price],
            title='Cambio en el Valor',
            labels={'x': 'Valor', 'y': 'Precio'}
        )
        fig_change.update_traces(marker_color=['#3498db', '#2ecc71'])
        fig_change.update_traces(marker_line_width=0, marker_line_color='white')
        st.plotly_chart(fig_change)
        
    else:
        st.warning('Alguna de las fechas seleccionadas no está en el conjunto de datos o el token no coincide.')


# Agregar separador visual
st.markdown('<hr style="border: 2px solid #e74c3c;">', unsafe_allow_html=True)

# Mostrar DataFrame 
#Esto agrega un subtítulo en la aplicación web que muestra el nombre del token (o cualquier variable que hayas definido como selected_token) junto a "DataFrame para".
st.subheader(f'DataFrame para {selected_token}')
#Esto muestra el DataFrame df_selected_token en la aplicación web. Es simplemente una representación visual de los datos.
st.write(df_selected_token)

# Explorando los Datos en Detalle
st.header('Explorando los Datos en Detalle 📊')
st.write("Dentro de la sección del token seleccionado, te ofrecemos un vistazo más detallado a los datos subyacentes. Puedes seleccionar una columna para análisis y, en caso de que selecciones fechas, te presentaremos estadísticas sobre las fechas seleccionadas, incluyendo el promedio, el máximo y el mínimo de los precios.")

# Seleccionar una columna para análisis
#Aquí, se crea un cuadro de selección (selectbox) donde el usuario puede elegir una columna del DataFrame df_selected_token para realizar análisis.
selected_column = st.selectbox('Selecciona una columna para análisis', df_selected_token.columns)

# Interacción con valores seleccionados
#Si la columna seleccionada es 'date', se muestran las fechas únicas disponibles en el DataFrame mediante un cuadro de selección múltiple (multiselect).
#Luego, si el usuario selecciona algunas fechas, se filtran los datos para incluir solo las filas con las fechas seleccionadas. Luego se calcula el promedio de los precios para las fechas seleccionadas.
#Además, se encuentra la fila con el precio máximo y la fila con el precio mínimo dentro del conjunto de datos filtrado. Luego se muestra el precio máximo y mínimo junto con sus fechas correspondientes.

if selected_column == 'date':
    selected_dates = st.multiselect('Selecciona fechas', df_selected_token['date'].unique(),
                                    format_func=lambda date: date.strftime('%Y-%m-%d'))
    if selected_dates:
        st.subheader(f'Análisis de precios para las fechas seleccionadas')
        st.write('Fechas seleccionadas:', ', '.join([date.strftime('%Y-%m-%d') for date in selected_dates]))
        filtered_data = df_selected_token[df_selected_token['date'].isin(selected_dates)]
        st.write('Promedio de precio:', filtered_data['price'].mean())
        
        max_price_row = filtered_data[filtered_data['price'] == filtered_data['price'].max()]
        st.write('Máximo de precio:', max_price_row['price'].iloc[0], 'Fecha:', max_price_row['date'].iloc[0].strftime('%Y-%m-%d'))
        
        min_price_row = filtered_data[filtered_data['price'] == filtered_data['price'].min()]
        st.write('Mínimo de precio:', min_price_row['price'].iloc[0], 'Fecha:', min_price_row['date'].iloc[0].strftime('%Y-%m-%d'))
else:
    selected_values = st.multiselect('Selecciona valores', df_selected_token[selected_column].unique())
    if selected_values:
        st.subheader(f'Análisis de {selected_column}')
        st.write(f'Valores seleccionados: {selected_values}')
        st.write('Promedio:', df_selected_token[df_selected_token[selected_column].isin(selected_values)]['price'].mean())
        st.write('Máximo:', df_selected_token[df_selected_token[selected_column].isin(selected_values)]['price'].max())
        st.write('Mínimo:', df_selected_token[df_selected_token[selected_column].isin(selected_values)]['price'].min())
#Si la columna seleccionada no es 'date', significa que el usuario eligió otra columna para análisis. 
# En este caso, se permite al usuario seleccionar valores únicos de esa columna utilizando un cuadro de selección múltiple.
# Después de seleccionar los valores, se filtran los datos para incluir solo las filas que contienen los valores seleccionados. 
# #Luego se calcula el promedio, el máximo y el mínimo de los precios correspondientes a los valores seleccionados.


# Agregar separador visual
st.markdown('<hr style="border: 2px solid #e74c3c;">', unsafe_allow_html=True)


# Sección para mostrar la correlación entre los precios de diferentes tokens
correlation_matrix = df_crypto_dashboard.pivot_table(index='date', columns='symbol', values='price').corr()

# Mostrar correlación como DataFrame
st.subheader('Correlación entre Precios de Tokens')
st.write("También puedes explorar la correlación entre los precios de diferentes tokens. Mostramos una matriz de correlación que te permite visualizar cómo los precios de los tokens están relacionados. Además, puedes seleccionar dos tokens específicos para ver su correlación detallada.")
st.write('Matriz de correlación entre los precios de diferentes tokens:')
st.dataframe(correlation_matrix)

# Interacción para seleccionar tokens y mostrar correlación específica
st.subheader('Correlación Específica entre Tokens')
selected_tokens = st.multiselect('Selecciona dos tokens:', df_crypto_dashboard['symbol'].unique())
if len(selected_tokens) == 2:
    specific_correlation = correlation_matrix.loc[selected_tokens[0], selected_tokens[1]]
    st.write(f'Correlación entre {selected_tokens[0]} y {selected_tokens[1]}: {specific_correlation:.4f}')

# Visualización de la matriz de correlación como un mapa de calor
fig_heatmap = px.imshow(correlation_matrix, color_continuous_scale='RdBu_r', title='Mapa de calor de la correlación')
st.plotly_chart(fig_heatmap)

# Descripción debajo del gráfico de matriz de correlación
st.write("La matriz de correlación muestra cómo los precios de diferentes tokens están correlacionados entre sí. Un valor más cercano a 1 indica una correlación positiva, mientras que un valor más cercano a -1 indica una correlación negativa.")

# Descripción debajo del mapa de calor de la correlación
st.write("El mapa de calor resalta visualmente las relaciones de correlación entre los tokens. Los colores más intensos representan una correlación más fuerte, ya sea positiva o negativa.")

# Consideraciones Importantes
st.header('Consideraciones Importantes ⚠️')
st.warning("Antes de embarcarte en cualquier inversión en criptomonedas, es fundamental recordar que estos activos son altamente volátiles y conllevan riesgos significativos. La situación del mercado puede cambiar rápidamente. Te recomendamos investigar exhaustivamente cada proyecto y evaluar tu tolerancia al riesgo antes de considerar cualquier inversión.")
st.markdown('<hr style="border: 2px solid #3498db;">', unsafe_allow_html=True)

# Centrar texto con estilo y emojis
#creditos
st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; color: #3498db;'>🚀 Proyecto Individual 2 Data Science - Henry 🚀</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Arial, sans-serif;'>👨‍🎓 Alumno Benjamin Zelaya 👨‍🎓</h3>", unsafe_allow_html=True)


### streamlit run crypto_dashboard_app.py  (PARA CORRER EN LOCAL)