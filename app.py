from flask import (render_template, redirect, 
                   url_for, request)
from models import db, Project, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'],
                              description=request.form['desc'], skills=request.form['skills'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def detail():
    return render_template('detail.html')


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project():
    pass


@app.route('/projects/<id>/delete')
def delete_project():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')
