"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Frontend via Streamlit
Page : Home (Principale)
"""
# Import modules :
from Tools.streamlit_app_core import *
# Import component :
from components.GUI_components import sidebar_loader
# Import librairies :
import streamlit as st

# --------------- Configuration de l'onglet ---------------
st.set_page_config(page_title="Aston Automate", page_icon="images/Aston_icon.png")

# --------------- Configuration de la sidebar ---------------
sidebar_loader()

# --------------- Configuration de l'en-tête' ---------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("images/Aston_icon.png")
with col2:
    st.title("Aston Automate")

# --------------- Configuration de la page ---------------
st.markdown("""
            
<h2> Bienvenu sur l'outil Aston Automate </h2>
Cet outil a pour but de simplifier la gestion du quotidien :
            
- Liste de course ;
- Validation des TIG + Notification
            

            """, unsafe_allow_html=True)

