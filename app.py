import streamlit as st
import pandas as pd
import sidetable as stb 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.title("Analisis Exploratorio de :blue[Vehiculos] :car:")

st.header('Analisis Exploratorio Inicial:')

raw_data =pd.read_csv('vehicles_us.csv')


st.subheader('Revisar tipos de datos de las columnas:')
st.dataframe(raw_data.dtypes.rename('datatype'))

st.subheader('Revisar primeras filas:')
st.dataframe(raw_data.head())

st.subheader('Revisar primeras filas:')
st.dataframe(raw_data.tail())

st.subheader('Revisar primeros valores ausentes:')
st.dataframe(raw_data.stb.missing(style=True))

st.subheader('Revisar primeros filas duplicadas:')
st.write('El numero de filas duplicadas es: {}'.format(raw_data.duplicated().sum()))

st.subheader('Estadisticas descriptivas de los datos numericos:')
st.dataframe(raw_data.describe())

st.header('Analisis Exploratorio')

st.header('Modelo vs Precio')

boton_barras= st.button('Crear grafico de barras del modelo vs el precio', type='primary')

if boton_barras:
    st.bar_chart(raw_data, x='model', y='price')

st.header('Histograma de Condiciones vs el año del modelo ')

boton_histograma = st.button('Crear histograma de la condicion de cada año del modelo ', type='primary')

if boton_histograma:
    fig, ax = plt.subplots() 
    ax.hist(raw_data['model_year'], bins=20)
    sns.histplot(raw_data, x='model_year', hue='condition', multiple='stack', ax=ax)
    st.pyplot(fig)

st.header('Modelo por odometro o cilindraje')
dimension_selection= st.selectbox(
    'Selecciona el tipo',
    ('cylinders','odometer')
)
st.write('El usuario selecciono: {}'.format(dimension_selection))
st.scatter_chart(raw_data, x='model', y=dimension_selection)