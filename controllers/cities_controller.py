from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City 
import repositories.city_repositories as city_repositories
import repositories.country_repositories as country_repositories

tasks_blueprint = Blueprint("cities", __name__)

@tasks_blueprint.route("/cities")
def cities():
    city = city_repositories.select_all()
    return render_template("cities/index.html", all_cities = cities)