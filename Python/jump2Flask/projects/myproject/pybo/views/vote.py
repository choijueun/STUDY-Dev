from datetime import datetime

from flask import Blueprint, url_for, g, flash
from werkzeug.utils import redirect

from .. import db
from ..models import Question, Answer
from .user_auth import login_required

bp = Blueprint('vote', __name__, url_prefix='/vote')

@bp.route('/question/<int:question_id>/')
@login_required
def question(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user.username == _question.user_id:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

@bp.route('/answer/<int:answer_id>/')
@login_required
def answer(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    if g.user.username == _answer.user_id:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=_answer.question.id))