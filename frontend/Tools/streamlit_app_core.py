"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Frontend via Streamlit
"""

import os
import sys
import time
import psutil
import keyboard
import subprocess
import streamlit as st

def reboot_app():
    """
    Redémarre proprement l'application Streamlit :
    - Ferme l'onglet courant
    - Termine le process Streamlit actuel
    - Relance le même script
    """
    st.info("🔄 Redémarrage de l'application en cours...")

    # Pause pour retour visuel
    time.sleep(2)

    # Fermer l’onglet du navigateur (si exécution locale)
    try:
        keyboard.press_and_release('ctrl+w')
    except:
        pass

    # Relancer le script actuel dans un nouveau process
    python = sys.executable
    script = sys.argv[0]
    subprocess.Popen([python, "-m", "streamlit", "run", script])

    # Terminer le process Streamlit courant
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()

def shutdown_app():
    # Give a bit of delay for user experience
    time.sleep(2)
    # Close streamlit browser tab
    keyboard.press_and_release('ctrl+w')
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()
