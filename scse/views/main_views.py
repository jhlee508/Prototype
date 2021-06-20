from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_scse():
    return 'Hello, SCSE!'


@bp.route('/', methods=['GET', 'POST'])
def index():
    value1, value2, value3 = 4, 10, 30
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        value3 = request.form['value3']
        print(value1, value2, value3)

    return render_template('index.html', value1=value1, value2=value2, value3=value3)
