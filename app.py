from flask import (render_template, redirect, 
                   url_for, request)
from models import db, Project, app
from completed_projects import PROJECTS


def insert_project_data():
    for project in PROJECTS:
        project_in_db = Project.query.filter(Project.title==project['title']).one_or_none()
        if project_in_db == None:
            id = project['id']
            title = project['title']
            date = project['date']
            description = project['description']
            skills = project['skills']
            url= project['url']
            new_project = Project(id=id, title=title, date=date, 
                                    description=description, 
                                    skills=skills, url=url)
            db.session.add(new_project)
            db.session.commit()
            

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'], 
                              description=request.form['desc'], skills=request.form['skills'], 
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/projects/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project():
    pass


@app.route('/projects/<id>/delete')
def delete_project():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_project_data()
    app.run(debug=True, port=8000, host='0.0.0.0')
    
    
    