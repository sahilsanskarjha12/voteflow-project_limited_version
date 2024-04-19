from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

# Define user data store
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# Configure security
security = Security(app, user_datastore)
