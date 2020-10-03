from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City 
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

tasks_blueprint = Blueprint("cities", __name__)

@tasks_blueprint.route("/cities")
def cities():
    city = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)


#new 
#get


#create
#post




#show
#get



#edit
#get



#update
#put



#delete
#delete