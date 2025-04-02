from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 블루프린트 등록
    from app.routes.quiz_routes import quiz_bp
    app.register_blueprint(quiz_bp)
    
    return app
