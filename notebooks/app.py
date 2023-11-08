import pandas as pd
import plotly.express as px
import streamlit as st

# Ler os dados do arquivo CSV em um DataFrame
car_data = pd.read_csv('vehicles.csv')

# Adicionar um cabeçalho ao aplicativo Streamlit
st.header('Exploração de Dados de Vendas de Carros')

# Criar um botão para o histograma
hist_button = st.button('Criar histograma')

# Se o botão for clicado, criar um histograma e exibi-lo
if hist_button:
    # Escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criar um botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

# Se o botão for clicado, criar um gráfico de dispersão e exibi-lo
if scatter_button:
    # Escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
