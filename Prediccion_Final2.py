import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Predicción Gasolina", layout="centered")

# --- Título (igual que lo tienes) ---
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Predicción del precio de la gasolina</h1>", unsafe_allow_html=True)

# --- Imagen principal centrada ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("Gasolina.jpg", caption="Precio de la gasolina.", width=400)

# --- Entradas de usuario ---
def user_input_features():
    Año = st.number_input('Año (a partir de 2017):',  min_value=2017, max_value=3000, value=2017, step=1)
    Mes = st.number_input('Mes (ENE: 1 ... DIC: 12):', min_value=1, max_value=12, value=1, step=1)

    st.markdown("<h2 style='text-align: center; color: #117A65;'>Datos</h2>", unsafe_allow_html=True)

    # Imagen DatosEntidad centrada
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("DatosEntidad.png", caption="Estados.", width=400)

    Entidad = st.number_input('Entidad (Valores del 0-32):', min_value=0, max_value=32, value=0, step=1)

    user_input_data = {'Año': Año, 'Mes': Mes, 'Entidad': Entidad}
    return pd.DataFrame(user_input_data, index=[0])

df = user_input_features()

# --- Mostrar entradas centradas (tabla pequeña) ---
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.markdown("**Entrada seleccionada:**")
    st.table(df)

# --- Modelo ---
Precio = pd.read_csv('Gasolina2.csv', encoding='latin-1')
X = Precio.drop(columns='PRECIO')
y = Precio['PRECIO']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train, y_train)

b1 = LR.coef_
b0 = LR.intercept_

# --- Predicción ---
prediccion = float(b0 + b1[0]*df.at[0, 'Año'] + b1[1]*df.at[0, 'Mes'] + b1[2]*df.at[0, 'Entidad'])

# --- Resultado (igual que ya tienes) ---
st.markdown("<h2 style='text-align: center; color: #884EA0;'>Cálculo del precio</h2>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="display:flex; justify-content:center;">
      <div style="width:420px; background-color:#F8F9F9; padding:18px; border-radius:12px; text-align:center; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <h3 style="color:#D35400; margin:4px 0;">El precio estimado es:</h3>
        <p style="font-size:30px; font-weight:700; color:#1F618D; margin:0;">${prediccion:,.2f} MXN</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
