from flask import Blueprint
from flask import render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route("/")
def main():
    return render_template('main.html')





   