from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_webserver():
	return 'Hello, 321son Family!'

@bp.route('/')
def index():
    # current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))
