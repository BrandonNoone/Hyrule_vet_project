from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Location, Animals, Vet
from app import db

vets_blueprint = Blueprint("vet", __name__)

@vets_blueprint.route("/vets")
def vet():
    vets_obj = Vet.query.all()
    return render_template("vets/index.jinja", vets = vets_obj) 

@vets_blueprint.route("/vets/<id>")
def vets_id(id):
    vets_id_obj = Vet.query.get(id)
    return render_template("/vets/show.jinja", vets_id = vets_id_obj)
