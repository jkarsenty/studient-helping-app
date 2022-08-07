import streamlit as st
import pandas as pd
from apps.home import home_header,home_prediction
from apps.sidebar import sidebar_student_characteristics,sidebar_choose_config

# Header Home
home_header()

# Sidebar choose app configuration
config_choice = sidebar_choose_config()
#st_char = sidebar_student_characteristics()

# Prediction
home_prediction()