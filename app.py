from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://brandonnoone@localhost:5432/hyrule_health_care_2"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *

from seeds import seed
app.cli.add_command(seed)

from controller.vet_controller import vets_blueprint
from controller.location_controller import locations_blueprint
from controller.animal_controller import animals_blueprint

app.register_blueprint(vets_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug = True)
