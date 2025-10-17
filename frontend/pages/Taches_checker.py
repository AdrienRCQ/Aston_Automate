"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Frontend via Streamlit
Page : Tache Checker 
"""

import streamlit as st
import requests
from datetime import datetime
from Tools.streamlit_app_core import *

API_URL = "http://localhost:5000"

# --------------- Configuration de l'onglet ---------------
st.set_page_config(page_title="Liste de courses", page_icon="images/Aston_icon.png")

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

st.title("🗓️ Gestionnaire de tâches récurrentes")

menu = st.sidebar.radio("Navigation", ["Voir les tâches", "Ajouter une tâche"])

if menu == "Ajouter une tâche":
    title = st.text_input("Titre")
    desc = st.text_area("Description")
    due_date = st.date_input("Date d'échéance")
    email = st.text_input("Email pour notification")

    if st.button("Ajouter"):
        data = {
            "title": title,
            "description": desc,
            "due_date": due_date.isoformat(),
            "email": email
        }
        st.warning(data)
        res = requests.post(f"{API_URL}/api/tasks", json=data)
        if res.status_code == 200:
            st.success("Tâche ajoutée avec succès ✅")

elif menu == "Voir les tâches":
    res = requests.get(f"{API_URL}/api/tasks")
    if res.status_code == 200:
        tasks = res.json()
        for t in tasks:
            st.write(f"{t["id"]} - **{t["title"]}** — échéance : {t["due_date"]}")
            st.caption(t["description"])


if exit_app:
    shutdown_app()

if relaunch_app:
    reboot_app()