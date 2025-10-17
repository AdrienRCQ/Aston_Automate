"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Frontend via Streamlit
Page : Home (Principale)
"""

import streamlit as st
from Tools.streamlit_app_core import *

# --------------- Configuration de l'onglet ---------------
st.set_page_config(page_title="Aston Automate", page_icon="images/Aston_icon.png")

# --------------- Configuration de la sidebar ---------------
st.sidebar.image("images/icon.png")
st.sidebar.markdown("---")

exit_app = st.sidebar.button("❌ Shut Down")
relaunch_app = st.sidebar.button("🔄 Reboot")
st.sidebar.markdown('<div class="sidebar-footer">@ 2025 Aston Automate </div>', unsafe_allow_html=True)

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


if exit_app:
    shutdown_app()

if relaunch_app:
    reboot_app()