from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from flask_mysqldb import MySQL

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def tasks():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))

    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE username = %s", [session['username']])
    tasks = cur.fetchall()
    cur.close()

    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))

    title = request.form['title']
    cur = current_app.mysql.connection.cursor()
    cur.execute("INSERT INTO tasks(title, username) VALUES(%s, %s)", (title, session['username']))
    current_app.mysql.connection.commit()
    cur.close()

    flash('Tâche ajoutée !', 'success')
    return redirect(url_for('tasks.tasks'))

@tasks_bp.route('/delete/<int:id>')
def delete_task(id):
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))

    cur = current_app.mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s AND username = %s", (id, session['username']))
    current_app.mysql.connection.commit()
    cur.close()

    flash('Tâche supprimée !', 'success')
    return redirect(url_for('tasks.tasks'))
