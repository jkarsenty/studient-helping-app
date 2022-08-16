import streamlit as st
import pandas as pd
import numpy as np

from apps.home import main_header
from apps.sidebar import sidebar_student_characteristics,sidebar_choose_student
from model.model import load_model

## Header Home ##
main_header()

## Sidebar choose app configuration ##
COLUMNS = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 
'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 
'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']
student_value = ['GP', 'M', 18, 'U', 'GT3', 'A', 4, 4, 'at_home', 'teacher','course', 'father', 2, 2, 0, 'no', 'no', 'no', 'yes', 'yes', 'yes','no', 'no', 4, 3, 4, 1, 1, 2, 12]

df_init = pd.DataFrame([student_value],columns = COLUMNS)

student_id = sidebar_choose_student()
df_to_predict = sidebar_student_characteristics(df_init,student_id)

## Home DataFrames ##
ACTIONABLE = ['school', 'studytime', 'famsup', 'paid', 'activities', 'internet', 'freetime', 'goout', 'Dalc', 'Walc', 'health',"absences"]
st.write("### Caractéristiques initiales de l'élève choisi", df_init[ACTIONABLE])

## Prediction ##

#model_clf = load_model("model/clf_model.joblib")
model_rgs = load_model("model/rgs_model.joblib")
st.write("### Caractéristiques modélisées",df_to_predict[ACTIONABLE])

prediction = np.round(model_rgs.predict(df_to_predict),1)
st.write(f"#### Avec ces caractéristiques l'élève devrait avoir {prediction[0]}/20")