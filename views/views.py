from flask import Blueprint

# create the main Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    return 'Blueprint Hello world!'
