from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connexion à la base de données
        cur = current_app.mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):
            session['logged_in'] = True
            session['username'] = username
            flash('Connexion réussie !', 'success')
            return redirect(url_for('tasks.tasks'))
        else:
            flash('Identifiants incorrects.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Vous êtes déconnecté.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        # Connexion à la base de données
        cur = current_app.mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, hashed_password))
        current_app.mysql.connection.commit()
        cur.close()

        flash('Compte créé avec succès !', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
