from db.run_sql import run_sql

from models.country import Country
from models.city import City


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country



def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row ['name'], row ['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['id'])
    return country



def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE country SET (name) = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)


#     def cities(country):
#         cities = []

#         sql = "SELECT * FROM cities Where country_id = %s"
#         values = [user.id]
#         results = run_sql(sql, values)

#         for row in results:
#             city = City(row['name'], row['visited'], row['id'])
#             cities.append(city)
#         return cities

#sk about cities/countries and city/country to know which is meant to be which - what is referring to?? Same for task_repository.