"""
***** Aston Automate *****
Auteur : Adrien RICQUE
Date de création : 14/10/2025

Description : Ce fichier regroupe les éléments permettant la gestion de l'application métier (backend) via flask

"""
# Importation des modules


# Importation des librairies 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "Inconnu")
    return jsonify({"message": f"Bonjour, {name} !"})


# ---------- Modèles ------------------
class ElementCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "quantity": self.quantity}

# ---------- Gestion des routes ------------------
@app.route("/api/courses", methods=["GET"])
def get_list():
    items = ElementCourse.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route("/api/courses", methods=["POST"])
def add_item():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity", 1)
    if not name:
        return jsonify({"error": "Le nom est requis pour l'ajouter dans la liste"})
    new_item = ElementCourse(name=name, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@app.route("/api/courses/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = ElementCourse.query.get(item_id)
    if not item:
        return jsonify({"error": "Element introuvable !"}), 404
    db.session.delete(item)
    db.session.commit()

# ---------- Initialisation ------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
