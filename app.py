from flask import (render_template, redirect, 
                   url_for, request)
from models import db, Project, app


def insert_project_data():
        project1= Project({db.id:1, db.title:'Number Guessing Game', 
                    db.date:'November 2022', 
                    db.description: f'''For this project, I created a random number 
                                    guessing game in which the player is asked to: 
                                    "Pick a number between 1 and 10". The player's 
                                    job is to make a guess, and the program will tell 
                                    them whether their guess is too high or too low. 
                                    Their next guess is based on what the program has 
                                    told them. The game ends when the player guesses 
                                    the correct number. Usually, players will try to 
                                    do this in the lowest number of tries possible.''',
                    db.skills: f'''Catching exceptions, Creating a loop, 
                                    Accepting user input, Conditional statements''',
                    db.url: 'https://github.com/chelsearumsey/Project-1---Number-Guessing-Game'})
        project2= Project({db.id:1, db.title:'Basketball Stats Tool', 
                    db.date:'January 2023', 
                    db.description: f'''For this project, I was given a list of teams and players, 
                                        tasked with cleaning up the player data, and then organizing 
                                        the players into equal teams for the upcoming basketball season.

                                        I applied my knowledge of built-in Python data types and combined 
                                        these types to create structures to store and organize a team of 
                                        basketball players into distributed teams. This tool not only balances 
                                        the teams by the total number of players but also lets you generate some 
                                        statistics for a given team.''',
                    db.skills: f'''Cleaning data, Appending data to multiple lists, 
                                    Catching exceptions, Creating a loop, Accepting 
                                    user input, Conditional statements''',
                    db.url: 'https://github.com/chelsearumsey/Project-2---Basketball-Stats-Tool'})
        project3= Project({db.id:1, db.title:'Phrase Hunter', 
                    db.date:'February 2023', 
                    db.description: f'''For this project, I created a word guessing game: 
                                        "Phrase Hunter." I used Python and object-oriented 
                                        programming approaches to select a phrase at random, 
                                        hidden from the player. The player tries to guess the 
                                        phrase by inputting individual characters.''',
                    db.skills: f'''Object oriented programming, Creating loops, Accepting 
                                    user input, Conditional statements ''',
                    db.url: 'https://github.com/chelsearumsey/Project-3---Phrase-Hunter'})
        project4= Project({db.id:1, db.title:'Store Inventory with SQLAlchemy', 
                    db.date:'March 2023', 
                    db.description: f'''For this project, I built a console application that 
                                        allows you to easily interact with data for a store's 
                                        inventory. The data was cleaned from the CSV file before 
                                        being added to the database. All interactions with the 
                                        records used ORM methods for viewing records, creating 
                                        records, and exporting a new CSV backup.''',
                    db.skills: f'''Used knowledge of CSV, File I/O, SQL, and Git, Set up a virtual environment 
                                    with Python, Cleaned CSV data, and Created a database using SQLAlchemy''',
                    db.url: 'https://github.com/chelsearumsey/Project-4---Store-Inventory-with-SQLAlchemy'})
        db.session.add(project1, project2, project3, project4)
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
    