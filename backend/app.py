"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Backend Flask pour la gestion de l'application métier
"""

# ---------- Importations ----------
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3 as bdd
import os

# ---------- Configuration ----------
app = Flask(__name__)
DATABASE = "aston_automate.db"


# ---------- Gestion de la base de données ----------
def init_db():
    """Initialise la base de données si elle n'existe pas"""
    conn = bdd.connect(DATABASE)
    c = conn.cursor()

    # Création des tables si elles n’existent pas
    c.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER DEFAULT 1
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_db_connection():
    """Crée une connexion SQLite et renvoie un objet de connexion"""
    conn = bdd.connect(DATABASE)
    conn.row_factory = bdd.Row
    return conn


# ---------- Routes API ----------
@app.route("/api/test", methods=["GET"])
def hello():
    name = request.args.get("name", "Inconnu")
    return jsonify({"message": f"Bonjour, {name} !"})


# ----- Courses -----
@app.route("/api/courses", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name")
    quantity = data.get("quantity", 1)

    if not name:
        return jsonify({"error": "Le nom est requis pour l'ajouter dans la liste"}), 400

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO courses (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()

    item_id = c.lastrowid
    c.execute("SELECT * FROM courses WHERE id = ?", (item_id,))
    new_item = dict(c.fetchone())

    conn.close()
    return jsonify(new_item), 201


@app.route("/api/courses/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM courses WHERE id = ?", (item_id,))
    item = c.fetchone()
    if not item:
        conn.close()
        return jsonify({"error": "Élément introuvable !"}), 404

    c.execute("DELETE FROM courses WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Élément {item_id} supprimé avec succès"}), 200


@app.route("/api/courses", methods=["GET"])
def get_items():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    items = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(items)


# ----- Tasks -----
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(rows)


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    due_date = data.get("due_date")
    email = data.get("email")

    if not title or not due_date or not email:
        return jsonify({"error": "title, due_date et email sont requis"}), 400

    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (title, description, due_date, email) VALUES (?, ?, ?, ?)",
        (title, description, due_date, email)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Tâche ajoutée avec succès"}), 201


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    item = c.fetchone()
    if not item:
        conn.close()
        return jsonify({"error": "Élément introuvable !"}), 404
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Élément {task_id} supprimé avec succès"}), 200


# ---------- Lancement ----------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
