from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/hello')
def hello_pybo():           # 라우트 함수: annotation으로 매핑되는 함수
    return 'Hello, Pybo!'