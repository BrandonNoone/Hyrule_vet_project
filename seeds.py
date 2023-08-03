from app import db
from models import Vet, Location, Animals
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Animals.query.delete()
    Vet.query.delete()
    Location.query.delete()

    location_1 = Location(name="Hyrule Castle Vets",founded="1404")
    location_2 = Location(name="Kakariko Village Vets",founded="1443")
    location_3 = Location(name="Gerudo Desert Vets",founded="1398")

    db.session.add(location_1)
    db.session.add(location_2)
    db.session.add(location_3)

#------------------------------------------------------------------------------
    vet_1 = Vet(name="Dr.Borville", location=location_1)
    vet_2 = Vet(name="Dr.Biggoron", location=location_2)
    vet_3 = Vet(name="Tingle",location = location_3 )

    db.session.add(vet_1)
    db.session.add(vet_2)
    db.session.add(vet_3)

#------------------------------------------------------------------------------
    
    animal_1 = Animals(name="Kiba", species="dog",age= 7, owner="Tammy", vet=vet_1)
    animal_2 = Animals(name="Kit", species="cat", age= 2, owner="Holly", vet=vet_2)
    animal_3 = Animals(name="Hoof Hearted", species="horse",age=13 , owner="Liam", vet=vet_2)
    animal_4 = Animals(name="Bob", species="fish", age=1,owner="Steph", vet=vet_2)
    animal_5 = Animals(name="Vincent van", species="goat",age=4, owner="Brandon", vet=vet_3)
    animal_6 = Animals(name="Yoda", species="frog", age= 1, owner="Summer", vet=vet_3)

    db.session.add(animal_1)
    db.session.add(animal_2)
    db.session.add(animal_3)
    db.session.add(animal_4)
    db.session.add(animal_5)
    db.session.add(animal_6)

    db.session.commit()