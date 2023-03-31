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


@app.route('/projects/about')
def about():
    return render_template('about.html')


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    projects = Project.query.all()
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'], 
                              description=request.form['desc'], skills=request.form['skills'], 
                              url=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects = projects)


@app.route('/projects/<id>')
def detail(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project, projects = projects)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.date=request.form['date']
        project.description=request.form['desc'] 
        project.skills=request.form['skills'] 
        project.url=request.form['github']
        db.session.commit()
        return redirect(url_for('detail', id=id))
    return render_template('edit_project.html', project = project)


@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index', project=project))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_project_data()
    app.run(debug=True, port=8000, host='0.0.0.0')
    
    
    