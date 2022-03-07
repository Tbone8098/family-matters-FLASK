from flask import Flask
app = Flask(__name__)
app.secret_key = 'Whos your daddy? Goons your daddy!'

# DATABASE_SCHEMA = 'family_matters_db'
DATABASE_SCHEMA = 's3p5x7kb9czupn46'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)