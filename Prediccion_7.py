import numpy as np
import streamlit as st
import pandas as pd

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("Gasolina.jpg", caption="Precio de la gasolina.", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)



st.write(''' # Precio de la Gasolina ''')
#st.image("calories-burn.jpg", caption="Cantidad de calorías quemadas.")

st.header('Datos personales')

def user_input_features():
  # Entrada
  Año= st.number_input('Año (a partir de 2017):',  min_value=2017, max_value=2050, value = 2017, step = 1) # Set a default value for Año
  Mes = st.number_input('Mes:Ene : 1, Feb : 2, Mar : 3, Abr : 4, May : 5, Jun : 6, Jul : 7, Agos : 8, Sep : 9, Oct : 10, Nov : 11, Dic : 12', min_value=1, max_value=12, value = 1, step = 1) # Set min_value to 1 and a default value
  Entidad = st.number_input('Entidad (Entidad numeria del 0-32):', min_value=0, max_value=32, value = 0, step = 1) # Set max_value to 32 and a default value


  user_input_data = {'Año': Año,
                     'Mes' : Mes,
                     'Entidad' : Entidad
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

gasolina_df =  pd.read_csv('Gasolina2.csv', encoding='latin-1') # Renamed calories to gasolina_df
X = gasolina_df.drop(columns='PRECIO')
y = gasolina_df['PRECIO']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df.Año + b1[1]*df.Mes + b1[2]*df.Entidad # Removed space in df.Año

st.markdown("<h2 style='text-align: center; color: #884EA0;'>Cálculo del precio</h2>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div style="text-align: center; background-color: #F2F4F4; padding: 20px; border-radius: 15px;">
        <h3 style="color: #D35400;">El precio será:</h3>
        <p style="font-size: 28px; font-weight: bold; color: #1F618D;">${prediccion.values[0]:.2f} MXN</p>
    </div>
    """, 
    unsafe_allow_html=True
)
