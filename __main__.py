import os

def launch_gui():
    os.system("python3 -m streamlit run frontend/home.py")

def launch_app():
    os.system("python3 backend/app.py")


if __name__ == "__main__":
    launch_app()
    