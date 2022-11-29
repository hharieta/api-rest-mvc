import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# creates the variable basedir pointing 
# to the directory that the program is running in.
base_dir = pathlib.Path(__file__).parent.resolve()
# uses the basedir variable to create the Connexion app 
# instance and give it the path to the directory 
# that contains your specification file.
connex_app = connexion.App(__name__.split(".")[0], specification_dir=base_dir)

# creates a variable, app,
# which is the Flask instance initialized by Connexion
app = connex_app.app
# tell SQLAlchemy to use SQLite as the database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_dir / 'database' / 'people.sqlite'}"

# turns the SQLAlchemy event system off. The event system 
# generates events that are useful in event-driven programs, 
# but it adds significant overhead. Since you’re not creating 
# an event-driven program, you turn this feature off.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initializes SQLAlchemy by passing the app 
# configuration information to SQLAlchemy 
# and assigning the result to a db variable.
db = SQLAlchemy(app)

# nitializes Marshmallow and allows it 
# to work with the SQLAlchemy components attached to the app.
ma = Marshmallow(app)