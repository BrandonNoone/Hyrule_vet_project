from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Animals, Vet, Location
from app import db

locations_blueprint = Blueprint("location",__name__)

@locations_blueprint.route("/locations")
def location():
    locations_obj = Location.query.all()
    return render_template("locations/index.jinja", locations = locations_obj)

@locations_blueprint.route("/locations/<id>")
def location_id(id):
    location_id_obj = Location.query.get(id)
    return render_template("/locations/show.jinja", locations_id = location_id_obj)

@locations_blueprint.route("/location/<id>/show")
def location_id_show(id):
    location_obj = Location.query.get(id)
    return render_template("location/show.jinja", locations_id_show = location_obj)

# @locations_blueprint.route("locations/new", methods=['POST'])
# def new_location():
#     locations = Location.query.all()
#     return render_template("locations/new.jinja", locations=locations)

# @locations_blueprint.route("/locations/new", methods=['POST'])
# def create_location():
#     location_id = request.form["location_id"]
#     db.session.add(location_id)
#     db.session.commit()
#     return redirect('/locations')

# @locations_blueprint.route("/location/<id>")
# def location_id(id):
#     location = Location.query.get(id)
#     return render_template("/locations/show.jinja", location=location)