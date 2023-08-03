from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Location, Vet, Animals
from app import db

animals_blueprint = Blueprint("animals",__name__)

@animals_blueprint.route("/animals")
def animal():
    animals_obj = Animals.query.all()
    return render_template("animals/index.jinja", animals = animals_obj)


@animals_blueprint.route("/animals/<id>/show")
def animals_id_obj(id):
    animal = Animals.query.get(id)
    return render_template("animals/show.jinja", animal = animal)



@animals_blueprint.route('/animals/<id>/update')
def edit_animal(id):
    animal = Animals.query.get(id)
    return render_template('/animals/update.jinja', animal = animal)


@animals_blueprint.route("/animals/<id>/update", methods=['POST'])
def update_animal(id):
    
    name = request.form ['name']
    species = request.form ['species']
    age = request.form ['age']
    owner = request.form ['owner']
    animal = Animals.query.get(id)
    animal.name = name
    animal.species = species
    animal.age = age
    animal.owner = owner
    db.session.commit()
    return redirect("/animals")



    # animal = Animals.query.get(id)
    # name = request.form['name']
    # species = request.form['species']
    # age = request.form['age']
    # owner = request.form['owner']
#     animal.name = name
#     animal.species = species
#     animal.age = age
#     animal.owner = owner
#     db.session.commit()
#     return redirect("/animals")

@animals_blueprint.route('/animals/new')
def add_animal_page():
    animals = Animals.query.all()
    return render_template('/animals/new.jinja', animals=animals)

@animals_blueprint.route("/animals/new", methods=["POST"])
def add_animal():
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    owner = request.form['owner']

    new_animal = Animals(name=name, species=species, age=age ,owner=owner)

    db.session.add(new_animal)
    db.session.commit()
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    Animals.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/animals')

