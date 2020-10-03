
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_blueprint = Blueprint
("country" __name__)

@country_blueprint.route("/country")
def country():
    country = country_repository.select_all()
    return render_template("/country/index.html", all_countries = country)


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