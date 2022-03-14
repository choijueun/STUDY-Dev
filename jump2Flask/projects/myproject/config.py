import os

BASE_DIR = os.path.dirname(__file__)

# DB 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Flask-WTF : CSRF 토큰
SECRET_KEY = "dev"