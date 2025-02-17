from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from App.controllers import (
    create_users,
    create_admin
)

from App.main import socketio, app
from App import db

manager = Manager(app)
migrate = Migrate(app, db)

# add migrate command
manager.add_command('db', MigrateCommand)

# initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

# serve command
@manager.command
def serve():
    print('Application running in '+app.config['ENV']+' mode')
    socketio.run(app, host='localhost', port=8080, debug=app.config['ENV'] == 'development')


@manager.command
def make_users():
    create_users([
        {
            'first_name': 'Bob',
            'last_name': 'Smith',
            'email': 'bob@mail.com',
            'password': 'bobpass',
        },
        {
            'first_name': 'Jame',
            'last_name': 'Smith',
            'email': 'jane@mail.com',
            'password': 'janepass',
        },
        {
            'first_name': 'Rick',
            'last_name': 'Smith',
            'email': 'rick@mail.com',
            'password': 'rickpass',
        }
    ])
    print("users created")


#creates an admin
@manager.command
def makeAdmin(fname="robAdmin", lname="Smith", email="robadmin@mail.com", password="bobpass"):
    create_admin(fname, lname, email, password)
    print(fname+' created!')

# CREATE ADMIN 
@manager.command
def createAdmin():
    firstname = input('Enter ADMIN firstname :')
    lastname = input('Enter ADMIN lastname :')
    email = input('Enter ADMIN email :')
    password = input('Enter ADMIN password :')    
    admin = create_admin(firstname, lastname, email, password)
    print('Admin '+firstname+' created ')
    
if __name__ == "__main__":
    manager.run()
