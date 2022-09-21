from flask import Flask
from .extensions import db, migrate
from .routes.uc_bp import uc_bp

def create_app():
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.create_all()
    
    migrate.init_app(app)

    app.register_blueprint(uc_bp)


    @app.route('/health')
    def health():
        return 'Up and running', 200


    return app