import streamlit as st

# --------------- Configuration de l'onglet ---------------
st.set_page_config(page_title="Aston Automate", page_icon="frontend/images/Aston_icon.png")

# --------------- Configuration de la sidebar ---------------
st.sidebar.image("frontend/images/icon.png")
st.sidebar.markdown('<div class="sidebar-footer">@ 2025 Aston Automate </div>')

# --------------- Configuration de l'en-tête' ---------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("frontend/images/Aston_icon.png")
with col2:
    st.title("Aston Automate")

# --------------- Configuration de la page ---------------
st.markdown("""
            
<h2> Bienvenu sur l'outil Aston Automate </h2>
Cet outil a pour but de simplifier la gestion du quotidien :
            
- Liste de course ;
- Validation des TIG + Notification
            

            """, unsafe_allow_html=True)