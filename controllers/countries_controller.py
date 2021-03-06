from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("/countries/index.html", countries=countries, cities=cities)
    # first countries refers to variable in html file and = countries is the list of countries from line above

#show
#get

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country=country)


# #new
# #get
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template('countries/new.html')

# #create
# #post

@countries_blueprint.route("/countries", methods= ['POST'])
def create_country():
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect('/countries')

#    #would it need country id in here at all?  
#    #does user get to create countries? do they need to? How would they attach image for it? Does it match the brief???



#edit
#get
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country= country )
#check this as its wierd agains the cities one. not finished.


# #update
# #put
@countries_blueprint.route("/countries/<id>", methods= ['POST'])
def update_country(id):
    name = request.form ['name']
    country = Country(name, id)
    country_repository.update(country)
    return redirect('/countries')


# #delete
# #delete

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')