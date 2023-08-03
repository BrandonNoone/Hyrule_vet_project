from app import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    founded = db.Column(db.String(64))
    vets = db.relationship('Vet', backref='location')

def __repr__(self):
    return f"<Location: {self.id}: {self.name}: {self.founded}>"


#----------------------------------------------------------------------


class Vet(db.Model):
    __tablename__ = "vets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    animal = db.relationship('Animals', backref='vet')

def __repr__(self):
    return f"<Vets: {self.id}: {self.name}: {self.Location_id}>"


#----------------------------------------------------------------------


class Animals(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64))
    species = db.Column(db.String(64))
    age = db.Column(db.String(64))
    owner = db.Column(db.String(64))
    vet_id = db.Column(db.Integer, db.ForeignKey("vets.id"))
    

def __repr__(self):
    return f"<Animals: {self.id}: {self.name}: {self.species}: {self.age}: {self.owner}: {self.Vet_id}>"
