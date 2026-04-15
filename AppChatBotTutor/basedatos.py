# basedatos.py
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Ruta al directorio del proyecto
basedir = os.path.abspath(os.path.dirname(__file__))

def init_db(app):
    """
    Inicializa la base de datos con la aplicación Flask.
    """
    # ¡Importante! Cambia 'site.db' a 'tutorepl.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tutorepl.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    print(f"Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")

def create_tables(app):
    """
    Crea las tablas de la base de datos si no existen.
    Debe llamarse dentro del contexto de la aplicación.
    """
    with app.app_context():
        db.create_all() # ¡Descomenta esta línea para que cree las tablas!
    print("Tablas de la base de datos creadas/verificadas.")           
        # Flask-SQLAlchemy intentaría crear la tabla 'user' si el modelo se llama 'User'.
        # Si ya tienes una tabla 'usuarios', no queremos que cree otra.
        #pass # No hacemos nada aquí, ya que la tabla ya existe.
    #print("Verificación de tablas de la base de datos (se asume que 'usuarios' ya existe).")