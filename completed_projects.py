from models import Project, db

PROJECTS = Project[{
                db.id:1, 
                db.title:'Number Guessing Game', 
                db.date:'November 2022', 
                db.description:f'''For this project, I created a random number 
                                guessing game in which the player is asked to: 
                                "Pick a number between 1 and 10". The player's 
                                job is to make a guess, and the program will tell 
                                them whether their guess is too high or too low. 
                                Their next guess is based on what the program has 
                                told them. The game ends when the player guesses 
                                the correct number. Usually, players will try to 
                                do this in the lowest number of tries possible.''',
                db.skills:f'''Catching exceptions, Creating a loop, 
                                Accepting user input, Conditional statements''',
                db.url:'https://github.com/chelsearumsey/Project-1---Number-Guessing-Game'
                }, {
                db.id:2, 
                db.title:'Basketball Stats Tool', 
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
                db.url: 'https://github.com/chelsearumsey/Project-2---Basketball-Stats-Tool'
                }, {
                db.id:3, 
                db.title:'Phrase Hunter', 
                db.date:'February 2023', 
                db.description: f'''For this project, I created a word guessing game: 
                                    "Phrase Hunter." I used Python and object-oriented 
                                    programming approaches to select a phrase at random, 
                                    hidden from the player. The player tries to guess the 
                                    phrase by inputting individual characters.''',
                db.skills: f'''Object oriented programming, Creating loops, Accepting 
                                user input, Conditional statements ''',
                db.url: 'https://github.com/chelsearumsey/Project-3---Phrase-Hunter'
                }, {
                db.id:4, 
                db.title:'Store Inventory with SQLAlchemy', 
                db.date:'March 2023', 
                db.description: f'''For this project, I built a console application that 
                                    allows you to easily interact with data for a store's 
                                    inventory. The data was cleaned from the CSV file before 
                                    being added to the database. All interactions with the 
                                    records used ORM methods for viewing records, creating 
                                    records, and exporting a new CSV backup.''',
                db.skills: f'''Used knowledge of CSV, File I/O, SQL, and Git, Set up a virtual environment 
                                with Python, Cleaned CSV data, and Created a database using SQLAlchemy''',
                db.url: 'https://github.com/chelsearumsey/Project-4---Store-Inventory-with-SQLAlchemy'
                }] 