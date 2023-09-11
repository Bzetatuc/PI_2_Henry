import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# # logo en la parte superior
# logo_path = '/Users/benjaminzelaya/Desktop/PI_DA-main/PI_2_Henry/PI_2_Henry/wealthsimple.png'
# st.image(logo_path, width=500)

# Leer el archivo CSV y procesar los datos
try:
    df_crypto_dashboard = pd.read_csv('dataframes_dashboard.csv')
    df_crypto_dashboard['date'] = pd.to_datetime(df_crypto_dashboard['date']).dt.date
except Exception as e:
    print("Error al leer el archivo CSV:", e)

## Título de la aplicación
st.title('Análisis de Criptomonedas 🚀📊')
st.markdown('<hr style="border: 2px solid #e74c3c;">', unsafe_allow_html=True)

# video_path = "/Users/benjaminzelaya/Desktop/Sanc/Untitled design.mp4"  

# st.video(video_path)

# Sidebar para seleccionar token

st.sidebar.subheader('🔷 Selecciona un token')
selected_token = st.sidebar.selectbox('Elije un token:', df_crypto_dashboard['symbol'].unique())

# Descripción de los tokens seleccionados
st.sidebar.subheader('TOKENS SELECCIONADOS')
st.sidebar.markdown("¡Aquí presentamos una descripción breve de las criptomonedas seleccionadas en este dashboard!\n\n"
                    "**Binance Coin (BNB):** BNB es la moneda nativa de Binance, una de las principales plataformas de intercambio de criptomonedas. Muchos inversores podrían considerar invertir en BNB debido a su utilidad en la plataforma Binance, como descuentos en tarifas de intercambio y acceso a ventas de tokens. Además, el crecimiento de Binance como plataforma podría impactar positivamente en la demanda de BNB. 💱\n\n"
                    "**Bitcoin (BTC):** Bitcoin es considerado como oro digital y una reserva de valor. Muchos inversores ven a Bitcoin como un activo seguro y una forma de diversificar sus carteras. La escasez de suministro, la adopción institucional y la cobertura mediática hacen que Bitcoin sea atractivo para aquellos que buscan inversiones a largo plazo. ₿\n\n"
                    "**Cardano (ADA):** Cardano se centra en la investigación científica y el desarrollo de soluciones robustas. Su enfoque en la escalabilidad y la sostenibilidad podría atraer a inversores interesados en proyectos blockchain de alto potencial. Además, su plataforma para contratos inteligentes y aplicaciones descentralizadas también podría ser un factor atractivo. 🏛️\n\n"
                    "**Dogecoin (DOGE):** Dogecoin comenzó como una broma, pero ha ganado una comunidad activa. Algunos inversores pueden considerar DOGE como una inversión especulativa o como una forma de apoyar causas benéficas y proyectos comunitarios. Sin embargo, debido a su naturaleza volátil y falta de casos de uso claros, también conlleva un alto riesgo. 🐶\n\n"
                    "**Ethereum (ETH):** Ethereum es una plataforma líder para contratos inteligentes y dApps. Muchos inversores ven a Ethereum como el 'Internet de las finanzas' y creen en su capacidad para transformar industrias. El crecimiento del ecosistema DeFi y NFT (tokens no fungibles) en la plataforma podría aumentar su demanda. 💡\n\n"
                    "**Polkadot (DOT):** Polkadot busca habilitar la interoperabilidad entre diferentes blockchains. Aquellos que creen en la importancia de la interoperabilidad y la conexión entre diferentes proyectos blockchain podrían considerar invertir en DOT. La interoperabilidad en el contexto de la tecnología blockchain se refiere a la capacidad de diferentes blockchains (redes de registro distribuido) para comunicarse, interactuar y trabajar juntas de manera eficiente y fluida. Cada blockchain es como un sistema independiente que almacena registros y ejecuta contratos inteligentes. Sin embargo, en el mundo real, hay muchas blockchains con diferentes propósitos, protocolos y características 🔗\n\n"
                    "**Ripple (XRP):** Ripple se centra en facilitar transferencias internacionales de dinero. Inversores interesados en soluciones de pagos globales podrían considerar XRP. Sin embargo, el litigio actual con la SEC ha afectado la percepción de riesgo asociada con esta moneda. 💸\n\n"
                    "**Solana (SOL):** Solana se destaca por su alta velocidad y escalabilidad. Inversores interesados en aplicaciones descentralizadas y DeFi podrían considerar SOL debido a su capacidad para manejar un alto rendimiento. ☀️\n\n"
                    "**Tether (USDT):** Tether es una criptomoneda estable vinculada al dólar estadounidense. Muchos inversores utilizan USDT como una forma de mantener estabilidad de valor en momentos de volatilidad, así como para facilitar el trading en exchanges. 💲\n\n"
                    "**USD Coin (USDC):** Similar a Tether, USD Coin es una criptomoneda estable vinculada al dólar estadounidense. Aquellos que buscan una alternativa estable en el mundo de las criptomonedas podrían considerar USDC.💲")

# Sección para seleccionar token
st.header('Explorando el Mercado 📈')
st.write("Comenzamos con un vistazo general al mercado. Cargamos los datos de diferentes criptomonedas y mostramos las principales estadísticas. Además, puedes seleccionar el token que más te interese en el menú de la barra lateral.")


# Filtrar datos por token seleccionado
df_selected_token = df_crypto_dashboard[df_crypto_dashboard['symbol'] == selected_token]
# Calcular los KPIs
token_max_price = df_selected_token['price'].max()
token_min_price = df_selected_token['price'].min()
token_avg_price = df_selected_token['price'].mean()

# Presentar los KPIs
st.header(f'Análisis de {selected_token} 📊')
st.write(f"Detalles clave sobre {selected_token} rendimiento. Visualiza el precio máximo, mínimo y promedio a lo largo del tiempo para obtener una comprensión rápida de su evolución.")
st.write("Explora las tendencias y cambios en el valor con el gráfico interactivo a continuación.")

col1, col2, col3, _ = st.columns(4)
col1.metric("Máximo Precio 2020-2023", f"${token_max_price:.2f}")
col2.metric("Mínimo Precio 2020-2023", f"${token_min_price:.2f}")
col3.metric("Precio Promedio 2020-2023", f"${token_avg_price:.2f}")

# Crear el gráfico de precio a lo largo del tiempo
fig = go.Figure()

# Agregar el gráfico de línea principal
line_trace = go.Scatter(x=df_selected_token['date'], y=df_selected_token['price'], #Se utiliza Plotly (go.Figure()) para crear un gráfico interactivo.
                        mode='lines', name='Precio')
fig.add_trace(line_trace)
#Se agrega un gráfico de línea principal (go.Scatter()) que representa el precio del token a lo largo del tiempo.
# # Los datos para el eje x (fechas) provienen del DataFrame df_selected_token['date'], y los datos para el eje y (precios) provienen de df_selected_token['price'].


# Agregar selección de rango
range_selector = go.layout.XAxis(
    rangeslider=dict(visible=True),
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1d", step="day", stepmode="backward"),
            dict(count=7, label="1w", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.update_layout(xaxis=range_selector)

#Se agrega un selector de rango en el eje x (range_selector) para permitir a los usuarios explorar diferentes intervalos de tiempo en el gráfico.
# Los botones en el selector de rango permiten ajustar la vista a intervalos de 1 día, 1 semana, 1 mes, 3 meses y la vista completa

# Personalizar el diseño del gráfico
fig.update_layout(title=f'Precio a lo largo del tiempo para {selected_token}',
                  xaxis_title='Fecha', yaxis_title='Precio',
                  template='plotly_dark')

#fig.update_layout() se usa para personalizar el diseño del gráfico. 
# Se establece el título del gráfico, los títulos de los ejes x e y, y se aplica un estilo oscuro (plotly_dark) al gráfico.

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Finalmente, st.plotly_chart(fig) se utiliza para mostrar el gráfico interactivo en la interfaz de Streamlit.

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
        #El cálculo del ROI (Return on Investment) implica comparar el resultado final (ganancia o pérdida) de una inversión con respecto a su costo inicial.
         # En este contexto, el ROI se calcula como la variación porcentual entre el precio futuro y el precio inicial de un activo financiero (en este caso, el token seleccionado). 
         # primero samocamos la ganancia potencial que es precio futuro - precio inicial 
        #La fórmula general para calcular el ROI es la siguiente: ganancia potencial sobre precio inicial x 100


        st.write(f" Si hubieras invertido ${investment_amount:.2f} dolares en  {selected_token}  el  {selected_investment_date}, "
                 f" a la fecha  {selected_future_date}  podrias haber obtenido un valor de  {potential_gain:.2f}  dolares en {selected_token}.")
        
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

# Sección para calcular ganancias y pérdidas comparando Tokens
st.header('Ganancias y Pérdidas comparando Tokens 💰')
st.write("¿Ahora te preguntas cuánto podrías haber ganado si hubieras invertido en otro token específico? ¡Te tenemos nuevamente cubierto! Puedes seleccionar otro token de nuestra lista, una nueva fecha de inversión y una nueva fecha futura, junto con la cantidad que habrías invertido en ambos. Nuestra aplicación calculará y mostrará tus posibles ganancias o pérdidas, así como el retorno de inversión (ROI) comparativas.")

# Seleccionar un token para comparar
available_tokens = df_crypto_dashboard['symbol'].unique()
selected_token_for_comparison = st.selectbox('Selecciona un token para comparar', available_tokens)

# Remover el token seleccionado previamente de las opciones
options_without_selected_token = [token for token in available_tokens if token != selected_token]

# Obtener los datos del token seleccionado para comparación
df_comparison_token = df_crypto_dashboard[df_crypto_dashboard['symbol'] == selected_token_for_comparison]

selected_investment_date_comparacion = st.date_input('Selecciona una fecha para invertir en la comparación:')
selected_future_date_comparacion = st.date_input('Selecciona una fecha futura en la comparación:')
investment_amount_comparacion = st.number_input('Inversión en USD en la comparación:', min_value=0.0)

if selected_investment_date_comparacion and selected_future_date_comparacion and investment_amount_comparacion > 0:
    investment_row_comparacion = df_selected_token[df_selected_token['date'] == selected_investment_date_comparacion]
    future_row_comparacion = df_selected_token[df_selected_token['date'] == selected_future_date_comparacion]
    
    comparison_investment_row = df_comparison_token[df_comparison_token['date'] == selected_investment_date_comparacion]
    comparison_future_row = df_comparison_token[df_comparison_token['date'] == selected_future_date_comparacion]
    
    if not investment_row_comparacion.empty and not future_row_comparacion.empty and not comparison_investment_row.empty and not comparison_future_row.empty:
        initial_price_comparacion = investment_row_comparacion['price'].values[0]
        future_price_comparacion = future_row_comparacion['price'].values[0]
        comparison_initial_price = comparison_investment_row['price'].values[0]
        comparison_future_price = comparison_future_row['price'].values[0]
        
        potential_gain_comparacion = investment_amount_comparacion * (future_price_comparacion / initial_price_comparacion)
        roi_comparacion = ((future_price_comparacion - initial_price_comparacion) / initial_price_comparacion) * 100
        comparison_potential_gain = investment_amount_comparacion * (comparison_future_price / comparison_initial_price)
        comparison_roi = ((comparison_future_price - comparison_initial_price) / comparison_initial_price) * 100
        
        st.write(f" Si hubieras invertido  {investment_amount_comparacion:.2f}  dolares en  {selected_token}  el  {selected_investment_date_comparacion}, "
                 f" a la fecha  {selected_future_date_comparacion}  podrías haber obtenido un valor de  {potential_gain_comparacion:.2f}  dolares en {selected_token}.")
        
        st.write(f" Si hubieras invertido  {investment_amount_comparacion:.2f}  dolares en {selected_token_for_comparison} el  {selected_investment_date_comparacion}, "
                 f" a la fecha  {selected_future_date_comparacion}  podrías haber obtenido un valor de  {comparison_potential_gain:.2f}  dolares en {selected_token_for_comparison}.")
        
        # Mostrar ROIs
        st.markdown(f'Retorno de Inversion (ROI) para {selected_token}: **{roi_comparacion:.2f}%**', unsafe_allow_html=True)
        st.markdown(f'Retorno de Inversion (ROI) para {selected_token_for_comparison}: **{comparison_roi:.2f}%**', unsafe_allow_html=True)

        # Gráfico de cambio en el valor (gráfico de barras agrupadas)
        fig_change_comparacion = px.bar(
            x=[f'Valor Inicial ({selected_token})', f'Valor Futuro ({selected_token})', f'Valor Inicial ({selected_token_for_comparison})', f'Valor Futuro ({selected_token_for_comparison})'],
            y=[initial_price_comparacion, future_price_comparacion, comparison_initial_price, comparison_future_price],
            title='Cambio en el Valor',
            labels={'x': 'Valor', 'y': 'Precio'}
        )
        fig_change_comparacion.update_traces(marker_color=['#3498db', '#2ecc71', '#e74c3c', '#9b59b6'])
        fig_change_comparacion.update_traces(marker_line_width=0, marker_line_color='white')
        st.plotly_chart(fig_change_comparacion)
        
    else:
        st.warning('Alguna de las fechas seleccionadas no está en el conjunto de datos o los tokens no coinciden.')


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
selected_column = st.selectbox('Selecciona una columna para análisis', ['date', 'price'])

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
        
        max_date_row = filtered_data[filtered_data['price'] == filtered_data['price'].max()]
        st.write('Máximo de precio:', max_date_row['price'].iloc[0], 'Fecha:', max_date_row['date'].iloc[0].strftime('%Y-%m-%d'))
        
        min_date_row = filtered_data[filtered_data['price'] == filtered_data['price'].min()]
        st.write('Mínimo de precio:', min_date_row['price'].iloc[0], 'Fecha:', min_date_row['date'].iloc[0].strftime('%Y-%m-%d'))
        
        st.write('Precio promedio:', filtered_data['price'].mean())

elif selected_column in ['price']:
    selected_values = st.multiselect(f'Selecciona valores de la columna {selected_column}', df_selected_token[selected_column].unique())
    if selected_values:
        st.subheader(f'Análisis de {selected_column}')
        st.write(f'Valores seleccionados: {selected_values}')
        
        max_value_row = df_selected_token[df_selected_token[selected_column].isin(selected_values)][selected_column].idxmax()
        st.write(f'Máximo de {selected_column}:', df_selected_token.loc[max_value_row, selected_column],
                 'Fecha:', df_selected_token.loc[max_value_row, 'date'].strftime('%Y-%m-%d'))
        
        min_value_row = df_selected_token[df_selected_token[selected_column].isin(selected_values)][selected_column].idxmin()
        st.write(f'Mínimo de {selected_column}:', df_selected_token.loc[min_value_row, selected_column],
                 'Fecha:', df_selected_token.loc[min_value_row, 'date'].strftime('%Y-%m-%d'))
        
        st.write('Precio promedio:', df_selected_token[df_selected_token[selected_column].isin(selected_values)]['price'].mean())
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
st.write("La matriz de correlación muestra cómo los precios de diferentes tokens están correlacionados entre sí. Un valor más cercano a 1 indica una correlación positiva, mientras que un valor más cercano a -1 indica una correlación negativa.")
st.write("También puedes explorar la correlación entre los precios de diferentes tokens. Mostramos una matriz de correlación que te permite visualizar cómo los precios de los tokens están relacionados. Además, puedes seleccionar dos tokens específicos para ver su correlación detallada.")
st.write('Matriz de correlación entre los precios de diferentes tokens:')
st.dataframe(correlation_matrix)



# Interacción para seleccionar tokens y mostrar correlación específica
st.subheader('Correlación Específica entre Tokens')
selected_tokens = st.multiselect('Selecciona dos tokens:', df_crypto_dashboard['symbol'].unique())
if len(selected_tokens) == 2:
    specific_correlation = correlation_matrix.loc[selected_tokens[0], selected_tokens[1]]
    st.write(f'Correlación entre {selected_tokens[0]} y {selected_tokens[1]}: {specific_correlation:.4f}')
    
    # Conclusión de correlación específica
    if specific_correlation > 0.7:
        st.write(f'La correlación entre {selected_tokens[0]} y {selected_tokens[1]} es alta, lo que sugiere que tienden a moverse en la misma dirección en el mercado.')
    elif specific_correlation < -0.7:
        st.write(f'La correlación entre {selected_tokens[0]} y {selected_tokens[1]} es negativa, lo que sugiere que tienden a moverse en direcciones opuestas en el mercado.')
    else:
        st.write(f'La correlación entre {selected_tokens[0]} y {selected_tokens[1]} es baja, lo que sugiere que no hay una relación clara en sus movimientos en el mercado.')

# Perfil de inversor basado en la correlación
st.subheader('Perfil de Inversor')
st.write("✅ **Diversificador:** Si la correlación es baja, tiendes a diversificar tus inversiones para minimizar riesgos y no depender de un solo tipo de activo. Esto puede ayudarte a mantener un equilibrio en tu cartera y protegerte contra grandes pérdidas en un solo activo..")
st.write("🔄 **Neutral en Correlación:** Si la correlación está cerca de cero, no tienes preferencias claras y podríamos proponerte una combinación de estrategias. Podrías estar buscando oportunidades tanto en activos con alta correlación como en aquellos con baja correlación, dependiendo de las condiciones del mercado.")
st.write("🔗 **Inversor en Pares:** Si la correlación es alta, te inclinas hacia movimientos en la misma dirección en el mercado. Esto sugiere que buscas aprovechar las tendencias y los movimientos conjuntos de los activos, lo que puede ser beneficioso en períodos de fuertes tendencias alcistas o bajistas..")
st.write("🔄 **Inversor Contrario:** Si la correlación es negativa, buscas aprovechar movimientos opuestos en el mercado. Esta estrategia implica invertir en activos que tienden a moverse en direcciones opuestas, lo que puede ser beneficioso para aprovechar situaciones de sobrecompra o sobreventa en el mercado..")
if len(selected_tokens) == 2:
    st.write("Basado en la correlación y los tokens seleccionados, podrías tener el siguiente perfil de inversor:")
    
    
    
    # Definir los perfiles de inversor

    profiles = {

    'Diversificador': "Eres un inversor diversificador. Tu enfoque se basa en la minimización de riesgos a través de la diversificación. La baja correlación entre los tokens seleccionados refleja tu estrategia de mantener un portafolio equilibrado y no depender excesivamente de un solo tipo de activo. Esta estrategia es especialmente valiosa en entornos volátiles ya que reduce la exposición a pérdidas significativas en un solo activo. Además, tu estrategia de diversificación podría incluir otros tipos de activos, como acciones, bonos o bienes raíces, para lograr un portafolio aún más equilibrado.",
    'Neutral en Correlación': "Eres un inversor neutral en correlación. Tienes una visión equilibrada y versátil del mercado. La correlación cercana a cero entre los tokens seleccionados sugiere que estás dispuesto a explorar oportunidades en diversos tipos de activos. Esta posición te permite beneficiarte de diferentes tendencias y protegerte en caso de volatilidad en una clase de activos específica. Además, tu neutralidad en correlación puede llevarte a considerar inversiones en acciones, ETFs, Fondos Cotizados en Bolsa (Exchange-Traded Funds en inglés), son instrumentos financieros que se negocian en bolsa de manera similar a las acciones. Un ETF es un fondo de inversión que busca replicar el rendimiento de un índice específico, como el S&P 500, el Nasdaq, un sector industrial o un mercado en particular, pudiendo invertir en otros instrumentos financieros fuera del mundo de las criptomonedas.",
    'Inversor en Pares': "Eres un inversor en pares. Prefieres capitalizar las tendencias compartidas en el mercado. La alta correlación entre los tokens seleccionados indica que buscas rendimientos basados en movimientos conjuntos de activos. Esta estrategia es efectiva en mercados alcistas o bajistas donde las tendencias son fuertes. Sin embargo, también implica un mayor riesgo si el mercado se vuelve adverso para los activos seleccionados. Además, tu preferencia por movimientos conjuntos podría llevar a considerar inversiones en pares de divisas, commodities y otros mercados interconectados.",
    'Inversor Contrario': "Eres un inversor contrario. Tu estrategia implica aprovechar las oportunidades en situaciones de cambio de dirección en el mercado. La correlación negativa entre los tokens seleccionados sugiere que buscas beneficios de los movimientos opuestos entre los activos. Esta táctica puede generar ganancias sustanciales en momentos de alta volatilidad y correcciones del mercado, pero también puede ser riesgosa si no se gestionan adecuadamente las tendencias y los puntos de entrada y salida. Además, tu estilo contrario podría llevarte a considerar inversiones en estrategias de contrarian en otros mercados, como acciones y futuros.",
    }

    # Obtener el perfil basado en la correlación
    if specific_correlation > 0.7:
        profile = 'Inversor en Pares'
    elif specific_correlation < -0.7:
        profile = 'Inversor Contrario'
    elif specific_correlation > -0.3 and specific_correlation < 0.3:
        profile = 'Neutral en Correlación'
    else:
        profile = 'Diversificador'
    
 
 # Mostrar el perfil 
    st.markdown(f"<h2 style='text-align:center;color:#3498db;'>Perfil: {profile}</h2>", unsafe_allow_html=True)
    st.write(f"<p style='font-size:18px;text-align:justify;'>{profiles[profile]}</p>", unsafe_allow_html=True)



# Mapa de calor de la correlación
fig_heatmap = px.imshow(correlation_matrix, color_continuous_scale='RdBu', title='Mapa de Calor de Correlación')
st.plotly_chart(fig_heatmap)


# Descripción debajo del mapa de calor de la correlación
st.subheader('Mapa de Calor de Correlación')
st.write("El mapa de calor resalta visualmente las relaciones de correlación entre los tokens. Los colores más intensos representan una correlación más fuerte, ya sea positiva o negativa.")


st.markdown('<hr style="border: 2px solid #3498db;">', unsafe_allow_html=True)

# Sección para Exchange Recomendados
st.header('Exchanges Recomendados 💼')
st.write("Aquí te presentamos algunos de los exchanges más recomendados usados para operar criptomonedas. Estos exchanges han demostrado ser confiables, seguros y ofrecen una variedad de tokens para operar. Recomendamos siempre de investigar y tomar precauciones antes de operar en cualquier exchange.")

# Información de los exchanges recomendados
exchanges = [
    {'nombre': 'Binance', 'descripcion': 'Uno de los exchanges más grandes y populares del mundo.', 'link': 'https://www.binance.com/'},
    {'nombre': 'Coinbase', 'descripcion': 'Plataforma amigable para principiantes, ideal para comprar y almacenar criptomonedas.', 'link': 'https://www.coinbase.com/'},
    {'nombre': 'Kraken', 'descripcion': 'Exchange con una sólida reputación y una amplia gama de tokens disponibles.', 'link': 'https://www.kraken.com/'},
    # Agrega más exchanges recomendados aquí
]

# Mostrar la información de los exchanges 
for exchange in exchanges:
    st.write(f"**{exchange['nombre']}**: {exchange['descripcion']} [Mas información]({exchange['link']})")



# Consideraciones Importantes
st.header('Consideraciones Importantes ⚠️')
st.warning("Antes de embarcarte en cualquier inversión en criptomonedas, es fundamental recordar que estos activos son altamente volátiles y conllevan riesgos significativos. La situación del mercado puede cambiar rápidamente. Te recomendamos investigar exhaustivamente cada proyecto y evaluar tu tolerancia al riesgo antes de considerar cualquier inversión.")

# Agregar separador visual
st.markdown('<hr style="border: 2px solid #3498db;">', unsafe_allow_html=True)

# Centrar texto con estilo y emojis
#creditos
st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; color: #3498db;'>🚀 Proyecto Individual 2 Data Science 🚀</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Arial, sans-serif;'>👨‍🎓 Benjamin Zelaya 👨‍🎓</h3>", unsafe_allow_html=True)


### streamlit run main.py  (PARA CORRER EN LOCAL)