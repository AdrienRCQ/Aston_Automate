from flask import Flask
# from flask_mysqldb import MySQL

# mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuration
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = 'ton_mot_de_passe'
    # app.config['MYSQL_DB'] = 'flask_app'
    # app.config['SECRET_KEY'] = 'ta_cle_secrete'

    # Initialisation de MySQL
    # mysql.init_app(app)

    # Import des Blueprints
    # from tasks.routes import tasks_bp
    from app.lab.routes import lab_bp

    # Enregistrement des Blueprints
    # app.register_blueprint(tasks_bp, url_prefix='/tasks')
    app.register_blueprint(lab_bp,url_prefix='/api/lab')

    return app
