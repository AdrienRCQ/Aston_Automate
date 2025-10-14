import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:5000/api/courses"

# --------------- Configuration de l'onglet ---------------
st.set_page_config(page_title="Liste de courses", page_icon="images/Aston_icon.png")

# --------------- Configuration de la sidebar ---------------
st.sidebar.image("images/icon.png")
st.sidebar.markdown('<div class="sidebar-footer">@ 2025 Aston Automate </div>', unsafe_allow_html=True)

# --------------- Configuration de l'en-tête' ---------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("images/Aston_icon.png")
with col2:
    st.title("Aston Automate")

# --------------- Configuration de la page ---------------

st.title("🛒 Liste de courses ")

# --- Afficher la liste des courses ---
def load_items():
    try:
        res = requests.get(API_URL)
        if res.status_code == 200:
            return res.json()
        else:
            st.error("Erreur lors du chargement des données.")
    except requests.exceptions.ConnectionError:
        st.error("Le backend Flask n’est pas accessible.")
    return []


# --- Ajouter un article ---
with st.form("add_item_form"):
    name = st.text_input("Nom de l’article")
    quantity = st.number_input("Quantité", min_value=1, value=1)
    submit = st.form_submit_button("Ajouter")

    if submit and name:
        res = requests.post(API_URL, json={"name": name, "quantity": quantity})
        if res.status_code == 201:
            st.success(f"'{name}' ajouté à la liste !")
        else:
            st.error("Erreur lors de l’ajout.")

# --- Rafraîchir la liste ---
if st.button("🔄 Rafraîchir la liste"):
    st.experimental_rerun()

# --- Afficher les articles ---
items = load_items()
if items:
    df = pd.DataFrame(items, )
    st.dataframe(df, use_container_width=True)

    # Supprimer un article
    delete_id = st.selectbox("Sélectionner un article à supprimer :", [i["id"] for i in items])
    if st.button("🗑️ Supprimer l’article"):
        res = requests.delete(f"{API_URL}/{delete_id}")
        if res.status_code == 200:
            st.success("Article supprimé !")
        else:
            st.error("Erreur lors de la suppression.")
