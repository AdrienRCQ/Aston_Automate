from Tools.streamlit_app_core import *

def sidebar_loader():
    st.sidebar.image("images/icon.png")
    st.sidebar.markdown("---")

    exit_app = st.sidebar.button("❌ Shut Down")
    relaunch_app = st.sidebar.button("🔄 Reboot")
    st.sidebar.markdown('<div class="sidebar-footer">@ 2025 Aston Automate </div>', unsafe_allow_html=True)

    if exit_app:
        shutdown_app()

    if relaunch_app:
        reboot_app()