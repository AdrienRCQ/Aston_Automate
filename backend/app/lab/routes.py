from flask import *

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/')
def hello():
    return {'message': 'Hello, World!'}
