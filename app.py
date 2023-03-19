from flask import (render_template, redirect, 
                   url_for, request)
from models import db, Project, app


@app.route('/')
def index():
    return f'Thank you for viewing my programming portfolio!'


@app.route('/project/new')
def create():
    pass


@app.route('/project/<id>')
def detail():
    pass


@app.route('/project/<id>/edit')
def edit_project():
    pass


@app.route('/project/<id>/delete')
def delete_project():
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')
