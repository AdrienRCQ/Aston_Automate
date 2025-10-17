import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv

load_dotenv()
LOGIN = getenv('MAIL_LOGIN')
## DON'T PUT YOUR TOKEN DIRECTLY HERE !!!
TOKEN = getenv('MAIL_TOKEN')


def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['From'] = "ton_email@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(LOGIN, TOKEN)  # mot de passe applicatif Gmail
        server.send_message(msg)

def check_tasks():
    conn = sqlite3.connect('aston_automate.db')
    c = conn.cursor()
    c.execute("SELECT id, title, due_date, email FROM tasks WHERE notified=0")
    tasks = c.fetchall()

    now = datetime.now()

    for task in tasks:
        task_id, title, due_date, email = task
        due = datetime.fromisoformat(due_date)
        if due < now:
            send_email(email, f"Tâche en retard : {title}", f"La tâche '{title}' était prévue pour le {due_date}.")
            c.execute("UPDATE tasks SET notified=1 WHERE id=?", (task_id,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    check_tasks()
