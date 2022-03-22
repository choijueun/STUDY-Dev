from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from sqlalchemy import MetaData

import config

# 객체 생성
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# create_app은 정해진 이름
def create_app():           # application factory: app 객체를 생성하는 함수
    app = Flask(__name__)   # Flask app: Flask class로 만든 객체
    app.config.from_object(config)  # 설정
    
    # ORM
    db.init_app(app)            # 초기화
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models        # Model 인식
    
    # Blueprint
    from .views import main, question, answer, user_auth, comment, vote
    app.register_blueprint(main.bp)   #블루프린트 객체(bp) 등록
    app.register_blueprint(question.bp)   
    app.register_blueprint(answer.bp)
    app.register_blueprint(user_auth.bp)
    app.register_blueprint(comment.bp)
    app.register_blueprint(vote.bp)
    
    # Filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    # Markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    
    return app