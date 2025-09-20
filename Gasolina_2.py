import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Precio de la Gasolina ''')
#st.image("calories-burn.jpg", caption="Cantidad de calorías quemadas.")

st.header('Datos personales')

def user_input_features():
  # Entrada
  Año= st.number_input('Año (a partir de 2017):',  min_value=2017, max_value=2050, value = 0, step = 1)
  Mes = st.number_input('Mes:Ene : 1, Feb : 2, Mar : 3, Abr : 4, May : 5, Jun : 6, Jul : 7, Agos : 8, Sep : 9, Oct : 10, Nov : 11, Dic : 12', min_value=0, max_value=100, value = 0, step = 1)
  Entidad = st.number_input('Entidad (Entidad numeria del 0-32):', min_value=0, max_value=230, value = 0, step = 1)
  

  user_input_data = {'Año': Año,
                     'Mes' : Mes,
                     'Entidad' : Entidad
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()  
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

calories =  pd.read_csv('Gasolina2.csv', encoding='latin-1')
X = calories.drop(columns='PRECIO')
y = calories['PRECIO']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df. Año + b1[1]*df.Mes + b1[2]*df.Entidad

st.subheader('Calculo del PRECIO')
st.write('El precio sera', prediccion)
